# utils/tenants.py
from fastapi import Request

def get_tenant_name(request: Request) -> str:
    host = request.headers.get("host", "")
    parts = host.split(".")
    if len(parts) > 2:
        return parts[0]  # subdomain = tenant name
    return "default"
