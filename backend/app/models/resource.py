from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db import Base

# EN: Creates resource table
class Resource(Base):
   __tablename__ = "resource"

   id = Column(Integer, primary_key=True)
   name = Column(String(256), nullable=False)
   description = Column(String(256))
   resource_format_id = Column(Integer, ForeignKey('resource_format.id'), nullable=False)
   resource_format_obj = relationship("ResourceFormat", backref="resources")
   resource_type_id = Column(Integer, ForeignKey('resource_type.id'), nullable=False)
   resource_type_obj = relationship("ResourceType", backref="resources")
   stage_id = Column(Integer, ForeignKey('stage.id'), nullable=False)
   stage_obj = relationship("Stage", backref="resources")
   access_tier_id = Column(Integer, ForeignKey('access_tier.id'), nullable=False)
   access_tier_obj = relationship("AccessTier", backref="resources")
   academic_year_id = Column(Integer, ForeignKey('academic_year.id'))
   week_id = Column(Integer, ForeignKey('week.id'))
   file_url = Column(String(512), nullable=False)
   uploaded_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
   is_active = Column(Boolean, default=True)

# EN: Creates resource_type table / BR: 
class ResourceType(Base):
   __tablename__ = "resource_type"

   id = Column(Integer, primary_key=True)
   name = Column(String(64), nullable=False)
   description = Column(String(256))
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)

# EN: Creates resource_format table
class ResourceFormat(Base):
   __tablename__ = "resource_format"

   id = Column(Integer, primary_key=True)
   name = Column(String(64), nullable=False)
   description = Column(String(256))
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)

# EN: Creates stage table
class Stage(Base):
   __tablename__ = "stage"

   id = Column(Integer, primary_key=True)
   name = Column(String(64), nullable=False)
   description = Column(String(256))
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)

# EN: Creates academic_year table
class AcademicYear(Base):
   __tablename__ = "academic_year"

   id = Column(Integer, primary_key=True)
   name = Column(String(64), nullable=False)
   description = Column(String(256))
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)

# EN: Creates week table
class Week(Base):
   __tablename__ = "week"

   id = Column(Integer, primary_key=True)
   academic_year_id = Column(Integer, ForeignKey('academic_year.id'), nullable=False)
   academic_year_obj = relationship("AcademicYear", backref="weeks")
   week_number = Column(Integer, nullable=False)
   start_date = Column(Date)
   description = Column(String(256))
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)


