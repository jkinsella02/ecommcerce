from flask import Flask, request, redirect, url_for, session, render_template, flash
from dao.productdao import ProductDAO
from dao.userdao import UserDAO

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Context processor for total items in cart
@app.context_processor
def utility_processor():
    def cart_total_items():
        if 'cart' in session:
            return sum(session['cart'].values())  # Total quantity of items in cart
        return 0
    return dict(cart_total_items=cart_total_items)

# Routes
@app.route('/')
def home():
    proddao = ProductDAO()
    products = proddao.getAllProducts()
    return render_template('index.html', products=products)

@app.route('/index')
def index():
    proddao = ProductDAO()
    products = proddao.getAllProducts()
    return render_template('index.html', products=products)

@app.route('/admin')
def admin():
    return render_template('adminhome.html')

@app.route('/product/<int:product_id>')
def product(product_id):
    proddao = ProductDAO()
    product = proddao.getProduct(product_id=product_id)
    print(f"DEBUG: product.imageUrl = {product.imageUrl}")  # Debugging output
    return render_template('product.html', product=product)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        userdao = UserDAO()
        user = userdao.getuserbyusername(username=username)
        if user is None or user.password != password:
            return redirect(url_for('index'))

        session['username'] = user.username
        if user.user_type == 'administrator':
            return redirect(url_for('admin'))
        elif user.user_type == 'customer':
            return redirect(url_for('index'))
    else:
        return render_template('login.html')

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    quantity = int(request.form.get('quantity', 1))

    if 'cart' not in session:
        session['cart'] = {}

    cart = session['cart']
    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    session['cart'] = cart
    flash('Item added to cart successfully!', 'success')  # Add success message
    return redirect(request.referrer)  # Stay on the same page

@app.route('/basket')
def basket():
    try:
        cart = session.get('cart', {})
        proddao = ProductDAO()
        cart_items = []

        for product_id, quantity in cart.items():
            product = proddao.getProduct(product_id=int(product_id))
            if product:
                cart_items.append({
                    'product': product,
                    'quantity': quantity
                })
            else:
                print(f"Product with ID {product_id} not found.")  # Debugging

        return render_template('basket.html', cart_items=cart_items)
    except Exception as e:
        print(f"Error in /basket: {e}")  # Debugging output
        return "An error occurred while loading the basket.", 500

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
