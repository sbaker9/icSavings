from app import app
from app.models import ProductToUser, Product, User, Price, Category


@app.shell_context_processor
def make_shell_context():
    return {'app.db': app.db, 'Product': Product, 'Price': Price, 'Category': Category, 'ProductToUser': ProductToUser, 'User': User, }

