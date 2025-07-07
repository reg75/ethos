from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db import Base

# EN: Creates resource_item table
class ResourceItem(Base):
   __tablename__ = "resource_item"

   id = Column(Integer, primary_key=True)
   name = Column(String(256), nullable=False)
   description = Column(String(256))
   resource_item_format_id = Column(Integer, ForeignKey('resource_item_format.id'), nullable=False)
   resource_item_format_obj = relationship("ResourceItemFormat", backref="resource_items")
   resource_item_type_id = Column(Integer, ForeignKey('resource_item_type.id'), nullable=False)
   resource_item_type_obj = relationship("ResourceItemType", backref="resource_items")
   stage_id = Column(Integer, ForeignKey('stage.id'), nullable=False)
   stage_obj = relationship("Stage", backref="resource_items")
   access_tier_id = Column(Integer, ForeignKey('access_tier.id'), nullable=False)
   access_tier_obj = relationship("AccessTier", backref="resource_items")
   academic_year_id = Column(Integer, ForeignKey('academic_year.id'))
   week_id = Column(Integer, ForeignKey('week.id'))
   file_url = Column(String(512), nullable=False)
   uploaded_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
   updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
   is_active = Column(Boolean, default=True)

# EN: Creates resource_item_type table / BR: 
class ResourceItemType(Base):
   __tablename__ = "resource_item_type"

   id = Column(Integer, primary_key=True)
   name = Column(String(64), nullable=False)
   description = Column(String(256))
   is_active = Column(Boolean, default=True)
   sort_order = Column(Integer, default=0)

# EN: Creates resource_item_format table
class ResourceItemFormat(Base):
   __tablename__ = "resource_item_format"

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


