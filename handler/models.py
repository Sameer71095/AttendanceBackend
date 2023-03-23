# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, DateTime, Float, ForeignKey, Integer, LargeBinary, String, Text, Time
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Department(Base):
    __tablename__ = 'Department'

    DepartmentID = Column(Integer, primary_key=True)
    DepartmentName = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)
    def to_dict(self):
        return {
            'DepartmentID': self.DepartmentID,
            'DepartmentName': self.DepartmentName,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate.isoformat() if self.CreatedDate else None,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate.isoformat() if self.UpdatedDate else None,
            'UpdatedBy': self.UpdatedBy,
        }


class HolidayType(Base):
    __tablename__ = 'HolidayType'

    HolidayTypeID = Column(Integer, primary_key=True)
    HolidayTypeName = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)
    
    def to_dict(self):
        return {
            'HolidayTypeID': self.HolidayTypeID,
            'HolidayTypeName': self.HolidayTypeName,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate.isoformat() if self.CreatedDate else None,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate.isoformat() if self.UpdatedDate else None,
            'UpdatedBy': self.UpdatedBy,
        }


class PaymentMethod(Base):
    __tablename__ = 'PaymentMethod'

    PaymentMethodID = Column(Integer, primary_key=True)
    PaymentMethodName = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)
    
    def to_dict(self):
        return {
            'PaymentMethodID': self.PaymentMethodID,
            'PaymentMethodName': self.PaymentMethodName,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate.isoformat() if self.CreatedDate else None,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate.isoformat() if self.UpdatedDate else None,
            'UpdatedBy': self.UpdatedBy,
        }
        


class PaymentStatu(Base):
    __tablename__ = 'PaymentStatus'

    PaymentStatusID = Column(Integer, primary_key=True)
    PaymentStatusName = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)
    
    def to_dict(self):
        return {
            'PaymentStatusID': self.PaymentStatusID,
            'PaymentStatusName': self.PaymentStatusName,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate,
            'UpdatedBy': self.UpdatedBy,
        }


class SalaryType(Base):
    __tablename__ = 'SalaryType'

    SalaryTypeID = Column(Integer, primary_key=True)
    SalaryTypeName = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)
    
    def to_dict(self):
        return {
            'SalaryTypeID': self.SalaryTypeID,
            'SalaryTypeName': self.SalaryTypeName,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate,
            'UpdatedBy': self.UpdatedBy,
        }


class SettingType(Base):
    __tablename__ = 'SettingType'

    SettingTypeID = Column(Integer, primary_key=True)
    SettingType = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)
    
    def to_dict(self):
        return {
            'SettingTypeID': self.SettingTypeID,
            'SettingType': self.SettingType,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate,
            'UpdatedBy': self.UpdatedBy,
        }


class SubscriptionType(Base):
    __tablename__ = 'SubscriptionType'

    SubscriptionTypeID = Column(Integer, primary_key=True)
    SubscriptionTypeName = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)

    def to_dict(self):
        return {
            'SubscriptionTypeID': self.SubscriptionTypeID,
            'SubscriptionTypeName': self.SubscriptionTypeName,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate,
            'UpdatedBy': self.UpdatedBy,
        }

class UserType(Base):
    __tablename__ = 'UserType'

    UserTypeID = Column(Integer, primary_key=True)
    UserType = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)

    def to_dict(self):
        return {
            'UserTypeID': self.UserTypeID,
            'UserType': self.UserType,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate,
            'UpdatedBy': self.UpdatedBy,
        }
        

class VacationType(Base):
    __tablename__ = 'VacationType'

    VacationTypeID = Column(Integer, primary_key=True)
    VacationTypeName = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)
    
    def to_dict(self):
        return {
            'VacationTypeID': self.VacationTypeID,
            'VacationTypeName': self.VacationTypeName,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate,
            'UpdatedBy': self.UpdatedBy,
        }


class User(Base):
    __tablename__ = 'User'

    UserID = Column(Integer, primary_key=True)
    FirstName = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    LastName = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    Email = Column(String(255, 'utf8mb4_general_ci'), nullable=False, unique=True)
    Password = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    PhoneNumber = Column(String(20, 'utf8mb4_general_ci'))
    UserTypeID = Column(ForeignKey('UserType.UserTypeID'), index=True)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)
    Token = Column(String(255, 'utf8mb4_general_ci'))

    UserType = relationship('UserType')
    
    def to_dict(self):
        return {
            'UserID': self.UserID,
            'FirstName': self.FirstName,
            'LastName': self.LastName,
            'Email': self.Email,
            'Password': self.Password,
            'PhoneNumber': self.PhoneNumber,
            'UserTypeID': self.UserTypeID,
            'UserType': self.UserType.to_dict(),
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate,
            'UpdatedBy': self.UpdatedBy,
            'Token': self.Token,
        }


