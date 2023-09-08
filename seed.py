from database.database import Database
from models.models import Category, Location, Product

# Initialize the database connection
db = Database()

def seed_database():
    # Create or get categories and locations
    category1 = db.get_or_create(Category, name="Electronics")
    category2 = db.get_or_create(Category, name="Clothing")
    location1 = db.get_or_create(Location, name="Warehouse A")
    location2 = db.get_or_create(Location, name="Store 1")\

    print(category1)

    # Add some example products

    # Use the retrieved Category and Location instances here
    product1 = db.get_or_create(Product, name="Laptop", quantity=10, category_id=category1.id, location_id=location1.id)
    product2 = db.get_or_create(Product, name="T-shirt", quantity=100, category_id=category2.id, location_id=location2.id)
    product3 = db.get_or_create(Product, name="Smartphone", quantity=20, category_id=category1.id, location_id=location1.id)
    product4 = db.get_or_create(Product, name="Jeans", quantity=50, category_id=category2.id, location_id=location2.id)

    # Commit the changes to the database
    db.session.commit()

    print("Database seeded successfully.")