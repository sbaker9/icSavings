from app import app, db
from flask import redirect, url_for, flash
from app.models import Product, Price, Category, ProductToUser, User


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/reset_db')
def reset_db():
    flash("Resetting database: deleting old data and repopulating with dummy data")
    # clear all data from all tables
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
    db.session.commit()

    # adding dummy data--

    a1 = Product(name="", info="", url="", favorite=False, category="Electronics", categoryID=2)
    a2 = Product(name="", info="", url="", favorite=True, category="Electronics", categoryID=2)
    a3 = Product(name="", info="", url="", favorite=False, category="Toys", categoryID=1)
    a4 = Product(name="", info="", url="", favorite=True, category="Toys", categoryID=1)
    a5 = Product(name="", info="", url="", favorite=False, category="Electronics", categoryID=2)

    db.session.add(a1)
    db.session.add(a2)
    db.session.add(a3)
    db.session.add(a4)
    db.session.add(a5)

    v1 = Price(price=0.01, datetime="", productID=1)
    v2 = Price(price=0.01, datetime="", productID=1)
    v3 = Price(price=0.01, datetime="", productID=1)
    v4 = Price(price=0.01, datetime="", productID=1)
    v5 = Price(price=0.01, datetime="", productID=1)
    v6 = Price(price=0.01, datetime="", productID=2)
    v7 = Price(price=0.01, datetime="", productID=2)
    v8 = Price(price=0.01, datetime="", productID=2)
    v9 = Price(price=0.01, datetime="", productID=2)
    v10 = Price(price=0.01, datetime="", productID=2)
    v11 = Price(price=0.01, datetime="", productID=3)
    v12 = Price(price=0.01, datetime="", productID=3)
    v13 = Price(price=0.01, datetime="", productID=3)
    v14 = Price(price=0.01, datetime="", productID=3)
    v15 = Price(price=0.01, datetime="", productID=3)
    v16 = Price(price=0.01, datetime="", productID=4)
    v17 = Price(price=0.01, datetime="", productID=4)
    v18 = Price(price=0.01, datetime="", productID=4)
    v19 = Price(price=0.01, datetime="", productID=4)
    v20 = Price(price=0.01, datetime="", productID=4)
    v21 = Price(price=0.01, datetime="", productID=5)
    v22 = Price(price=0.01, datetime="", productID=5)
    v23 = Price(price=0.01, datetime="", productID=5)
    v24 = Price(price=0.01, datetime="", productID=5)
    v25 = Price(price=0.01, datetime="", productID=5)

    db.session.add(v1)
    db.session.add(v2)
    db.session.add(v3)
    db.session.add(v4)
    db.session.add(v5)
    db.session.add(v6)
    db.session.add(v7)
    db.session.add(v8)
    db.session.add(v9)
    db.session.add(v10)
    db.session.add(v11)
    db.session.add(v12)
    db.session.add(v13)
    db.session.add(v14)
    db.session.add(v15)
    db.session.add(v16)
    db.session.add(v17)
    db.session.add(v18)
    db.session.add(v19)
    db.session.add(v20)
    db.session.add(v21)
    db.session.add(v22)
    db.session.add(v23)
    db.session.add(v24)
    db.session.add(v25)

    c1 = Category(name="Toys")
    c2 = Category(name="Electronics")

    db.session.add(c1)
    db.session.add(c2)

    pu1 = ProductToUser(userID=1, productID=1)
    pu2 = ProductToUser(userID=1, productID=2)
    pu3 = ProductToUser(userID=1, productID=4)
    pu4 = ProductToUser(userID=2, productID=1)
    pu5 = ProductToUser(userID=2, productID=3)
    pu6 = ProductToUser(userID=2, productID=4)
    pu7 = ProductToUser(userID=2, productID=5)

    db.session.add(pu1)
    db.session.add(pu2)
    db.session.add(pu3)
    db.session.add(pu4)
    db.session.add(pu5)
    db.session.add(pu6)
    db.session.add(pu7)

    u1 = User(username="", email="", password="")
    u2 = User(username="", email="", password="")

    db.session.add(u1)
    db.session.add(u2)

    db.session.commit()

    return redirect(url_for('index'))