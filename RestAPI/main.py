from flask import Flask,jsonify,request
from flask_restful import Api
import os
from flask_sqlalchemy import  SQLAlchemy
from flask_marshmallow import  Marshmallow
from Models  import db
from  View import CustomerView,CustomersView,OrderView,ProductsView,ProductView,OrdersView,OrderHistoryView


app = Flask(__name__)

# app.config.from_object('config')
basedir = os.path.abspath(os.path.dirname(__file__))

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# @app.before_first_request
# def create_table():
#     db.create_all()
app.app_context().push()


api = Api(app)

api.add_resource(CustomersView,'/customers')
api.add_resource(CustomerView,'/customer/<string:CustomerID>')


api.add_resource(ProductsView,'/products')
api.add_resource(ProductView,'/product/<string:ProductID>')

api.add_resource(OrdersView,'/orders')
api.add_resource(OrderView,'/orders/<int:OrderID>')


api.add_resource(OrderHistoryView,'/orderhistory/<string:CustomerID>')


if __name__ == '__main__':
    app.run(debug=True)