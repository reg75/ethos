from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.db import engine, Base
from app.routers.homepage import router
from app.config import FRONTEND_DIR

def create_app():

   app = FastAPI()

   # EN: Creates database tables / 
   Base.metadata.create_all(bind=engine)
   
   app.include_router(router)
   
   app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="static")
   
   return app
