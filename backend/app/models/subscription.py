from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db import Base

# EN: Creates subscription table
class Subscription(Base):
   __tablename__ = "subscription"

   id = Column(Integer, primary_key=True)
   school_id = Column(Integer, ForeignKey('school.id'), nullable=False)
   school_obj = relationship("School", backref="subscriptions")
   access_tier_id = Column(Integer, ForeignKey('access_tier.id'), nullable=False)
   access_tier_obj = relationship("AccessTier", backref="subscriptions")
   subscription_status_id = Column(Integer, ForeignKey('subscription_status.id'), nullable=False)
   subscription_status_obj = relationship("SubscriptionStatus", backref="subscriptions")
   start_date = Column(DateTime, nullable=False)
   end_date = Column(DateTime, nullable=False)
   auto_renew = Column(Boolean, default=False)
   created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   is_active = Column(Boolean, default=True)

# EN: Creates subscription_status table
class SubscriptionStatus(Base):
   __tablename__ = "subscription_status"

   id = Column(Integer, primary_key=True)
   name = Column(String(32), unique=True, nullable=False)
   description = Column(String(256))
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)

# EN: Creates access_tier table
class AccessTier(Base):

   __tablename__ = "access_tier"

   id = Column(Integer, primary_key=True)
   name = Column(String(32), unique=True, nullable=False)
   description = Column(String(256))
   price = Column(DECIMAL(10,2))
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)
