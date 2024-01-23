#!/usr/bin/env python3

from flask import Flask,request,jsonify, make_response
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Hero,Power,HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    response_body = {
        "Hey": "This is the superhero domain"
    }

    response = make_response(jsonify(response_body))
    return response

@app.route('/heroes')
def heroes():
    heroes_list = [hero.to_dict() for hero in Hero.query.all()]
    return make_response(jsonify(heroes_list),200)

@app.route('/heroes/<int:id>')
def heroes_by_id(id):
    hero = Hero.query.filter_by(id=id).first()

    if hero:
        hero_data = hero.to_dict()
        return make_response(jsonify(hero_data), 200)

    else:
        error = {"error": "Hero not found"}
        return make_response(jsonify(error), 404)

@app.route('/powers')
def powers():

    powers = []

    for power in Power.query.all():
        data = {
            "id": power.id,
            "name":power.name,
            "description":power.description
        }    
        powers.append(data)

    return make_response(jsonify(powers), 200)



if __name__ == '__main__':
    app.run(port=5555)
