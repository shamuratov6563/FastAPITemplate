from fastapi import FastAPI
from sqladmin import Admin
from app.admin.auth import authentication_backend
from app.db.database import db_helper


def setup_admin(app: FastAPI):
    admin = Admin(app=app, engine=db_helper.engine, authentication_backend=authentication_backend)
    # Add your ModelViews here
    # admin.add_view(SomeModelView)
    # admin.add_view(AnotherModelView)