class Employer(Base):
    __tablename__ = 'Employer'

    EmployerID = Column(Integer, primary_key=True)
    Name = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    Email = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    PhoneNumber = Column(String(20, 'utf8mb4_general_ci'))
    Password = Column(String(255, 'utf8mb4_general_ci'))
    Token = Column(String(255, 'utf8mb4_general_ci'))
    Address = Column(String(255, 'utf8mb4_general_ci'))
    City = Column(String(255, 'utf8mb4_general_ci'))
    State = Column(String(255, 'utf8mb4_general_ci'))
    Country = Column(String(255, 'utf8mb4_general_ci'))
    PostalCode = Column(String(20, 'utf8mb4_general_ci'))
    IndustryType = Column(String(255, 'utf8mb4_general_ci'))
    WebsiteURL = Column(String(255, 'utf8mb4_general_ci'))
    LogoImage = Column(LargeBinary)
    CompanySize = Column(Integer)
    TaxID = Column(String(255, 'utf8mb4_general_ci'))
    UserId = Column(ForeignKey('User.UserID'), index=True)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)

    User = relationship('User')
    def to_dict(self):
        return {
            "EmployerID": self.EmployerID,
            "Name": self.Name,
            "Email": self.Email,
            "PhoneNumber": self.PhoneNumber,
            "Password": self.Password,
            "Token": self.Token,
            "Address": self.Address,
            "City": self.City,
            "State": self.State,
            "Country": self.Country,
            "PostalCode": self.PostalCode,
            "IndustryType": self.IndustryType,
            "WebsiteURL": self.WebsiteURL,
            "LogoImage": self.LogoImage,
            "CompanySize": self.CompanySize,
            "TaxID": self.TaxID,
            "UserId": self.UserId,
            "IsActive": self.IsActive,
            "IsDeleted": self.IsDeleted,
            "CreatedDate": self.CreatedDate,
            "CreatedBy": self.CreatedBy,
            "UpdatedDate": self.UpdatedDate,
            "UpdatedBy": self.UpdatedBy
        }



class AppSetting(Base):
    __tablename__ = 'AppSettings'

    SettingID = Column(Integer, primary_key=True)
    EmployerID = Column(ForeignKey('Employer.EmployerID'), nullable=False, index=True)
    Description = Column(String(255, 'utf8mb4_general_ci'))
    SettingName = Column(String(255, 'utf8mb4_general_ci'))
    SettingValue = Column(String(255, 'utf8mb4_general_ci'))
    IsEnabled = Column(BIT(1))
    SettingTypeID = Column(ForeignKey('SettingType.SettingTypeID'), index=True)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)

    Employer = relationship('Employer')
    SettingType = relationship('SettingType')

    def to_dict(self):
        return {
            'SettingID': self.SettingID,
            'EmployerID': self.EmployerID,
            'Description': self.Description,
            'SettingName': self.SettingName,
            'SettingValue': self.SettingValue,
            'IsEnabled': self.IsEnabled,
            'SettingTypeID': self.SettingTypeID,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate,
            'UpdatedBy': self.UpdatedBy
        }


