from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.admin.admin import setup_admin
from app.core import SETTINGS


async def on_startup() -> None:
    print('The app is working 🎊🎉🎛')


class Server:
    __app: FastAPI

    def __init__(self, app: FastAPI):
        self.__app = app
        self.__register_router(app)
        self.__register_events(app)
        self.__register_middlewares(app)
        self.__register_websocket(app)
        self.__register_admin(app)
        self.__register_media_files(app)
        self.__register_static_files(app)

    def get_app(self):
        return self.__app

    @staticmethod
    def __register_router(app):
        from app.api.router import api_router
        app.include_router(api_router)

    @staticmethod
    def __register_websocket(app):
        pass

    @staticmethod
    def __register_admin(app):
        setup_admin(app)
        return app

    @staticmethod
    def __register_events(app: FastAPI):
        app.on_event('startup')(on_startup)

    @staticmethod
    def __register_middlewares(app: FastAPI):
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    @staticmethod
    def __register_media_files(app: FastAPI):
        app.mount(f'/{SETTINGS.MEDIA_URL}', StaticFiles(directory="media/"), name="media")

    @staticmethod
    def __register_static_files(app: FastAPI):
        app.mount(f'/{SETTINGS.STATIC_URL}', StaticFiles(directory="static"), name="static")
