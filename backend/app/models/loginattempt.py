from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Index, func
from sqlalchemy.orm import relationship

# EN: Creates user_login_attempt table / BR:
class UserLoginAttempt(Base):
   __tablename__ = "user_login_attempt"

   id = Column(Integer, primary_key=True)
   user_id = Column(Integer, ForeignKey('user.id'), nullable=True, index=True)
   user_obj = relationship("User", backref="login_attempts")
   attempt_time = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
   success = Column(Boolean, nullable=False)
   email_entered = Column(String(320), nullable=False)
   reason = Column(String(32), nullable=True)
   ip_address = Column(String(64))
   user_agent = Column(String(1024))
   
   __table_args__ = (
    Index("ix_attempt_user_time", "user_id", "attempt_time"),
    Index("ix_attempt_email_time", "email_entered", "attempt_time"),
    Index("ix_attempt_ip_time", "ip_address", "attempt_time"),
)