class Employee(Base):
    __tablename__ = 'Employee'

    EmployeeID = Column(Integer, primary_key=True)
    EmployerID = Column(ForeignKey('Employer.EmployerID'), nullable=False, index=True)
    Name = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    Email = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    Password = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    PhoneNumber = Column(String(20, 'utf8mb4_general_ci'))
    JobTitle = Column(String(255, 'utf8mb4_general_ci'))
    DepartmentId = Column(ForeignKey('Department.DepartmentID'), index=True)
    ProfileImage = Column(LargeBinary)
    MaxLateTimeinMins = Column(Integer)
    DateOfBirth = Column(Date)
    Address = Column(String(255, 'utf8mb4_general_ci'))
    Gender = Column(String(255, 'utf8mb4_general_ci'))
    UniqueId = Column(String(255))
    WeekendDays = Column(String(255))
    IsLocationBound = Column(BIT(1))
    WorkdayStartTime = Column(Time)
    WorkdayEndTime = Column(Time)
    IsImagesRegistered = Column(BIT(1))
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)
    Token = Column(String(255, 'utf8mb4_general_ci'))
    FCMToken = Column(String(255, 'utf8mb4_general_ci'))

    Department = relationship('Department')
    Employer = relationship('Employer')
    

    def to_dict(self):
        return {
            'EmployeeID': self.EmployeeID,
            'EmployerID': self.EmployerID,
            'Name': self.Name,
            'Email': self.Email,
            'Password': self.Password,
            'PhoneNumber': self.PhoneNumber,
            'JobTitle': self.JobTitle,
            'DepartmentId': self.DepartmentId,
            'ProfileImage': self.ProfileImage,
            'MaxLateTimeinMins': self.MaxLateTimeinMins,
            'DateOfBirth': self.DateOfBirth,
            'Address': self.Address,
            'Gender': self.Gender,            
            'UniqueId': self.UniqueId,
            'WeekendDays': self.WeekendDays,
            'IsLocationBound': self.IsLocationBound,
            'WorkdayStartTime': self.WorkdayStartTime,
            'WorkdayEndTime': self.WorkdayEndTime,
            'IsImagesRegistered': self.IsImagesRegistered,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate,
            'UpdatedBy': self.UpdatedBy,
            'Token': self.Token,
            'FCMToken': self.FCMToken
        }
        



class Location(Base):
    __tablename__ = 'Location'

    LocationID = Column(Integer, primary_key=True)
    EmployerID = Column(ForeignKey('Employer.EmployerID'), nullable=False, index=True)
    NAME = Column(String(255, 'utf8mb4_general_ci'))
    DESCRIPTION = Column(String(255, 'utf8mb4_general_ci'))
    Latitude = Column(Float)
    Longitude = Column(Float)
    Location = Column(String(255, 'utf8mb4_general_ci'))
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)

    Employer = relationship('Employer')

    def to_dict(self):
        return {
            'LocationID': self.LocationID,
            'EmployerID': self.EmployerID,
            'NAME': self.NAME,
            'DESCRIPTION': self.DESCRIPTION,
            'Latitude': self.Latitude,
            'Longitude': self.Longitude,
            'Location': self.Location,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate,
            'UpdatedBy': self.UpdatedBy
        }
        

class Memo(Base):
    __tablename__ = 'Memo'

    MemoID = Column(Integer, primary_key=True)
    EmployerID = Column(ForeignKey('Employer.EmployerID'), nullable=False, index=True)
    Title = Column(Text(collation='utf8mb4_general_ci'), nullable=False)
    Body = Column(Text(collation='utf8mb4_general_ci'), nullable=False)
    ReminderDate = Column(Date)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)

    Employer = relationship('Employer')

    def to_dict(self):
        return {
            'MemoID': self.MemoID,
            'EmployerID': self.EmployerID,
            'Title': self.Title,
            'Body': self.Body,
            'ReminderDate': self.ReminderDate,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate,
            'UpdatedBy': self.UpdatedBy
        }

class Subscription(Base):
    __tablename__ = 'Subscription'

    SubscriptionID = Column(Integer, primary_key=True)
    EmployerID = Column(ForeignKey('Employer.EmployerID'), nullable=False, index=True)
    SubscriptionTypeId = Column(ForeignKey('SubscriptionType.SubscriptionTypeID'), nullable=False, index=True)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)
    SubscriptionStatus = Column(Integer)
    RenewalDate = Column(DateTime)
    Amount = Column(DECIMAL(10, 2))
    PaymentDate = Column(Date)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)

    Employer = relationship('Employer')
    SubscriptionType = relationship('SubscriptionType')

    def to_dict(self):
        return {
            'SubscriptionID': self.SubscriptionID,
            'EmployerID': self.EmployerID_id,
            'SubscriptionTypeId': self.SubscriptionTypeId_id,
            'StartDate': str(self.StartDate),
            'EndDate': str(self.EndDate),
            'SubscriptionStatus': self.SubscriptionStatus,
            'RenewalDate': str(self.RenewalDate) if self.RenewalDate else None,
            'Amount': float(self.Amount),
            'PaymentDate': str(self.PaymentDate) if self.PaymentDate else None,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': str(self.CreatedDate),
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': str(self.UpdatedDate),
            'UpdatedBy': self.UpdatedBy
        }


