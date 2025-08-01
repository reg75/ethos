from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.db import engine, Base
from app.routers.homepage import router as homepage_router
from app.routers.auth_routes import router as auth_router
from app.config import FRONTEND_DIR

def create_app():

   app = FastAPI()

   # EN: Creates database tables / 
   Base.metadata.create_all(bind=engine)
   
   app.include_router(homepage_router)
   app.include_router(auth_router)
   
   app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="static")
   
   return app
