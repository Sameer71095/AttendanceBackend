from http import HTTPStatus
import json
import os

from sanic import Blueprint, response
from sanic.config import Config
from sqlalchemy import create_engine

import asyncio
from datetime import datetime

import aiomysql
from handler.services import CustomJSONEncoder, EmployeeClass, EmployerClass, Prediction, Helper, User,EmployerService

from handler.models import  Department, Employee, Employer, Location, SalaryType, UserType, Attendance
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import MultipleResultsFound

services = Blueprint('services')

config = Config()

# Initialize the 'config' attribute for the Blueprint
services.ctx.config = config

# call this api to make sure api is running
@services.get('/api/hello', strict_slashes=True)
async def hello(request):
    return response.json({'status': HTTPStatus.OK, 'message': 'Hello .. '})




# api that handle recognition image
@services.post('/api/recognize', strict_slashes=True)
async def recognize(request):
    if 'image' not in request.files:
        return response.json({'status': HTTPStatus.BAD_REQUEST, 'message': 'image is required'})

    file = request.files.get('image')
    if file.name == '':
        return response.json({'status': HTTPStatus.BAD_REQUEST, 'message': 'image is required name'})

    if not file and not Helper.allowed_file(file.name):
        return response.json({'status': HTTPStatus.BAD_REQUEST, 'message': 'image extension not allowed'})

    knn_model, _, _ = request.app.ctx.train_model

    distance_threshold = request.app.ctx.distance_threshold
    prediction = Prediction(knn_model, distance_threshold)
    # get file extension
    image_extension = file.name.split('.')[1]
    # get file stream
    file_stream = file.body
    results = prediction.predict_image(file_stream, image_extension)
    return response.json({'status': HTTPStatus.OK, 'data': results[0][0]})



# async def connect_db():
#     return await aiomysql.create_pool(
#         host='mysql.fuzixtech.com',
#         port=3306,
#         user='adminsameer',
#         password='m.sameer',
#         db='db_attendancesystem',
#         autocommit=True,
#         cursorclass=aiomysql.DictCursor,
#     )

# @services.listener('before_server_start')
# async def setup_db(app, loop):
#     services.ctx.config.db = await connect_db()

# @services.listener('after_server_stop')
# async def close_db(app, loop):
#     services.ctx.config.db.close()
#     await services.ctx.config.db.wait_closed()

engine = create_engine('mssql+pyodbc://adminsameer:m.sameer@mysql.fuzixtech.com:3306/db_attendancesystem?driver=SQL+Server')
employer_service = EmployerService(engine)

