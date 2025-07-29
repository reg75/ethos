import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
   raise ValueError("DATABASE_URL Not found in environment")

engine = create_engine(DATABASE_URL)

csv_path = Path(__file__).resolve().parent.parent.parent / "data" / "seed" /"payment_method.csv"

payment_method_df = pd.read_csv(csv_path)

try: 
   with engine.connect() as connection:
      with connection.begin():
         payment_method_df.to_sql(
            'payment_method',
            con=connection,
            if_exists='append',
            index=False
         )
   print("Payment methods imported successfully!")
except SQLAlchemyError as e:
   print(f"Database error: {e}")


