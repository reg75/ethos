from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, DECIMAL, CheckConstraint, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db import Base

# EN: Creates trust table / BR 
class Trust(Base):
   __tablename__ = "trust"

   id = Column(Integer, primary_key=True)
   name = Column(String(128), nullable=False)
   billing_contact_id = Column(Integer, ForeignKey('user.id'))
   billing_contact_obj = relationship("User", backref="billing_trusts")
   billing_email = Column(String(128)) # Use if present
   billing_address_1 = Column(String(128), nullable=False)
   billing_address_2 = Column(String(128))
   billing_address_3 = Column(String(128))
   town_or_city = Column(String(64), nullable=False)
   county_id = Column(Integer, ForeignKey('county.id'))
   county_obj = relationship("County", backref="trusts")
   country = Column(String(32))
   postcode = Column(String(12), nullable=False)
   telephone = Column(String(32), nullable=False)
   website = Column(String(128))
   created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
   is_active = Column(Boolean, default=True)
   notes = Column(Text)
   billing_reference = Column(String(64))
   billing_terms_days = Column(Integer, default=30)
   vat_number = Column(String(32))
   custom_discount_percent = Column(DECIMAL(5,2), default=0.00)

   __table_args__ = (
      CheckConstraint('custom_discount_percent >=0 AND custom_discount_percent <= 100', name='trust_discount_check'),
      UniqueConstraint('name', 'postcode', name="unique_trust_and_postcode")
   )

# EN: Creates county table / BR:
class County(Base):
   __tablename__ = "county"

   id = Column(Integer, primary_key=True)
   name = Column(String(32), unique=True, nullable=False)
   is_active = Column(Boolean, default=True)

