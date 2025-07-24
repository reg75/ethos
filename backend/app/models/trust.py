from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, DECIMAL, CheckConstraint, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db import Base

# EN: Creates trust table / BR 
class Trust(Base):
   __tablename__ = "trust"

   id = Column(Integer, primary_key=True)
   name = Column(String(128), nullable=False, index=True)
   address_1 = Column(String(128))
   address_2 = Column(String(128))
   address_3 = Column(String(128))
   town_or_city = Column(String(64))
   county = Column(String(64))
   country = Column(String(32))
   postcode = Column(String(12), index=True)
   telephone = Column(String(32))
   website = Column(String(128))
   billing_contact_id = Column(Integer, ForeignKey('user.id'))
   billing_contact_obj = relationship("User", backref="billing_trusts")
   billing_email = Column(String(128))
   billing_address_1 = Column(String(128))
   billing_address_2 = Column(String(128))
   billing_address_3 = Column(String(128))
   billing_town_or_city = Column(String(64))
   billing_county = Column(String(64))
   billing_country = Column(String(32))
   billing_postcode = Column(String(12))
   billing_telephone = Column(String(32))
   created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
   is_active = Column(Boolean, default=True, index=True)
   notes = Column(Text)
   billing_reference = Column(String(64))
   billing_terms_days = Column(Integer, default=30)
   vat_number = Column(String(32))
   custom_discount_percent = Column(DECIMAL(5,2), default=0.00)

   __table_args__ = (
      CheckConstraint('custom_discount_percent >=0 AND custom_discount_percent <= 100', name='trust_discount_check'),
      UniqueConstraint('name', 'postcode', name="unique_trust_and_postcode")
   )
