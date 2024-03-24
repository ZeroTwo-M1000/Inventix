from fastapi import FastAPI
from core.config import settings
from routers.api_router import api_router


def init_app() -> FastAPI:
    app = FastAPI()

    async def on_startup() -> None:
        await settings.prisma_connection.connect()

    async def on_shutdown() -> None:
        await settings.prisma_connection.disconnect()

    app.add_event_handler("startup", on_startup)
    app.add_event_handler("shutdown", on_shutdown)

    app.include_router(api_router)

    return app


app = init_app()
