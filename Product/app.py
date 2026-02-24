from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 70000},
    {"id": 2, "name": "Phone", "price": 25000}
]

@app.route('/')
def home():
    return jsonify({"message": "Product Service Running"})

@app.route('/products')
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)