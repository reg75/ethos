from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from app.db import Base

    
class Session(Base):
    __tablename__ = "session"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, index=True)
    user_obj = relationship("User", backref="sessions")
    key_hash = Column(String(128), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)   
    last_seen_at = Column(DateTime(timezone=True))
    expires_at = Column(DateTime(timezone=True), nullable=False)
    revoked_at = Column(DateTime(timezone=True))
    ip_first = Column(String(64))
    ip_last = Column(String(64))
    user_agent = Column(String(1024))

    __table_args__ = (
        UniqueConstraint("key_hash", name="uq_session_key_hash"),
        Index("ix_session_expires_at", "expires_at"),
    )
