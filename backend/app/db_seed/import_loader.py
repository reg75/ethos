import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from app.models.school import School
from app.utils.parsers import parse_none, parse_int_or_none
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
   raise ValueError("DATABASE_URL Not found in environment")

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()


def main():
   # EN: Expects CSV with snake case headers / BR:
   # gov_urn, school_phase_id, name, address_1, address_2, address_3, town_or_city, county, country, postcode, website, telephone,
   # billing_address_1, billing_address_2, billing_address_3, billing_town_or_city, billing_county, billing_country, billing_postcode, billing_telephone

   csv_path = Path(__file__).resolve().parent.parent.parent / "data" / "import" /"school_import_data.csv"

   school_df = pd.read_csv(csv_path)

   # EN: Truncates strings to comply with db constraints
   def truncate(value, max_length):
      val = parse_none(value)
      return val[:max_length] if val else val


   # EN: Prepares school entries for database / BR
   def prepare_school(row):
      return School(
            gov_urn=parse_int_or_none(row.get("gov_urn")),
            name=truncate(row.get("name"), 128),
            school_phase_id=parse_int_or_none(row.get('school_phase_id')),
            
            address_1=truncate(row.get('address_1'), 128),
            address_2=truncate(row.get('address_2'), 128),
            address_3=truncate(row.get('address_3'), 128),
            town_or_city=truncate(row.get('town_or_city'), 64),
            county=truncate(row.get('county'), 64),
            country=truncate(row.get('country'), 32),
            postcode=truncate(row.get('postcode'), 12),
            website=truncate(row.get('website'), 128),
            telephone=truncate(row.get('telephone'), 32),
            
            billing_address_1=truncate(row.get('billing_address_1'), 128),
            billing_address_2=truncate(row.get('billing_address_2'), 128),
            billing_address_3=truncate(row.get('billing_address_3'), 128),
            billing_town_or_city=truncate(row.get('billing_town_or_city'), 64),
            billing_county=truncate(row.get('billing_county'), 64),
            billing_country=truncate(row.get('billing_country'), 32),
            billing_postcode=truncate(row.get('billing_postcode'), 12),
            billing_telephone=truncate(row.get('billing_telephone'), 32),
            
            is_active=True,
            billing_terms_days=30,
            custom_discount_percent=0.0
      )

   schools = [] 
   for _,row in school_df.iterrows():
      school = prepare_school(row)
      schools.append(school)


   try:
      session.add_all(schools)
      session.commit()
   except Exception as e:
      print(f"Error: {e}")
      session.rollback()

if __name__ == "__main__":
   main() 