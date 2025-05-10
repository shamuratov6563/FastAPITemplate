from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Time, Date, DateTime, func, Enum
from sqlalchemy.orm import relationship
from app.db import Base


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())



class Branch(BaseModel):
    __tablename__ = "branch"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    users = relationship("UserBranch", back_populates="branch_obj")



class Activity(BaseModel):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    image = Column(String)  
    duration = Column(String)
    description = Column(Text)

    groups = relationship("Group", back_populates="activity_obj")


class Role(BaseModel):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)

    users = relationship("UserRole", back_populates="role_obj")


class User(BaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    role = Column(String, nullable=False)  
    is_active = Column(Boolean, default=False)


    branches = relationship("UserBranch", back_populates="user_obj")
    roles = relationship("UserRole", back_populates="user_obj")
    description = relationship("UserDescription", back_populates="user", uselist=False)
    user_groups = relationship("UserGroup", back_populates="user")

class UserBranch(BaseModel):
    __tablename__ = "user_branch"

    id = Column(Integer, primary_key=True, index=True)
    user_id  = Column(Integer, ForeignKey('user.id'))
    branch_id  = Column(Integer, ForeignKey('branch.id'))
    is_active = Column(Boolean, default=True)

    user_obj = relationship("User", back_populates="branches")  
    branch_obj = relationship("Branch", back_populates="users")  



class UserRole(BaseModel):
    __tablename__ = "user_role" 
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    role_id = Column(Integer, ForeignKey('role.id'))
    
    user_obj = relationship("User", back_populates="roles")
    role_obj = relationship("Role", back_populates="users")


class UserDescription(BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    description = Column(String)
    
    user = relationship("User", back_populates="description")



class Group(BaseModel):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    activity_id = Column(Integer, ForeignKey('activity.id'))
    branch_id = Column(Integer, ForeignKey('branch.id'))
    starts_at = Column(Time)
    is_active = Column(Boolean, default=True)

    activity_obj = relationship("Activity", back_populates="groups")
    branch_obj = relationship("Branch")
    working_days = relationship("WorkingDay", back_populates="group")
    user_groups = relationship("UserGroup", back_populates="group")
  


class WorkingDay(BaseModel):
    __tablename__ = "working_day"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey('group.id'))
    day_of_week = Column(String)  
    start_date = Column(Date)
    is_active = Column(Boolean, default=True)

    group = relationship("Group", back_populates="working_days")


class Attendance(BaseModel):
    __tablename__ = "attendances"


    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey('user.id'))
    user_group_id = Column(Integer, ForeignKey('user_group.id'))
    date = Column(Date)
    group_id = Column(Integer, ForeignKey('group.id'))
    is_available = Column(Boolean, default=False)
    
    user_groups = relationship("UserGroup",back_populates="attendance")
   


class StatusChoices(Enum):
    ACTIVE = "ACTIVE"
    ARXIV = "ARXIV"


class UserGroup(BaseModel):
    __tablename__ = "user_group"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), default=StatusChoices.ACTIVE)
    added_date = Column(DateTime, nullable=False) 
    user_id = Column(Integer, ForeignKey('user.id'))
    group_id = Column(Integer, ForeignKey("group.id"))

    user = relationship("User", back_populates="user_groups")
    group = relationship("Group", back_populates="user_groups")
    attendance = relationship("Attendance",back_populates="user_groups")



class TicketMessage(BaseModel):
    __tablename__ = "ticket_message"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey('ticket.id'), nullable=False)
    sender_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    admin_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    message = Column(Text, nullable=True)
    file = Column(String, nullable=True)  # file yo‘li yoki fayl nomi

    ticket = relationship("Ticket", back_populates="messages")
    sender = relationship("User", foreign_keys=[sender_id])
    admin = relationship("User", foreign_keys=[admin_id])




class TicketStatusEnum(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    IN_PROGRESS = "IN_PROGRESS"


class Ticket(BaseModel):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    branch_id = Column(Integer, ForeignKey('branch.id'), nullable=False)
    status = Column(String(50), default=TicketStatusEnum.OPEN)

    branch = relationship("Branch")
    messages = relationship("TicketMessage", back_populates="ticket", cascade="all, delete-orphan")



    