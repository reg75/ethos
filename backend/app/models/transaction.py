from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db import Base

# EN: Creates transaction table / BR: 
class Transaction(Base):
   __tablename__ = "transaction"

   id = Column(Integer, primary_key=True)
   invoice_id = Column(Integer, ForeignKey('invoice.id'), nullable=False)
   invoice_obj = relationship("Invoice", backref="transactions")
   payment_date = Column(Date, nullable=False, index=True)
   payment_method_id = Column(Integer, ForeignKey('payment_method.id'), nullable=False)
   payment_method_obj = relationship("PaymentMethod", backref="transactions")
   external_payment_id = Column(String(64))
   transaction_status_id = Column(Integer, ForeignKey('transaction_status.id'), nullable=False)
   transaction_status_obj = relationship("TransactionStatus", backref="transactions")
   created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

# EN: Creates transaction_status table / BR:
class TransactionStatus(Base):
   __tablename__ = "transaction_status"
   
   id = Column(Integer, primary_key=True)
   name = Column(String(64), unique=True, nullable=False)
   description = Column(String(256))
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)

# EN: Creates payment_method table / BR:
class PaymentMethod(Base):
   __tablename__ = "payment_method"
   
   id = Column(Integer, primary_key=True)
   name = Column(String(64), unique=True, nullable=False)
   description = Column(String(256))
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)