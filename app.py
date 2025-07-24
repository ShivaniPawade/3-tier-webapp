from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'your-secret-key'

products = [
    {'id': 1, 'name': 'Laptop', 'price': 45000.00, 'image': 'laptop.jpg'},
    {'id': 2, 'name': 'Phone', 'price': 12000.00, 'image': 'phone.jpg'},
    {'id': 3, 'name': 'Keyboard', 'price': 999.00, 'image': 'keyboard.jpg'},
    {'id': 4, 'name': 'Mouse', 'price': 499.00, 'image': 'mouse.jpg'}
]

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "admin" and password == "admin":
        return redirect(url_for('shop'))
    return "Invalid credentials", 401

@app.route('/shop')
def shop():
    return render_template('shop.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    session.modified = True
    return redirect(url_for('shop'))

@app.route('/cart')
def cart():
    cart_items = [p for p in products if p['id'] in session.get('cart', [])]
    return render_template('cart.html', cart_items=cart_items)

if __name__ == "__main__":
    app.run(debug=True)