import click
from database.database import Database
from models.models import Product
from seed import seed_database
# Initialize the database
db = Database()
seed_database()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Product Name', help='Name of the product')
@click.option('--quantity', prompt='Product Quantity', help='Quantity of the product')
def add_product(name, quantity):
    """Add a new product to the database."""
    product = Product(name=name, quantity=quantity)
    db.session.add(product)
    db.session.commit()
    print(f'Added product: {product.name} with quantity: {product.quantity}')

@cli.command()
@click.option('--product-id', prompt='Product ID', help='ID of the product to delete')
def delete_product(product_id):
    """Delete a product from the database by ID."""
    product = db.session.query(Product).filter_by(id=product_id).first()
    if product:
        db.session.delete(product)
        db.session.commit()
        print(f'Deleted product: {product.name} with ID: {product.id}')
    else:
        print(f'Product with ID {product_id} not found.')

@cli.command()
@click.option('--product-id', prompt='Product ID', help='ID of the product to update')
@click.option('--name', prompt='New Product Name', help='New name for the product')
@click.option('--quantity', prompt='New Product Quantity', help='New quantity for the product')
def update_product(product_id, name, quantity):
    """Update a product's name and quantity by ID."""
    product = db.session.query(Product).filter_by(id=product_id).first()
    if product:
        product.name = name
        product.quantity = quantity
        db.session.commit()
        print(f'Updated product: {product.name} with ID: {product.id}')
    else:
        print(f'Product with ID {product_id} not found.')

if __name__ == '__main__':
    cli()
