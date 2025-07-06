from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, DECIMAL, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db import Base

# EN: Creates school table / BR 
class School(Base):
   __tablename__ = "school"

   id = Column(Integer, primary_key=True)
   trust_id = Column(Integer, ForeignKey('trust.id'))
   trust_obj = relationship("Trust", backref="schools")
   school_type_id = Column(Integer, ForeignKey('school_type.id'))
   school_type_obj = relationship("SchoolType", backref="schools")
   name = Column(String(128), nullable=False)
   billing_email = Column(String(128), nullable=False)
   billing_address_1 = Column(String(128), nullable=False)
   billing_address_2 = Column(String(128))
   billing_address_3 = Column(String(128))
   town_city = Column(String(64), nullable=False)
   county_id = Column(Integer, ForeignKey('county.id'))
   county_obj = relationship("County", backref="schools")
   country = Column(String(32))
   postcode = Column(String(12), nullable=False)
   telephone = Column(String(32), nullable=False)
   created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
   is_active = Column(Boolean, default=True)
   main_contact_name = Column(String(128), nullable=False)
   main_contact_email = Column(String(128), nullable=False)
   main_contact_phone = Column(String(32))
   notes = Column(Text)
   billing_reference = Column(String(64))
   billing_terms_days = Column(Integer, default=30)
   vat_number = Column(String(32))
   custom_discount_percent = Column(DECIMAL(5,2), default=0.00)

   __table_args__ = (
   CheckConstraint('custom_discount_percent >=0 AND custom_discount_percent <= 100', name='school_discount_check'),
   UniqueConstraint('name', 'postcode', name="unique_school_and_postcode")
)
   

# EN: Creates school_type table
class SchoolType(Base):
   __tablename__ = "school_type"

   id = Column(Integer, primary_key=True)
   name = Column(String(32), unique=True, nullable=False)
   description = Column(String(256))
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)



   