Session = sessionmaker(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

services.ctx.config['DB_SESSION'] = session


@services.get('/api/employers', strict_slashes=True)
async def get_employers(request):
    employers = employer_service.get_employers()
    employers_dict = [employer.to_dict() for employer in employers]
    return response.json(employers_dict)

@services.get('/api/employers/<employer_id>', strict_slashes=True)
async def get_employer_by_id(request, employer_id): 
    # Get a SQLAlchemy session object from the Sanic app
    session = request.app.config['DB_SESSION']

    # Execute the modified query
    employer = session.query(Employer.Name, Employer.Email).filter_by(id=employer_id).first()

    if not employer:
        return response.json({'isSuccess': False,'errorMessage': 'Invalid credentials'}, status=401)
    else:
        return response.json({'isSuccess': True,'errorMessage':'', 'data': json.dumps(employer.to_dict())})
    
    
@services.get('/employers', strict_slashes=True)
async def create_employer(request):
    employer_data = request.json
    employer = employer_service.create_employer(employer_data)
    return json({'employer': employer})
    
    
@services.post('/api/employee/login', strict_slashes=True)
async def loginemployee(request):
    email = request.json.get('email')
    password = request.json.get('password')
    # Validate the request parameters
    if not email or not password:
        return response.json({'message': 'Missing email or password'}, status=400)
    employee= EmployeeClass()
    async with services.ctx.config.db.acquire() as conn:
        employeedata = await employee.login_employee(conn,email,password)
        if not employeedata:
            return response.json({'isSuccess': False,'errorMessage': 'Invalid credentials'}, status=401)
        else:
            return response.json({'isSuccess': True, 'errorMessage': '', 'data': employeedata}, cls=CustomJSONEncoder)
   
   
   
   
@services.post("/api/attendance/checkin", strict_slashes=True)
async def attendance_checkin(request):
    session = Session()
    
    if 'image' not in request.files:
            return response.json({"isSuccess": False, "errorMessage": 'image is required', "data": ""})

    file = request.files.get('image')
    if file.name == '':
        return response.json({"isSuccess": False, "errorMessage": 'image is required name', "data": ""})

    if not file and not Helper.allowed_file(file.name):
        return response.json({"isSuccess": False, "errorMessage": 'image extension not allowed', "data": ""})

    knn_model, _, _ = request.app.ctx.train_model

    distance_threshold = request.app.ctx.distance_threshold
    prediction = Prediction(knn_model, distance_threshold)
    # get file extension
    image_extension = file.name.split('.')[1]
    # get file stream
    file_stream = file.body
    results = prediction.predict_image(file_stream, image_extension)
    recognizecheckedInUserId=results[0][0]

    # Extract request parameters
    employee_id = request.form.get("EmployeeID")
    latitude = request.form.get("Latitude")
    longitude = request.form.get("Longitude")
    location = request.form.get("Location")
    schedule_id = request.form.get("ScheduleID")
    location_id = request.form.get("LocationID")
    checked_image = request.form.get("CheckedImage")

    # Validate request parameters
    # if not employee_id or not latitude or not longitude or not location or not schedule_id or not location_id:
    #     return response.json({"isSuccess": False, "errorMessage": "Missing required parameters.", "data": "Invalid request."})

    try:
        # Get the current date and time
        now = datetime.now()
        checked_date = now.date()
        checked_time = now.time()

        # Create a new Attendance object
        new_attendance = Attendance(
            EmployeeID=recognizecheckedInUserId,
            CheckedTime=checked_time,
            CheckedDate=checked_date,
            Latitude=latitude,
            Longitude=longitude,
            Location=location,
            ScheduleID=schedule_id,
            LocationID=location_id,
            CheckedImage=checked_image,
            IsCheckedout=False,
            CreatedBy=employee_id,
            IsActive=True,
            IsDeleted=False
        )

        # Add the new Attendance object to the session
        session.add(new_attendance)

        # Commit the transaction
        session.commit()

        return response.json({"isSuccess": True, "errorMessage": "", "data": "Attendance successfully checked in."})
    except Exception as e:
        session.rollback()
        return response.json({"isSuccess": False, "errorMessage": str(e), "data": "An error occurred during attendance check-in."})
    finally:
        session.close()
        
        
    
    
@services.post('/api/employer/login', strict_slashes=True)
async def loginemployer(request):
    email = request.json.get('email')
    password = request.json.get('password')
    # Validate the request parameters
    if not email or not password:
        return response.json({'message': 'Missing email or password'}, status=400)
    employer= EmployerClass()
    async with services.ctx.config.db.acquire() as conn:
        employerdata = await employer.login_employer(conn,email,password)
        if not employerdata:
            return response.json({'isSuccess': False,'errorMessage': 'Invalid credentials'}, status=401)
        else:
            return response.json({'isSuccess': True,'errorMessage':'', 'data': employerdata})





@services.post("/api/addemployee", strict_slashes=True)
async def add_employee(request):
    # Replace employer_id with the actual employer_id you want to use
    employer_id = 1

    data = request.json
    employee = Employee(
        EmployerID=employer_id,
        Name=data["name"],
        Email=data["email"],
        Password="default_password",  # You should use a hashed password
        PhoneNumber=data["contact"],
        UniqueId=data["unique_id"],
        WeekendDays=",".join(data["weekend_days"]),
        JobTitle=data["designation"],
        DepartmentId=data["department"],
        IsLocationBound=data["is_location_bound"],
        WorkdayStartTime=data["workday_start"],
        WorkdayEndTime=data["workday_end"],
        IsActive=True,
        IsDeleted=False
    )

    db_session = SessionLocal()
    db_session.add(employee)

    try:
        db_session.commit()
        return response.json({"status": "success", "message": "Employee added successfully", "employee_id": employee.EmployeeID})
    except Exception as e:
        db_session.rollback()




@services.post('/api/users', strict_slashes=True)
async def get_users(request):
    user = User()
    async with services.ctx.config.db.acquire() as conn:
        users = await user.fetch_all_users(conn)
        if len(users) > 0:
          return json({'users': [{'id': u.UserID, 'name': u.FirstName, 'email': u.Email} for u in users]})
        else:
          return response.json({'status': HTTPStatus.OK, 'data': 'No Data Found'})
    

@services.post('/api/createuser', strict_slashes=True)
async def create_user(request):
    data = request.json
    async with services.ctx.config.db.acquire() as conn:
        user = await create_user(conn, data['name'], data['email'])
        return json({'message': 'User created successfully', 'user': {'id': user.id, 'name': user.name, 'email': user.email}})



# Define the API endpoint to get SalaryType
@services.post('/api/getsalarytype', strict_slashes=True)
async def get_salary_type(request):
    session = Session()
    salary_types = session.query(SalaryType.SalaryTypeID, SalaryType.SalaryTypeName).all()
    session.close()
    return response.json({'isSuccess': True,'errorMessage':'', 'data': [{'SalaryTypeID': s[0], 'SalaryTypeName': s[1]} for s in salary_types]})


# Define the API endpoint to get SalaryType
@services.post('/api/getdepartments', strict_slashes=True)
async def get_departments(request):
    session = Session()
    departments = session.query(Department.DepartmentID, Department.DepartmentName).all()
    session.close()
    return response.json({'isSuccess': True,'errorMessage':'', 'data': [{'DepartmentID': s[0], 'DepartmentName': s[1]} for s in departments]})



# Define the API endpoint to get SalaryType
@services.post('/api/getlocations', strict_slashes=True)
async def get_locations(request):
    session = Session()
    locations = session.query(Location.LocationID, Location.NAME).filter(Location.EmployerID==request.json.get('EmployerID')).all()
    session.close()
    return response.json({'isSuccess': True,'errorMessage':'', 'data': [{'LocationID': s[0], 'NAME': s[1]} for s in locations]})


# Define the API endpoint
@services.post('/api/registeremployeeimages', strict_slashes=True)
async def save_images(request):
    # Get the foldername from the request
    foldername = request.form.get('foldername')
    foldername='train\\train\\'+foldername
    # Create the folder if it doesn't exist
    if not os.path.exists(foldername):
        os.makedirs(foldername)

    # Save all the uploaded images to the folder
    for file in request.files.getlist('images'):
        filename = file.name
        with open(os.path.join(foldername, filename), 'wb') as f:
            f.write(file.body)

    db_session = Session()
    employee_id = request.form.get('foldername')
    try:
     employee = db_session.query(Employee).filter(Employee.EmployeeID == employee_id).first()
    except Exception as e:
        db_session.rollback()
        message=str(e)
        return response.json({"status": "failed", "message": str(e)})

    if employee is None:
        return response.json({"status": "failed", "message": "Employee not found"})

    employee.IsImagesRegistered = True

    try:
        db_session.commit()
        return response.json({'status': HTTPStatus.OK,  "message": "Employee Images updated successfully"})
    except Exception as e:
        db_session.rollback()
        return response.json({"status": "failed", "message": "Error updating employee Images"})

    # Return a success message
  #  return response.json({'status': HTTPStatus.OK, 'data': 'images saved succesfully'})

