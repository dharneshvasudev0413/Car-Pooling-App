#starter template
from fastapi import FastAPI
from app.db import Base, engine
from app.routes.user_routes import router as user_router

app = FastAPI(title="User Service")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(user_router)


@app.get("/health")
def health():
    return {"status": "user-service OK"}
