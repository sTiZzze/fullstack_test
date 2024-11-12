from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from src.interfaces.auth import router_auth
from src.interfaces.task import router_task

app = FastAPI()

app.include_router(router_auth, prefix="/api/v1", tags=["users"])
app.include_router(router_task, prefix="/api/v1", tags=["tasks"])

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Content-Type", "Authorization"],
)