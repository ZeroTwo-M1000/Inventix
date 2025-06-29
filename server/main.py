from fastapi import FastAPI, Response

from app.config.conf import DATABASE_URL
from fastapi.middleware.cors import CORSMiddleware

print(DATABASE_URL)

app = FastAPI()


@app.get("/health")
def check_health():
    return Response(status_code=200)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
