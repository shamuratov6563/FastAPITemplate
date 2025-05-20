from fastapi import APIRouter, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session
from utils.tenants import get_tenant_name
from app.db.session_manager import get_session
from app.models import User

router = APIRouter(
    tags=["User Auth"],
)


class RegisterSchema(BaseModel):
    full_name: str
    username: str
    phone: str | None = None
    role: str


@router.post("/register/")
def register_user(payload: RegisterSchema, request: Request):
    tenant = get_tenant_name(request)
    db: Session = get_session(tenant)

    user = User(
        full_name=payload.full_name,
        username=payload.username,
        phone=payload.phone,
        role=payload.role,
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"msg": "User registered", "user_id": user.id}


@router.get("/test")
async def test_auth():
    return {"msg": "Auth router is working!"}
