from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Time, Date, DateTime, func
from app.db import Base


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())



class Branch(Base):
    __tablename__ = "branch"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    image = Column(String)  
    duration = Column(String)
    description = Column(Text)


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    role = Column(String, nullable=False)  
    is_active = Column(Boolean, default=False)

class UserBranch(Base):
    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey('user.id'))
    branch = Column(Integer, ForeignKey('branch.id'))
    is_active = Column(Boolean, default=True)

class UserRole(Base):
    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey('user.id'))
    role = Column(Integer, ForeignKey('role.id'))

class UserDescription(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    description = Column(String)


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    activity = Column(Integer, ForeignKey('activity.id'))
    branch = Column(Integer, ForeignKey('branch.id'))
    starts_at = Column(Time)
    is_active = Column(Boolean, default=True)



class WorkingDay(Base):
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey('group.id'))
    day_of_week = Column(String)  
    start_date = Column(Date)
    is_active = Column(Boolean, default=True)


class Attendance(Base):
    __tablename__ = "attendances"


    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey('user.id'))
    date = Column(Date)
    group_id = Column(Integer, ForeignKey('group.id'))
    is_available = Column(Boolean, default=False)