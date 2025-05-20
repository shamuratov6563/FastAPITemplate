from app.core.routes import Routes
from app.api.views.auth import router as auth_router


__routes__ = Routes(routers=(auth_router,))
