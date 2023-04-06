import base64
import io

import dlib
import face_recognition
import numpy as np
import json
from PIL import Image, ImageDraw

from handler.models import Employer
from sqlalchemy.orm import sessionmaker

from datetime import date, datetime, timedelta
from collections import namedtuple


class Prediction:
    def __init__(self, train_model, distance_threshold):
        self.__model = train_model
        self.__distance_threshold = distance_threshold
        self.__shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    def _align_face(self, image, face_location):
        rect = dlib.rectangle(face_location[3], face_location[0], face_location[1], face_location[2])
        shape = self.__shape_predictor(image, rect)
        aligned_face = dlib.get_face_chip(image, shape)
        return aligned_face
    
    
    @staticmethod
    def show_prediction_labels_on_image(img_path, predictions, image_extension):
        pil_image = Image.open(io.BytesIO(img_path)).convert("RGB")
        draw = ImageDraw.Draw(pil_image)

        for name, (top, right, bottom, left) in predictions:
            # Draw a box around the face using the Pillow module
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

            # There's a bug in Pillow where it blows up with non-UTF-8 text
            # when using the default bitmap font
            name = name.encode("UTF-8")

            # Draw a label with a name below the face
            text_width, text_height = draw.textsize(name)
            draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
            draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

        # Remove the drawing library from memory as per the Pillow docs
        del draw

        # convert pil to base64 encode image
        buffered = io.BytesIO()
        pil_image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())

        # Display the resulting image
        return f'data:image/{image_extension};base64,{img_str.decode()}'



    def predict_image(self, data: bytes, image_extension: str):
        # get data model from database
        data_model = self.__model
        # Load image file and find face locations
        x_img = face_recognition.load_image_file(io.BytesIO(data))
        x_face_locations = face_recognition.face_locations(x_img)

        # If no faces are found in the image, return an empty result.
        if len(x_face_locations) == 0:
            return []

        # Align faces and find encodings for faces in the test image
        aligned_faces = [self._align_face(x_img, face_location) for face_location in x_face_locations]
        faces_encodings = [face_recognition.face_encodings(np.array(aligned_face))[0] for aligned_face in aligned_faces]

        # Use the KNN model to find the best matches for the test face
        closest_distances = data_model.kneighbors(faces_encodings, n_neighbors=5)
        are_matches = [closest_distances[0][i][0] <= self.__distance_threshold for i in range(len(x_face_locations))]

        # Predict classes and remove classifications that aren't within the threshold
        results = [(pred, loc) if rec else ("unknown", loc) for pred, loc, rec in
                   zip(data_model.predict(faces_encodings), x_face_locations, are_matches)]

        return results



class Helper:
    @staticmethod
    def allowed_file(filename: str) -> bool:
        """Check if filename is allowed
        :return:
        """
        # function to validate acceptable files
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, timedelta):
            return str(obj)
        elif isinstance(obj, datetime):  # Handle datetime objects
            return obj.isoformat()
        elif isinstance(obj, date):  # Add this line to handle date objects
            return obj.isoformat()
        elif isinstance(obj, memoryview):  # This will handle LargeBinary data
            return base64.b64encode(obj.tobytes()).decode('utf-8')
        elif isinstance(obj, bytes):  # This will handle BIT(1) data
            if len(obj) == 1:  # Add this line to check if the length is 1
                return bool(int.from_bytes(obj, byteorder='big'))
            else:
                return obj  # If the length is not 1, return the bytes object unchanged
        return super(CustomJSONEncoder, self).default(obj)

    def encode(self, obj):
        def hint_tuples(item):
            if isinstance(item, tuple) and hasattr(item, '_asdict'):
                return {'__tuple__': True, 'items': item._asdict()}
            if isinstance(item, list) or isinstance(item, set):
                return [hint_tuples(e) for e in item]
            if isinstance(item, dict):
                new_dict = {}
                for key, value in item.items():
                    new_dict[key] = hint_tuples(value)
                return new_dict
            return item

        return super(CustomJSONEncoder, self).encode(hint_tuples(obj))

    def decode(self, obj):
        def hinted_tuples(item):
            if isinstance(item, dict) and '__tuple__' in item:
                return namedtuple('Tuple', item['items'].keys())(*item['items'].values())
            if isinstance(item, list) or isinstance(item, set):
                return [hinted_tuples(e) for e in item]
            if isinstance(item, dict):
                new_dict = {}
                for key, value in item.items():
                    new_dict[key] = hinted_tuples(value)
                return new_dict
            return item

        return hinted_tuples(super(CustomJSONEncoder, self).decode(obj))
