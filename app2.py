 
# # from flask import Flask, jsonify, session
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_cors import CORS
# # from flask import url_for, request  
# # from sqlalchemy.orm import relationship
# # from flask_bcrypt import Bcrypt
# # from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
# # from sqlalchemy.dialects.postgresql import JSON 
# # from sqlalchemy.orm import sessionmaker


# # app = Flask(__name__)
# # CORS(app)  # Enable CORS for all routes
# # app.config['SECRET_KEY'] = 'your_secret_key_here'
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# # db = SQLAlchemy(app)
# # bcrypt = Bcrypt(app)
# # login_manager = LoginManager(app)
# # login_manager.login_view = 'login'


# # class User(db.Model, UserMixin):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(20), unique=True, nullable=False)
# #     password = db.Column(db.String(60), nullable=False)
# #     cart = db.relationship('CartItem', backref='user', lazy=True)

# #     def __repr__(self):
# #         return f"User('{self.username}')"

# # class Product(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String(100), nullable=False)
# #     description = db.Column(db.Text, nullable=False)
# #     price = db.Column(db.Float, nullable=False)
# #     quantity = db.Column(db.Integer, nullable=False)
# #     image = db.Column(db.String(100), nullable=False)

# #     def to_dict(self):
# #         return {
# #             'id': self.id,
# #             'name': self.name,
# #             'description': self.description,
# #             'price': self.price,
# #             'quantity': self.quantity,
# #             'image': url_for('static', filename=f'{self.image}')
# #         }


# # class CartItem(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
# #     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
# #     quantity = db.Column(db.Integer, nullable=False)


# # @login_manager.user_loader
# # def load_user(user_id):
# #     return User.query.get(int(user_id))


# # @app.route('/')
# # def home():
# #     products = Product.query.all()
# #     products_list = [product.to_dict() for product in products]
# #     return jsonify(products=products_list)

# # @app.route('/products')
# # def products():
# #     products = Product.query.all()
# #     products_list = [product.to_dict() for product in products]
# #     return jsonify(products=products_list)

# # @app.route('/login', methods=['POST'])
# # def login():
# #     data = request.get_json()
# #     username = data['username']
# #     password = data['password']
# #     user = User.query.filter_by(username=username).first()

# #     if user and bcrypt.check_password_hash(user.password, password):
# #         login_user(user)
# #         return jsonify({'message': 'Login successful', 'user': user.to_dict()})
# #     else:
# #         return jsonify({'message': 'Invalid username or password'}), 401

# # from flask import jsonify

# # @app.route('/register', methods=['POST'])
# # def register():
# #     if request.method == 'POST':
# #         data = request.get_json()

# #         print('Received data:', data)  # Add this line to print the received data

# #         username = data.get('username')
# #         password = data.get('password')

# #         if not username or not password:
# #             return jsonify({'error': 'Missing username or password'}), 400

# #         hashed_password = bcrypt.generate_password_hash(
# #             password).decode('utf-8')

# #         new_user = User(username=username, password=hashed_password)

# #         # Create a cart for the new user
# #         new_cart = CartItem(user=new_user, quantity=0)  # You can set the initial quantity as needed
# #         db.session.add(new_user)
# #         db.session.add(new_cart)
        
# #         # Commit the changes to the database
# #         db.session.commit()

# #         return jsonify({'message': 'User registered successfully'})



# # @app.route('/logout')
# # @login_required
# # def logout():
# #     logout_user()
# #     return jsonify({'message': 'Logout successful'})


# # @app.route('/add_to_cart/<int:product_id>')
# # @login_required
# # def add_to_cart(product_id):
# #     product = Product.query.get(product_id)

# #     if not product:
# #         return jsonify({'message': 'Product not found'}), 404

# #     cart_item = CartItem(user=current_user, product=product, quantity=1)
# #     db.session.add(cart_item)
# #     db.session.commit()

# #     return jsonify({'message': 'Product added to cart successfully'})


# # @app.route('/Cart')
# # @login_required
# # def cart():
# #     cart_items = current_user.cart
# #     cart_items_list = [{'product': item.product.to_dict(), 'quantity': item.quantity} for item in cart_items]
# #     return jsonify(cart_items=cart_items_list)


# # if __name__ == '__main__':
# #     with app.app_context():
# #         db.create_all()