class Holiday(Base):
    __tablename__ = 'Holiday'

    HolidayID = Column(Integer, primary_key=True)
    EmployeeID = Column(ForeignKey('Employee.EmployeeID'), nullable=False, index=True)
    Description = Column(String(255, 'utf8mb4_general_ci'))
    HolidayDate = Column(Date)
    HolidayDay = Column(Integer)
    Year = Column(Integer, nullable=False)
    IsRecurring = Column(BIT(1), nullable=False)
    IsSpecialHoliday = Column(BIT(1))
    IsNotificationRequired = Column(BIT(1))
    Location = Column(String(255, 'utf8mb4_general_ci'))
    HolidayTypeId = Column(ForeignKey('HolidayType.HolidayTypeID'), index=True)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)

    Employee = relationship('Employee')
    HolidayType = relationship('HolidayType')

    def to_dict(self):
        return {
            'HolidayID': self.HolidayID,
            'EmployeeID': self.EmployeeID,
            'Description': self.Description,
            'HolidayDate': self.HolidayDate,
            'HolidayDay': self.HolidayDay,
            'Year': self.Year,
            'IsRecurring': self.IsRecurring,
            'IsSpecialHoliday': self.IsSpecialHoliday,
            'IsNotificationRequired': self.IsNotificationRequired,
            'Location': self.Location,
            'HolidayTypeId': self.HolidayTypeId,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate,
            'UpdatedBy': self.UpdatedBy,
        }
        

class Payment(Base):
    __tablename__ = 'Payment'

    PaymentID = Column(Integer, primary_key=True)
    SubscriptionID = Column(ForeignKey('Subscription.SubscriptionID'), nullable=False, index=True)
    Amount = Column(DECIMAL(10, 2), nullable=False)
    PaymentDate = Column(Date, nullable=False)
    TransactionId = Column(String(255, 'utf8mb4_general_ci'))
    ReferenceNumber = Column(String(255, 'utf8mb4_general_ci'))
    PaymentMethodId = Column(ForeignKey('PaymentMethod.PaymentMethodID'), index=True)
    PaymentStatusId = Column(ForeignKey('PaymentStatus.PaymentStatusID'), index=True)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)

    PaymentMethod = relationship('PaymentMethod')
    PaymentStatu = relationship('PaymentStatu')
    Subscription = relationship('Subscription')

    def to_dict(self):
        return {
            'PaymentID': self.PaymentID,
            'SubscriptionID': self.SubscriptionID,
            'Amount': self.Amount,
            'PaymentDate': self.PaymentDate,
            'TransactionId': self.TransactionId,
            'ReferenceNumber': self.ReferenceNumber,
            'PaymentMethodId': self.PaymentMethodId,
            'PaymentStatusId': self.PaymentStatusId,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate,
            'UpdatedBy': self.UpdatedBy,
        }
        

class Salary(Base):
    __tablename__ = 'Salary'

    SalaryID = Column(Integer, primary_key=True)
    EmployeeID = Column(ForeignKey('Employee.EmployeeID'), nullable=False, index=True)
    CurrencyType = Column(String(255, 'utf8mb4_general_ci'))
    Amount = Column(DECIMAL(10, 2))
    SalaryTypeId = Column(ForeignKey('SalaryType.SalaryTypeID'), index=True)
    IsOverTimeAllowed = Column(BIT(1))
    PaymentType = Column(Integer)
    EffectiveDate = Column(Date)
    MaxMonthlyOvertime = Column(Integer)
    MaxDailyOvertime = Column(Integer)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)

    Employee = relationship('Employee')
    SalaryType = relationship('SalaryType')

    def to_dict(self):
        return {
            'SalaryID': self.SalaryID,
            'EmployeeID': self.EmployeeID,
            'CurrencyType': self.CurrencyType,
            'Amount': self.Amount,
            'SalaryTypeId': self.SalaryTypeId,
            'IsOverTimeAllowed': self.IsOverTimeAllowed,
            'PaymentType': self.PaymentType,
            'EffectiveDate': self.EffectiveDate,
            'MaxMonthlyOvertime': self.MaxMonthlyOvertime,
            'MaxDailyOvertime': self.MaxDailyOvertime,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate,
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate,
            'UpdatedBy': self.UpdatedBy,
        }



