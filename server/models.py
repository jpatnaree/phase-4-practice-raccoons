from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Raccoon(db.Model, SerializerMixin):
    __tablename__ = 'raccoon_table'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    
    serialize_rules = ('-visits.raccoon',)
    
    visits = db.relationship('Visit', back_populates='raccoon')
    trashcan = association_proxy('visits', 'trashcan')
    
    @validates('age')
    def validate_age(self, key, value):
        if value <= 0:
            raise ValueError('age must be greater than 0')
        return value


class Visit(db.Model, SerializerMixin):
    __tablename__ = 'visit_table'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    
    raccoon_id = db.Column(db.Integer, db.ForeignKey('raccoon_table.id'))
    trashcan_id = db.Column(db.Integer, db.ForeignKey('trashcan_table.id'))
    
    serialize_rules = ('-raccoon.visits','-trashcan.visits')
    
    raccoon = db.relationship('Raccoon', back_populates='visits')
    trashcan = db.relationship('Trashcan', back_populates='visits')


class Trashcan(db.Model, SerializerMixin):
    __tablename__ = 'trashcan_table'
    
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String, nullable=False)
    
    serialize_rules = ('-visits.trashcan',)
    
    visits = db.relationship('Visit', back_populates='trashcan')
    raccoon = association_proxy('visits', 'raccoon')