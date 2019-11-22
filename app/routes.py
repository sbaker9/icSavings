from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User, Product, Price, ProductToUser, Category

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/')
@app.route('/index')
@login_required
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
    return render_template('index.html')


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


