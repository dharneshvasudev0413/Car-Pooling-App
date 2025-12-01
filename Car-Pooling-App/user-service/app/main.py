#starter template
from fastapi import FastAPI
from app.db import Base, engine
from app.routes.users import router as user_router
from app.routes.auth import router as auth_router

app = FastAPI(title="Secure User Service")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(user_router)
app.include_router(auth_router)

@app.get("/health")
def health():
    return {"status": "user-service OK"}
