from fastapi import FastAPI
from app.db import engine, Base
from app.routers.root import router

def create_app():

   app = FastAPI()
   Base.metadata.create_all(bind=engine)
   app.include_router(router)
   return app