def make_json_serializable(obj):
    if isinstance(obj, (list, tuple, set)):
        return [make_json_serializable(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: make_json_serializable(value) for key, value in obj.items()}
    elif hasattr(obj, '_asdict'):  # For namedtuples
        return make_json_serializable(obj._asdict())
    elif isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, date):
        return obj.isoformat()
    elif isinstance(obj, timedelta):
        return str(obj)
    elif isinstance(obj, memoryview):
        return base64.b64encode(obj.tobytes()).decode('utf-8')
    elif isinstance(obj, bytes):
        if len(obj) == 1:
            return bool(int.from_bytes(obj, byteorder='big'))
        else:
            return obj
    else:
        return obj

class EmployerService:
    def __init__(self, engine):
        self.SessionFactory = sessionmaker(bind=engine)

    def get_employers(self):
        session = self.SessionFactory()
        employers = session.query(Employer).order_by(Employer.EmployerID).all()
        session.close()
        return employers

    def get_employer_by_id(self, employer_id):
        session = self.SessionFactory()
        employer = session.query(Employer).filter_by(EmployerID=employer_id).first()
        session.close()
        return employer

    def create_employer(self, employer_data):
        session = self.SessionFactory()
        employer = Employer(**employer_data)
        session.add(employer)
        session.commit()
        session.close()
        return employer

    def update_employer(self, employer_id, employer_data):
        session = self.SessionFactory()
        employer = session.query(Employer).filter_by(EmployerID=employer_id).first()
        for key, value in employer_data.items():
            setattr(employer, key, value)
        session.commit()
        session.close()
        return employer

    def delete_employer(self, employer_id):
        session = self.SessionFactory()
        employer = session.query(Employer).filter_by(EmployerID=employer_id).first()
        session.delete(employer)
        session.commit()
        session.close()





class EmployeeClass:
    def __init__(self):
        pass

    @staticmethod
    def login_employee(conn, email, password):
        with conn.cursor() as cur:
            query = """SELECT E.EmployeeID, E.IsImagesRegistered, E.Name, E.Email
                   FROM Employee AS E
                   WHERE E.IsActive = 1 AND E.IsDeleted = 0 AND E.email = %s AND E.password = %s
                   """
            cur.execute(query, (email, password))
            result = cur.fetchone()
            if not result:
                return None

            # Convert the result to a dictionary
            column_names = [desc[0] for desc in cur.description]
            result_dict = {key: value for key, value in zip(column_names, result)}

            return result_dict
    # Add this function to update the IsImagesRegistered field
    @staticmethod
    def update_employee_images_registered(conn, employee_id, is_images_registered):
        with conn.cursor() as cur:
            query = """UPDATE Employee SET IsImagesRegistered = %s WHERE EmployeeID = %s"""
            cur.execute(query, (is_images_registered, employee_id))
            conn.commit()
        

class EmployerClass:
    def __init__(self):
        pass
    @staticmethod
    async def login_employer(conn, email, password):
        async with conn.cursor() as cur:
            query = "SELECT EmployerID, Name, Email, Token, PhoneNumber, Address, City, State, Country, PostalCode, IndustryType, WebsiteURL, CompanySize, TaxID, CreatedDate, UpdatedDate FROM Employer WHERE IsActive = true AND IsDeleted = false AND email = %s AND password = %s"
            await cur.execute(query, (email, password))
            result = await cur.fetchone()
            if not result:
                return None
            return json.dumps(result)
    


class User:
    def __init__(self):
        pass
    
    @staticmethod
    async def fetch_user(conn, user_id):
        async with conn.cursor() as cur:
            await cur.execute('SELECT * FROM users WHERE id=%s', (user_id,))
            result = await cur.fetchone()
            if not result:
                return None
            return User(result['id'], result['name'], result['email'])
        
        

    @staticmethod
    async def fetch_all_users(conn):
        async with conn.cursor() as cur:
            await cur.execute('SELECT * FROM User')
            result = await cur.fetchall()
            return [User(r['UserID'], r['FirstName'], r['Email']) for r in result]

    @staticmethod
    async def create_user(conn, name, email):
        async with conn.cursor() as cur:
            await cur.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
            user_id = cur.lastrowid
            return User(user_id, name, email)

    @staticmethod
    async def update_user(conn, user_id, name, email):
        async with conn.cursor() as cur:
            await cur.execute('UPDATE users SET name=%s, email=%s WHERE id=%s', (name, email, user_id))
            return User(user_id, name, email)

    @staticmethod
    async def delete_user(conn, user_id):
        async with conn.cursor() as cur:
            await cur.execute('DELETE FROM users WHERE id=%s', (user_id,))
