#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Raccoon, Trashcan, Visit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return "Hello world"

# write your routes here!
@app.get('/raccoons')
def all_raccoons():
    all_rac = Raccoon.query.all()
    return [r.to_dict(rules=('-visits',)) for r in all_rac], 200

@app.get('/trashcans')
def all_trashcans():
    can = Trashcan.query.all()
    return [c.to_dict(rules=('-visits',)) for c in can], 200

@app.get('/visits')
def all_visits():
    visit = Visit.query.all()
    return [v.to_dict() for v in visit], 200

@app.get('/raccoons/<int:id>')
def raccoon_by_id(id):
    rac = db.session.get(Raccoon, id)
    if not rac:
        return {'error': f'raccoon id: {id} has escaped'}, 404
    return rac.to_dict(rules=('-visits.raccoon', '-visits.trashcan')), 200

@app.get('/trashcans/<int:id>')
def trashcan_by_id(id):
    can = db.session.get(Trashcan, id)
    if not can:
        return {'error': f'trashcan id: {id} was stolen!!!'}
    return can.to_dict(rules=('-visits',)), 200

@app.delete('/raccoons/<int:id>')
def delete_raccoon(id):
    rac = db.session.get(Raccoon, id)
    if not rac:
        return {'error': f'raccoon id: {id} has escaped'}, 404
    db.session.delete(rac)
    db.session.commit()
    return {}, 204

@app.post('/visits')
def post_visit():
    try:
        data = request.json
        
        visit = Visit(
            date = data['date'],
            raccoon_id = data['raccoon_id'],
            trashcan_id = data['trashcan_id']
        )
        db.session.add(visit)
        db.commit()
        return visit.to_dict(rules=('-trashcan_id', '-raccoon_id')), 201
    except:
        return {'error': 'Shumting Wong! cannot post'}, 406
    
@app.delete('/visits/<int:id>')
def delete_visit(id):
    visit = db.session.get(Visit, id)
    if not visit:
        return {'error': 'No body had come!'}
    db.session.delete(visit)
    db.session.commit()
    return {}, 204

if __name__ == '__main__':
    app.run(port=5555, debug=True)