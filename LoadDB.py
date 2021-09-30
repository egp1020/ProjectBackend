from app import db
from app.inventory.model import Inventory
from app.product.model import Product
from app.tax.model import Tax
from app.taxDetails.model import TaxDetails
from app.category.model import Category

if __name__ == '__main__':
    db.create_all()
    db.session.commit()