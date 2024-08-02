from flask import Blueprint, render_template, redirect, url_for
from app.models import db, User, Product, Order

main = Blueprint('main', __name__)

@main.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@main.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    return render_template('product_detail.html', product=product)

@main.route('/add_to_cart/<int:id>')
def add_to_cart(id):
    # Simplified for example
    return redirect(url_for('main.index'))

@main.route('/checkout')
def checkout():
    # Simplified for example
    return render_template('checkout.html')
