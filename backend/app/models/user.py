import enum
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db import Base

# EN: Creates user table / BR:
class User(Base):
   __tablename__ = "user"

   id = Column(Integer, primary_key=True)
   school_id = Column(Integer, ForeignKey('school.id'), nullable=False)
   school_obj = relationship("School", backref="users", foreign_keys=[school_id])
   email = Column(String(128), unique=True, nullable=False)
   phone_1 = Column(String(32))
   phone_2 = Column(String(32))
   title_id = Column(Integer, ForeignKey('title.id'))
   title_obj = relationship("Title", backref="users")
   first_name = Column(String(64)) # Require at front end
   last_name = Column(String(64)) # Require at front end
   job_role_id = Column(Integer, ForeignKey('job_role.id')) # Require at front end
   job_role_obj = relationship("JobRole", backref="users")
   user_role_id = Column(Integer, ForeignKey('user_role.id'), nullable=False) # Could set to #1 if #1 is basic user
   user_role_obj = relationship("UserRole", backref="users")
   password_hash = Column(String(256), nullable=True)
   email_optin = Column(Boolean, default=False)
   email_optin_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
   is_active = Column(Boolean, default=True)
   is_verified = Column(Boolean, default=False)
   profile_complete = Column(Boolean, default=False)
   last_login = Column(DateTime, default=None)
   is_locked = Column(Boolean, default=False)
   locked_at = Column(DateTime, default=None)
   lock_reason = Column(String(128))

# EN: Creates title table / BR:
class Title(Base):
   __tablename__ = "title"

   id = Column(Integer, primary_key=True)
   name = Column(String(16), unique=True, nullable=False)
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)

# EN: Creates job_role table / BR:
class JobRole(Base):
   __tablename__ = "job_role"

   id = Column(Integer, primary_key=True)
   name = Column(String(64), unique=True, nullable=False)
   description = Column(String(256))
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)

# EN: Creates user_role table / BR:
class UserRole(Base):
   __tablename__ = "user_role"

   id = Column(Integer, primary_key=True)
   name = Column(String(64), unique=True, nullable=False)
   description = Column(String(256))
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)

# EN: Creates token table / BR:
class TokenPurposeEnum(enum.Enum):
   CONFIRM_EMAIL = "confirm_email"
   FINISH_REGISTRATION = "finish_registration"
   PASSWORD_RESET = "password_reset"

class Token(Base):
   __tablename__ = "token"

   id = Column(Integer, primary_key=True)
   user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
   user_obj = relationship("User", backref="tokens")
   token = Column(String(128), unique=True, nullable=False)
   purpose = Column(SQLEnum(TokenPurposeEnum), nullable=False)
   created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   expires_at = Column(DateTime, nullable=False)
   used = Column(Boolean, default=False)

# EN: Creates user_login_attempt table / BR:
class UserLoginAttempt(Base):
   __tablename__ = "user_login_attempt"

   id = Column(Integer, primary_key=True)
   user_id = Column(Integer, ForeignKey('user.id'), nullable=False, index=True)
   user_obj = relationship("User", backref="login_attempts")
   attempt_time = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   success = Column(Boolean, nullable=False)
   ip_address = Column(String(64))
   user_agent = Column(String(512))
