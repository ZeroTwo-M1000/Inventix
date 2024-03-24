from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from routers.api_router import api_router


def init_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['http://localhost:5173', 'http://127.0.0.1:5173'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    async def on_startup() -> None:
        await settings.prisma_connection.connect()

    async def on_shutdown() -> None:
        await settings.prisma_connection.disconnect()

    app.add_event_handler("startup", on_startup)
    app.add_event_handler("shutdown", on_shutdown)

    app.include_router(api_router, prefix="/api")

    return app


app = init_app()
