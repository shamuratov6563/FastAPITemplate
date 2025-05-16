from fastapi import FastAPI
from app.core.server import Server

fastapi_app = FastAPI(
    title="FastAPI Multi-Tenant Example",
    version="1.0.0"
)

server = Server(fastapi_app)
app = server.get_app()