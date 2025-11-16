from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import api_router

app = FastAPI()

origins = [
    "http://localhost:1234",
    "https://127.0.0.1:1234",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router, prefix="")
