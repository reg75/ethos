from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from datetime import datetime, timezone
from app.db import Base

# EN: Creates Trust database table / BR 
class Trust(Base):
   __tablename__ = "trust"

   id = Column(Integer, primary_key=True)
   name = Column(String(128), unique=True, nullable=False)
   billing_email = Column(String(128), nullable=False)
   billing_address_1 = Column(String(128), nullable=False)
   billing_address_2 = Column(String(128))
   billing_address_3 = Column(String(128))
   town_city = Column(String(64), nullable=False)
   county = Column(String(32))
   country = Column(String(32))
   postcode = Column(String(12), nullable=False)
   telephone = Column(String(32), nullable=False)
   created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   is_active = Column(Boolean, default=True)
   main_contact_name = Column(String(128), nullable=False)
   main_contact_email = Column(String(128), nullable=False)
   main_contact_phone = Column(String(32))
   notes = Column(Text)
   billing_reference = Column(String(64))
   billing_terms_days = Column(Integer, default=30)
   vat_number = Column(String(32))
   custom_discount_percent = Column(DECIMAL(5,2))