# #         # # Create some example products
# #         # example_products = [
# #         #     Product(name='Product 1', description='Description 1', price=10.0, quantity=100, image='images/Image7.jpg'),
# #         #     Product(name='Product 2', description='Description 2', price=20.0, quantity=50, image='images/Image2.jpg'),
# #         #     Product(name='Product 3', description='Description 3', price=15.0, quantity=75, image='images/Image4.jpg'),
# #         # ]

# #         # for product in example_products:
# #         #     db.session.add(product)

# #         # db.session.commit()

# #         app.run(debug=True)



# from flask import Flask, jsonify, session, request, redirect
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
# from datetime import datetime
# from sqlalchemy.orm import relationship
# from flask_bcrypt import Bcrypt
# from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
# from flask_session import Session
# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
# from flask_bcrypt import Bcrypt
# # from flask_jwt_extended import jwt_required, get_jwt_identity


# app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Replace with your database URL
# app.config['SECRET_KEY'] = 'your_strong_secret_key'  # Replace with a strong secret key
# app.config["JWT_SECRET_KEY"] = 'your_jwt_secret_key'  # Replace with a secure JWT secret key
# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)
# jwt = JWTManager(app)
# blacklist = set()  # Define the blacklist

 
# CORS(app)


# # class User(db.Model, UserMixin):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(20), unique=True, nullable=False)
# #     password = db.Column(db.String(60), nullable=False)
# #     cart = db.relationship('CartItem', backref='user', lazy=True)

# #     def __repr__(self):
# #         return f"User('{self.username}')"

# # class Product(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String(100), nullable=False)
# #     description = db.Column(db.Text, nullable=False)
# #     price = db.Column(db.Float, nullable=False)
# #     quantity = db.Column(db.Integer, nullable=False)
# #     image = db.Column(db.String(100), nullable=False)

# #     def to_dict(self):
# #         return {
# #             'id': self.id,
# #             'name': self.name,
# #             'description': self.description,
# #             'price': self.price,
# #             'quantity': self.quantity,
# #             'image': url_for('static', filename=f'{self.image}')
# #         }


# # class CartItem(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
# #     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
# #     quantity = db.Column(db.Integer, nullable=False)



# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data['username']
#     password = data['password']
#     print('Received data:', username , password)

#     user = User.query.filter_by(name=username).first()

#     if user and bcrypt.check_password_hash(user.password, password):
#         access_token = create_access_token(identity=user.id)
#         return jsonify({'message': 'Login Success', 'access_token': access_token})
#     else:
#         return jsonify({'message': 'Login Failed'}), 401



# @app.route('/logout', methods=['POST'])
# @jwt_required()
# def logout():
#     jti = get_jwt()['jti']  # Get the JWT ID
#     # Add jti to a blacklist (in-memory, database, or Redis)
#     blacklist.add(jti)  # Example using in-memory blacklist
#     return jsonify({'message': 'Successfully logged out'}), 200


# @app.route('/register', methods=['POST'])
# def register():
#     if request.method == 'POST':
#         data = request.get_json()

#         print('Received data:', data)  # Add this line to print the received data

#         username = data[ 'username' ]
#         password = data[ 'Password' ]

#         if not username or not password:
#             return jsonify({'error': 'Missing username or password'}), 400

#         hashed_password = bcrypt.generate_password_hash(
#             password).decode('utf-8')

#         new_user = User(name=username, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()

#         return jsonify({'message': 'User registered successfully'})


 
     
# @app.route('/tasks', methods=['GET'])
# @jwt_required() 
# def tasks():
#     user_id = get_jwt_identity()  # Retrieve user ID from JWT
#     user_tasks = Task.query.filter_by(user_id=user_id).all()
#     tasks_data = [{'id': task.id, 'title': task.title} for task in user_tasks]
#     return jsonify({'tasks': tasks_data})


# @app.route('/add_tasks', methods=['POST'])
# @jwt_required()
# def add_task():
#     if request.method == 'POST':
#         data = request.get_json()
#         task_name = data['Task']
#         date_added = data['Date ']
#         user_id = get_jwt_identity()  # Retrieve user ID from JWT

        
#         new_task = Task(title=task_name, date_created=datetime.strptime(date_added, '%Y-%m-%d'), user_id=user_id)
#         db.session.add(new_task)
#         db.session.commit()
#         return jsonify({'message': 'Task added to cart successfully!'})

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()

#     app.run(debug=True)

