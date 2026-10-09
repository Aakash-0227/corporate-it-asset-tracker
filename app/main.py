
from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routers import auth_routes, asset_routes


# Create database tables
Base.metadata.create_all(bind=engine)


# Initialize FastAPI application
app = FastAPI(
    title="Corporate IT Asset Tracker API",
    description=(
        "A secure IT asset management API with JWT authentication, "
        "user registration, and CRUD operations."
    ),
    version="1.0.0",
)


# Register API routers
app.include_router(auth_routes.router)
app.include_router(asset_routes.router)


@app.get("/", tags=["Home"])
def home():
    return {
        "message": "Corporate IT Asset Tracker API is running",
        "docs": "/docs",
    }
