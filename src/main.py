from fastapi import FastAPI


def init_app() -> FastAPI:
    app = FastAPI()
    return app


app = init_app()
