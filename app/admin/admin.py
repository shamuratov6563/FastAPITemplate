from fastapi import FastAPI
from sqladmin import Admin
from app.admin.auth import authentication_backend
from app.db.database import db_helper
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



from app.admin.sqladmin import (
    UserAdmin,
    BranchAdmin,
    RoleAdmin,
    ActivityAdmin,
    GroupAdmin,
    UserBranchAdmin,
    UserRoleAdmin,
    UserDescriptionAdmin,
    AttendanceAdmin,
    WorkingDayAdmin,
)


def setup_admin(app: FastAPI):
    admin = Admin(app=app, engine=db_helper.engine, authentication_backend=authentication_backend)

    admin.add_view(UserAdmin)
    admin.add_view(BranchAdmin)
    admin.add_view(RoleAdmin)
    admin.add_view(ActivityAdmin)
    admin.add_view(GroupAdmin)
    admin.add_view(UserBranchAdmin)
    admin.add_view(UserRoleAdmin)
    admin.add_view(UserDescriptionAdmin)
    admin.add_view(AttendanceAdmin)
    admin.add_view(WorkingDayAdmin)