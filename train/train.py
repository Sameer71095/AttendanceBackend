import math
import os
import os.path
import pickle
from multiprocessing import Pool

import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
from sklearn import neighbors
from PIL import Image
import traceback
import dlib
import numpy as np

def align_face(image, face_locations):
    landmarks = face_recognition.face_landmarks(image, face_locations=face_locations)
    
    # Create a dlib rectangle for each face bounding box
    dlib_rects = [dlib.rectangle(left, top, right, bottom) for (top, right, bottom, left) in face_locations]
    
    # Initialize dlib's shape predictor with a pre-trained model for 5-point facial landmarks
    predictor_path = "shape_predictor_68_face_landmarks.dat"  # Download this file from: http://dlib.net/files/shape_predictor_5_face_landmarks.dat.bz2
    sp = dlib.shape_predictor(predictor_path)
    
    aligned_faces = []
    for i, rect in enumerate(dlib_rects):
        # Get the facial landmarks
        shape = sp(image, rect)

        # Extract the face chip (aligned face image)
        face_chip = dlib.get_face_chip(image, shape)
        aligned_faces.append(face_chip)

    return aligned_faces

def process_image(params):
    print(f"Processing image {params[0]}")  # Add this line
    try:
        img_path, class_dir = params
        image = face_recognition.load_image_file(img_path)
        face_bounding_boxes = face_recognition.face_locations(image)

        if len(face_bounding_boxes) != 1:
            return None, None, None

        aligned_faces = align_face(image, face_bounding_boxes)
        
        if not aligned_faces:
            return None, None, (IndexError(f"No aligned faces found for image {img_path}"), traceback.format_exc())

        return face_recognition.face_encodings(aligned_faces[0])[0], class_dir, None
    except Exception as e:
        return None, None, (e, traceback.format_exc())

    
def train(train_dir, model_save_path=None, n_neighbors=None, knn_algo='ball_tree', verbose=False, update_existing_model=False):
    X = []
    y = []

    # Loop through each person in the training set
    for class_dir in os.listdir(train_dir):
        if not os.path.isdir(os.path.join(train_dir, class_dir)):
            continue

        image_paths = image_files_in_folder(os.path.join(train_dir, class_dir))
        image_params = [(img_path, class_dir) for img_path in image_paths]

        # Parallelize the face encoding process
        with Pool() as pool:
            results = pool.map(process_image, image_params)

        for result in results:
            if result[2] is not None:
                print(f"Error processing image: {result[2][0]}\n{result[2][1]}")
            elif result[0] is not None and result[1] is not None:
                X.append(result[0])
                y.append(result[1])

    if update_existing_model and os.path.isfile(model_save_path):
        with open(model_save_path, 'rb') as f:
            knn_clf, X_existing, y_existing = pickle.load(f)
            X += X_existing
            y += y_existing

    if n_neighbors is None:
        n_neighbors = int(round(math.sqrt(len(X))))
        if verbose:
            print("Chose n_neighbors automatically:", n_neighbors)

    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
    knn_clf.fit(X, y)

    if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump((knn_clf, X, y), f)


    return knn_clf


if __name__ == "__main__":
    _model_path = os.path.dirname(os.path.abspath(__file__)) + '/../model/train_model.clf'
    print("Training KNN classifier...")
    classifier = train("./train", model_save_path=_model_path, n_neighbors=2, verbose=True, update_existing_model=True)
    print("Training complete!")
