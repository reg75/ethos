from app.db import engine, Base
import app.models

def main():
   print("Creating database tables...")
   Base.metadata.create_all(bind=engine)
   print("Tables created.")

if __name__ == "__main__":
   main() 
