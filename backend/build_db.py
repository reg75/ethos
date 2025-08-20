from app.db import engine, Base
import app.models

import create_db
from db import (
    import_loader,
    seed_academic_year,
    seed_access_tier,
    seed_job_role,
    seed_payment_method,
    seed_resource_item,
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
    print("===| Dropping all tables |===")
    Base.metadata.drop_all(bind=engine) 
    print("===| Building database |===")
    
    print("Creating new tables...")
    create_db.main()
    
    print("Seeding academic years...")
    seed_academic_year.main()
    
    print("Seeding access tiers...")
    seed_access_tier.main()
    
    print("Seeding job roles ...")
    seed_job_role.main()
    
    print("Seeding payment methods ...")
    seed_payment_method.main()
    
    print("Seeding resource items...")
    seed_resource_item.main()
    
    print("Seeding resource phases...")
    seed_resource_phase.main()
    
    print("Seeding school phases...")
    seed_school_phase.main()
    
    print("Seeding titles...")
    seed_title.main()
    
    print("Seeding transaction statuses (statusses? stati?)...")
    seed_transaction_status.main()
    
    print("Seeding user roles...")
    seed_user_role.main()
    
    print("Seeding weeks...")
    seed_week.main()
    
    print("Loading schools from file...")
    import_loader.main()
    
    print("✅ Database build complete")

if __name__ == "__main__":
    build_database()


