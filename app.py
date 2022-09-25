from tokenize import String
from urllib import request
from microservicio_tarjeta import create_app
from flask_restful import Resource, Api
from flask import Flask, request, jsonify
import random
from flask.json import JSONEncoder
from datetime import datetime
from flask_jwt_extended import jwt_required, create_access_token,get_jwt
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
import decimal
from .Modelos import db, Balance, BalanceSchema
import json

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.init_app(app)

balance_schema = BalanceSchema()


class Retirar(Resource):

    def put(self, id_balance): 
        balance = Balance.query.get_or_404(id_balance)
        cantidadret = request.json["cantidad_Retirada"]
        balance_new = Balance.cantidad - cantidadret
        balance.cantidad = balance_new
        db.session.commit()
        return balance_schema.dump(balance)

class agregar(Resource):
    def post (self):
        nuevo_balance = Balance(cantidad=request.json["ingreso"], tarjeta = request.json["tarjeta"])
        db.session.add(nuevo_balance)
        db.session.commit()
        return balance_schema.dump(nuevo_balance)        

api.add_resource(Retirar, '/retirar/<int:id_balance>')
api.add_resource(agregar, '/agregar')
