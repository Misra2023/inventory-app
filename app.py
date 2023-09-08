import click

from database.database import Database
from models.models import Product, Category, Location

# ...rest of your code...

@click.group()
def cli():
    """Business Inventory CLI"""

@cli.command()
@click.option('--name', prompt='Product Name', help='Name of the product')
@click.option('--quantity', prompt='Quantity', type=int, help='Quantity of the product')
@click.option('--category', prompt='Category', help='Category of the product')
@click.option('--location', prompt='Location', help='Location of the product')
def add_product(name, quantity, category, location):
    """Add a new product to the inventory"""
    db = Database()
    product = Product(name=name, quantity=quantity)
    
    # Get or create category and location
    product.category = db.get_or_create(Category, name=category)
    product.location = db.get_or_create(Location, name=location)
    
    db.session.add(product)
    db.session.commit()
    click.echo('Product added successfully.')

@cli.command()
def list_products():
    """List all products in the inventory"""
    db = Database()
    products = db.session.query(Product).all()
    for product in products:
        click.echo(f'Product: {product.name}, Quantity: {product.quantity}')

if __name__ == '__main__':
    cli()