class Schedule(Base):
    __tablename__ = 'Schedule'

    ScheduleID = Column(Integer, primary_key=True)
    EmployeeID = Column(ForeignKey('Employee.EmployeeID'), nullable=False, index=True)
    DayOfWeek = Column(String(15, 'utf8mb4_general_ci'))
    CheckInTime = Column(Time)
    CheckOutTime = Column(Time)
    Latitude = Column(Float)
    Longitude = Column(Float)
    Location = Column(String(255, 'utf8mb4_general_ci'))
    LocationID = Column(ForeignKey('Location.LocationID'), index=True)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)

    Employee = relationship('Employee')
    Location1 = relationship('Location')

    def to_dict(self):
        return {
            'schedule_id': self.schedule_id,
            'employee_id': self.employee.id,
            'day_of_week': self.day_of_week,
            'check_in_time': str(self.check_in_time) if self.check_in_time else None,
            'check_out_time': str(self.check_out_time) if self.check_out_time else None,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'location': self.location,
            'location_id': self.location_id.id if self.location_id else None,
            'is_active': self.is_active,
            'is_deleted': self.is_deleted,
            'created_date': self.created_date,
            'created_by': self.created_by,
            'updated_date': self.updated_date,
            'updated_by': self.updated_by
        }


class Vacation(Base):
    __tablename__ = 'Vacation'

    VacationID = Column(Integer, primary_key=True)
    EmployeeID = Column(ForeignKey('Employee.EmployeeID'), index=True)
    StartDate = Column(Date)
    EndDate = Column(Date)
    EmployerID = Column(ForeignKey('Employer.EmployerID'), index=True)
    Reason = Column(String(255, 'utf8mb4_general_ci'))
    IsPaid = Column(BIT(1))
    RequestedDate = Column(Date)
    ApprovalDate = Column(Date)
    IsApproved = Column(BIT(1))
    Location = Column(String(255, 'utf8mb4_general_ci'), nullable=False)
    VacationTypeId = Column(ForeignKey('VacationType.VacationTypeID'), index=True)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)

    Employee = relationship('Employee')
    Employer = relationship('Employer')
    VacationType = relationship('VacationType')

    def to_dict(self):
        return {
            'vacation_id': self.vacation_id,
            'employee_id': self.employee.id if self.employee else None,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'employer_id': self.employer.id if self.employer else None,
            'reason': self.reason,
            'is_paid': self.is_paid,
            'requested_date': str(self.requested_date),
            'approval_date': str(self.approval_date) if self.approval_date else None,
            'is_approved': self.is_approved,
            'location': self.location,
            'vacation_type_id': self.vacation_type.id,
            'is_active': self.is_active,
            'is_deleted': self.is_deleted,
            'created_date': self.created_date,
            'created_by': self.created_by,
            'updated_date': self.updated_date,
            'updated_by': self.updated_by
        }

class Attendance(Base):
    __tablename__ = 'Attendance'

    AttendanceID = Column(Integer, primary_key=True)
    EmployeeID = Column(ForeignKey('Employee.EmployeeID'), nullable=False, index=True)
    CheckedTime = Column(DateTime)
    CheckedDate = Column(Date)
    Latitude = Column(Float)
    Longitude = Column(Float)
    Location = Column(String(255, 'utf8mb4_general_ci'))
    CheckedImage = Column(LargeBinary)
    IsCheckedout = Column(BIT(1))
    IsLate = Column(BIT(1))
    ScheduleID = Column(ForeignKey('Schedule.ScheduleID'), index=True)
    Reason = Column(String(255, 'utf8mb4_general_ci'))
    IsExcused = Column(BIT(1))
    LocationID = Column(ForeignKey('Location.LocationID'), index=True)
    IsActive = Column(BIT(1))
    IsDeleted = Column(BIT(1))
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Integer)
    UpdatedDate = Column(DateTime)
    UpdatedBy = Column(Integer)

    Employee = relationship('Employee')
    Location1 = relationship('Location')
    Schedule = relationship('Schedule')

    def to_dict(self):
        return {
            'AttendanceID': self.AttendanceID,
            'EmployeeID': self.EmployeeID.id,
            'CheckedTime': self.CheckedTime.isoformat(),
            'CheckedDate': self.CheckedDate.isoformat(),
            'Latitude': self.Latitude,
            'Longitude': self.Longitude,
            'Location': self.Location,
            'CheckedImage': self.CheckedImage.hex(),
            'IsCheckedout': self.IsCheckedout,
            'IsLate': self.IsLate,
            'ScheduleID': self.ScheduleID.id,
            'Reason': self.Reason,
            'IsExcused': self.IsExcused,
            'LocationID': self.LocationID.id,
            'IsActive': self.IsActive,
            'IsDeleted': self.IsDeleted,
            'CreatedDate': self.CreatedDate.isoformat(),
            'CreatedBy': self.CreatedBy,
            'UpdatedDate': self.UpdatedDate.isoformat(),
            'UpdatedBy': self.UpdatedBy,
        }