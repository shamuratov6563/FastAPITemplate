from fastapi import FastAPI
from app.core import Server, SETTINGS
from app.admin.admin import setup_admin

app = FastAPI(
    title=SETTINGS.PROJECT_NAME,
    debug=SETTINGS.DEBUG,
)

# Admin panelni ulaymiz
setup_admin(app)

