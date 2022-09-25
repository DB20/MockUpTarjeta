from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum


db = SQLAlchemy()

class Balance(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cantidad = db.Column(db.Integer)
    tarjeta = db.Column(db.Integer)

class BalanceSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Balance
         load_instance = True