from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import URLForm, LoginForm, RegistrationForm
from app.models import User, Product, Price, ProductToUser, Category
#import matplotlib.pyplot as plt


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():

    form = URLForm()

    form.name.choices = [(a.id, a.name) for a in Product.query.order_by('name')]

    if form.validate_on_submit():
        return render_template('/product page/<name>', form=form)


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

    c1 = Category(name="Toys")
    c2 = Category(name="Electronics")

    db.session.add(c1)
    db.session.add(c2)
    db.session.commit()


    a1 = Product(name="Nintendo Switch with Neon Blue and Neon Red Joy‑Con",
                 description="Play your way with the Nintendo Switch gaming system. Whether you’re at home or on the "
                             "go, solo or with friends, the Nintendo Switch system is designed to fit your life. Dock "
                             "your Nintendo Switch to enjoy HD gaming on your TV. Heading out? Just undock your console and "
                             "keep playing in handheld mode.",
                 url="https://www.amazon.com/dp/B07VGRJDFY/ref=cm_gf_atz_iaaa_d_p0_c0_qd0coEtwouCW5V9Zr4M2HQ8",
                 favorite=False, category=c1,
                 image="https://images-na.ssl-images-amazon.com/images/I/71Qk2M1CIgL._AC_SL1500_.jpg")
    a2 = Product(name="Echo Dot Kids Edition",
                 description="Designed with kids in mind - They can ask Alexa to play music, hear stories, call "
                             "approved friends and family, and explore a world of kid-friendly skills.",
                 url="https://www.amazon.com/dp/B07Q2MXPH6/ref=cm_gf_atz_iaaa_d_p0_c0_qd0O2FWT6ajLcfkyxyUA27t",
                 favorite=True, category=c2,
                 image="https://images-na.ssl-images-amazon.com/images/I/619hTFl4%2BIL._AC_SL1000_.jpg")
    a3 = Product(name="Really RAD Robots - Turbo Bot",
                 description="Turbo Bot is built for speed! With a full function remote control including a turbo "
                             "Boost switch!",
                 url="https://www.amazon.com/dp/B07NSTW6FT/ref=cm_gf_atz_iaaa_d_p0_c0_qd01g4cV1qjOSc2nnti4MzZ",
                 favorite=False, category=c1,
                 image="https://images-na.ssl-images-amazon.com/images/I/61QEo-fe1JL._AC_SL1418_.jpg")
    a4 = Product(name="Hot Wheels Toy Story 4 Bundle Vehicles, 6 Pack",
                 description="The beloved cast becomes a 5-pack of unique and highly coveted Character Cars.",
                 url="https://www.amazon.com/gp/product/B07L8YMFH8/ref=cg_htl-lcat_3a2_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_"
                     "s=desktop-top-slot-6&pf_rd_r=YDW1WMNXF1Y3FFJY0KH5&pf_rd_t=0&pf_rd_p=b4c22792-984a-4880-8b60-"
                     "44dfcac63ee9&pf_rd_i=gf-events--holiday-toy-list",
                 favorite=True, category=c1,
                 image="https://images-na.ssl-images-amazon.com/images/I/81ytG6lfGTL._AC_SL1500_.jpg")
    a5 = Product(name="Beats Solo3 Wireless On-Ear Headphones - Matte Black",
                 description="With up to 40 hours of battery life, Beats Solo3 wireless is your perfect everyday "
                             "headphone.",
                 url="https://www.amazon.com/dp/B01LWWY3E2/ref=cm_gf_aaam_iaaa_d_p0_c0_qd0PoZ3uEKKhZA1d0qZjrgk",
                 favorite=False, category=c2,
                 image="https://images-na.ssl-images-amazon.com/images/I/71sBjbHYbKL._AC_SL1500_.jpg")


    db.session.add(a1)
    db.session.add(a2)
    db.session.add(a3)
    db.session.add(a4)
    db.session.add(a5)

    v1 = Price(price=299.00, datetime=datetime(2019, 10, 14), productID=1)
    v2 = Price(price=289.00, datetime=datetime(2019, 10, 16), productID=1)
    v3 = Price(price=249.00, datetime=datetime(2019, 10, 18), productID=1)
    v4 = Price(price=299.00, datetime=datetime(2019, 10, 20), productID=1)
    v5 = Price(price=309.00, datetime=datetime(2019, 10, 22), productID=1)
    v6 = Price(price=34.99, datetime=datetime(2019, 10, 14), productID=2)
    v7 = Price(price=39.99, datetime=datetime(2019, 10, 16), productID=2)
    v8 = Price(price=44.99, datetime=datetime(2019, 10, 18), productID=2)
    v9 = Price(price=34.99, datetime=datetime(2019, 10, 20), productID=2)
    v10 = Price(price=39.99, datetime=datetime(2019, 10, 22), productID=2)
    v11 = Price(price=39.99, datetime=datetime(2019, 10, 14), productID=3)
    v12 = Price(price=37.99, datetime=datetime(2019, 10, 16), productID=3)
    v13 = Price(price=41.99, datetime=datetime(2019, 10, 18), productID=3)
    v14 = Price(price=38.99, datetime=datetime(2019, 10, 20), productID=3)
    v15 = Price(price=43.99, datetime=datetime(2019, 10, 22), productID=3)
    v16 = Price(price=24.99, datetime=datetime(2019, 10, 14), productID=4)
    v17 = Price(price=26.99, datetime=datetime(2019, 10, 16), productID=4)
    v18 = Price(price=28.99, datetime=datetime(2019, 10, 18), productID=4)
    v19 = Price(price=23.99, datetime=datetime(2019, 10, 20), productID=4)
    v20 = Price(price=24.99, datetime=datetime(2019, 10, 22), productID=4)
    v21 = Price(price=249.00, datetime=datetime(2019, 10, 14), productID=5)
    v22 = Price(price=199.00, datetime=datetime(2019, 10, 16), productID=5)
    v23 = Price(price=179.00, datetime=datetime(2019, 10, 18), productID=5)
    v24 = Price(price=239.00, datetime=datetime(2019, 10, 20), productID=5)
    v25 = Price(price=219.00, datetime=datetime(2019, 10, 22), productID=5)

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

    u1 = User(username="john", email="john@john.com")
    u2 = User(username="evan", email="evan@gmail.com")

    db.session.add(u1)
    db.session.add(u2)

    db.session.commit()

    u1.set_password("firewater")
    u2.set_password("earthair")

    db.session.commit()

    return redirect(url_for('index'))


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/recently-searched', methods=['GET', 'POST'])
def recently():
    products = Product.query.all()

    return render_template('recently-searched.html', searched_products=products)


@app.route('/product-page/<name>', methods=['GET', 'POST'])
def product(name):

    new_product = Product.query.filter_by(name=name).first()

    new_prices = Price.query.filter_by(productID=new_product.id).all()

    new_category = Category.query.filter_by(id=new_product.categoryID).first()

    related_products = Product.query.filter_by(categoryID=new_category.id).all()

    x = []
    y = []
    for price in new_prices:
        x.append(price.datetime)
        y.append(price.price)
    plt.plot(x, y)
    plt.xlabel('Date')
    plt.ylabel('Price')
    graph = plt.show()

    return render_template('product-page.html', product=new_product, prices=new_prices, category=new_category,
                           related_products=related_products, graph=graph)


@app.route('/saved-products', methods=['GET', 'POST'])
def saved_products():
    return render_template('saved-products.html')
