from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from decouple import config
from utils.init_db import init_db
from router.api import router 

app = FastAPI(
    debug=True,
    title="FastAPI",
    description="FastAPI",
)

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:5000",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup() -> None:
    """Start the application."""
    init_db()


app.include_router(router)


app.mount("/static", StaticFiles(directory="static"), name="static")
Message = config("MESSAGE")
@app.get("/")
def root():
    return {"Api": Message}
