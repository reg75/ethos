from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db import Base

class User(Base):
   __tablename__ = "user"

   id = Column(Integer, primary_key=True)
   school_id = Column(Integer, ForeignKey('school.id'), nullable=False)
   school_obj = relationship("School", backref="users")
   email = Column(String(128), unique=True, nullable=False)
   first_name = Column(String(64)) # Require at front end
   last_name = Column(String(64)) # Require at front end
   job_role_id = Column(Integer, ForeignKey('job_role.id')) # Require at front end
   job_role_obj = relationship("JobRole", backref="users")
   password_hash = Column(String(256), nullable=True)
   email_optin = Column(Boolean, default=False)
   optin_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   is_active = Column(Boolean, default=True)

class JobRole(Base):
   __tablename__ = "job_role"

   id = Column(Integer, primary_key=True)
   name = Column(String(64), unique=True, nullable=False)
   description = Column(String(256))
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)
