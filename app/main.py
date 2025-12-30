from datetime import datetime
from fastapi import FastAPI
from app.api.routers.users import router as users_router
from app.api.routers.follows import router as follows_router
from app.api.routers.companies import router as companies_router
from app.api.routers.employments import router as employments_router

app = FastAPI(title="Alumni Backend API")

app.include_router(users_router)
app.include_router(follows_router)
app.include_router(companies_router)
app.include_router(employments_router)


@app.get("/")
def root():
    return {"message": "Alumni Backend API"}


@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
