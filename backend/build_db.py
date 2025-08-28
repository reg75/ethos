from sqlalchemy import text
from app.db import engine, Base
import app.models

import create_db

from app.db_seed import (
    import_loader,
    seed_academic_year,
    seed_access_tier,
    seed_job_role,
    seed_payment_method,
    seed_resource_item_format,
    seed_resource_phase,
    seed_school_phase,
    seed_title,
    seed_transaction_status,
    seed_user_role,
    seed_week,
    )

def build_database():
    """EN: Build the dev database schema and insert seed data.
    BR: Cria o esquema do banco de dados e insere dados de seed."""
    print("===| Nuking public schema (dev only) |===")
    with engine.begin() as conn:
        conn.execute(text("DROP SCHEMA public CASCADE;"))
        conn.execute(text("CREATE SCHEMA public;"))
    
    print("Creating new tables...")
    create_db.main()
    
    print("Seeding academic years...")
    seed_academic_year()
    
    print("Seeding access tiers...")
    seed_access_tier()
    
    print("Seeding job roles ...")
    seed_job_role()
    
    print("Seeding payment methods ...")
    seed_payment_method()
    
    print("Seeding resource item formats...")
    seed_resource_item_format()
    
    print("Seeding resource phases...")
    seed_resource_phase()
    
    print("Seeding school phases...")
    seed_school_phase()
    
    print("Seeding titles...")
    seed_title()
    
    print("Seeding transaction statuses (statusses? stati?)...")
    seed_transaction_status()
    
    print("Seeding user roles...")
    seed_user_role()
    
    print("Seeding weeks...")
    seed_week()
    
    print("Loading schools from file...")
    import_loader()
    
    print("✅ Database build complete")

if __name__ == "__main__":
    build_database()


