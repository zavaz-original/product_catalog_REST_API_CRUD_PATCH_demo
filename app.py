# Python Flask SQLAlchemy
# used below video guide to implement GET, POST, DELETE operations. 
# https://www.youtube.com/watch?v=qbLc5a9jdXo 
# Added support for PUT and PATCH operations by own investigations.

# C:\Users\Omistaja\py_world\api> python -m venv .venv
# .venv\Scripts\activate
# (.venv) PS C:\Users\Omistaja\py_world\api> pip install flask
# (.venv) PS C:\Users\Omistaja\py_world\api> pip install flask-sqlalchemy
# (.venv) PS C:\Users\Omistaja\py_world\api> pip freeze > requirements.txt

from flask import Flask, request, render_template
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(80), unique= True, nullable= False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.id} - {self.name} - {self.description}"

# to do: move the static guide.html under folder static.
@app.route('/')
@app.route('/home')
def index():
    return render_template('guide.html')

# R of CRUD, Retrieve all products, json -> html table
@app.route('/products')
def get_products():
    headers = [ "id", "Product", "Description"]
    products = Product.query.all()
    json = []
    for product in products:
        product_data = {'id': product.id, 'name' : product.name, 'description' : product.description }
        json.append(product_data)
    return render_template('products.html', headers = headers, json = json)
    # return {"products": output}

# http://localhost:5000/products

# R of CRUD, Retrieve 1 product, json -> html table, GET
@app.route('/products/<int:id>')
def get_product(id):
    headers = [ "id", "Product", "Description"]
    product = Product.query.get_or_404(id)
    json = []
    product_data = {'id': product.id, 'name' : product.name, 'description' : product.description }
    json.append( product_data )
    return render_template('products.html', headers = headers, json = json)
# http://localhost:5000/products/1

# C of CRUD, Create/add 1 product, json -> html table, GET
@app.route('/products', methods=['POST'])
def add_product():
    product = Product(name=request.json['name'], description=request.json['description'])
    db.session.add(product)
    db.session.commit()
    return {'id': product.id, 'name': product.name, 'description': product.description}
# Tested by Postman

# U of CRUD, Update/Overwrite 1 product, return json
@app.route('/products/<int:id>', methods=['PUT'])
def replace_product(id):
    product = Product.query.get(id)
    if product is None:
        return { 'error': 'not found'}
    setattr(product, 'name', request.json['name'])
    setattr(product, 'description', request.json['description'])
    db.session.commit()
    return {'id': product.id, 'name': product.name, 'description': product.description}
# Tested by Postman

# PATCH, Update/Overwrite >=1 fields in a product, return json
@app.route('/products/<int:id>', methods=['PATCH'])
def update_some_product_fields(id):
    product = Product.query.get(id)
    if product is None:
        return { 'error': 'not found'}
    new_name = request.json.get('name')
    if  new_name != None:
        setattr(product, 'name', new_name)
    new_description = request.json.get('description')
    if  new_description != None:
        setattr(product, 'description', new_description)
    db.session.commit()
    return {'id': product.id, 'name': product.name, 'description': product.description}
# Tested by Postman

# D of CRUD, Delete 1 product, return json
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if product is None:
        return { 'error': 'not found'}
    db.session.delete(product)
    db.session.commit()
    return { 'deleted': id }
# Tested by Postman

if __name__ == '__main__':
   app.run(debug= False)


