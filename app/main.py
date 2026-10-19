from fastapi import FastAPI

from app.routers.tenant import router as tenant_router

app=FastAPI()

app.include_router(tenant_router)
@app.get("/")
def home():
    return{
        "app running"
    }