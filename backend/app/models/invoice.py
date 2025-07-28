from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, ForeignKey, DECIMAL, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db import Base

# EN: Creates invoice table / BR: 
class Invoice(Base):
   __tablename__ = "invoice"

   id = Column(Integer, primary_key=True)
   school_id = Column(Integer, ForeignKey('school.id'), nullable=False)
   school_obj = relationship("School", backref="invoices")
   trust_id = Column(Integer, ForeignKey('trust.id'))
   trust_obj = relationship("Trust", backref="invoices")
   invoice_status_id = Column(Integer, ForeignKey('invoice_status.id'), nullable=False)
   invoice_status_obj = relationship("InvoiceStatus", backref="invoices")
   total_amount = Column(DECIMAL(10,2), nullable=False)
   issue_date = Column(Date, nullable=False) # Day invoice was issued
   billing_terms_days = Column(Integer, nullable=False) # Days until due - Derive from Trust or School billing terms
   due_date = Column(Date, nullable=False, index=True) # Date payment due - Derive from issue date and billing terms
   outstanding = Column(DECIMAL(10,2), nullable=False, default=0)
   created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

# EN: Creates invoice_line_item table / BR:
class InvoiceLineItem(Base):
   __tablename__ = "invoice_line_item"

   id = Column(Integer, primary_key=True)
   invoice_id = Column(Integer, ForeignKey('invoice.id'), nullable=False)
   invoice_obj = relationship("Invoice", backref="invoice_line_items")
   subscription_id = Column(Integer, ForeignKey('subscription.id'), nullable=False)
   subscription_obj = relationship("Subscription", backref="invoice_line_items")
   school_id = Column(Integer, ForeignKey('school.id'), nullable=False)
   school_obj = relationship("School", backref="invoice_line_items")
   price = Column(DECIMAL(10,2), nullable=False)
   code_discount_id = Column(Integer, ForeignKey('discount_code.id'))
   applied_discount_percent = Column(DECIMAL(10,2), default=0) # Applied discount = code discount + Trust/school discount
   amount_due = Column(DECIMAL(10,2), nullable=False)

   __table_args__ = (
      CheckConstraint('applied_discount_percent >=0 AND applied_discount_percent <= 100', name='applied_discount_check'),
   )

# EN: Creates invoice_status table / BR:
class InvoiceStatus(Base):
   __tablename__ = "invoice_status"
   
   id = Column(Integer, primary_key=True)
   name = Column(String(64), unique=True, nullable=False)
   description = Column(String(256))
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)

# EN: Creates discount_code table / BR:
class DiscountCode(Base):
   __tablename__ = "discount_code"
   
   id = Column(Integer, primary_key=True)
   name = Column(String(64), nullable=False)
   description = Column(String(256))
   discount_percent = Column(DECIMAL(5,2), nullable=False)
   valid_from_date = Column(Date, nullable=False)
   valid_to_date = Column(Date, nullable=False)
   created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
   is_active = Column(Boolean, default=True)

   __table_args__ = (
      CheckConstraint('discount_percent >=0 AND discount_percent <= 100', name='discount_check'),
      CheckConstraint('valid_to_date >= valid_from_date', name='date_check'),
      UniqueConstraint('name', 'is_active', name="unique_active_name")
   )