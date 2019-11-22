from app import app, db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class ProductToUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))
    productID = db.Column(db.Integer, db.ForeignKey('product.id'))

    user = db.relationship('User', backref='product', lazy=True)
    product = db.relationship('Product', backref='user', lazy=True)

    def __repr__(self):
        return '<ArtistToEvent {}>' .format(self.artistID, self.eventID)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(2048), index=True)
    url = db.Column(db.VARCHAR(512))
    favorite = db.Column(db.Boolean, default=False, nullable=False)
    category = db.relationship('Category', backref='product', lazy=True)
    categoryID = db.Column(db.String, db.ForeignKey('category.id'))
    p2us = db.relationship('ProductToUser', back_populates='product', lazy='dynamic')

    def __repr__(self):
        return '<Product {}>' .format(self.name)


class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    datetime = db.Column(db.DateTime)
    productID = db.Column(db.Integer, db.ForeignKey('product.id'))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True)
    products = db.relationship('Product', back_populates='category', lazy='dynamic')

    def __repr__(self):
        return '<Category {}>' .format(self.name)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
