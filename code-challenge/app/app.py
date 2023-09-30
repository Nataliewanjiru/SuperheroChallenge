#!/usr/bin/env python3

from flask import Flask, jsonify,request,make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse

from models import *

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


#Get request for home route
class Home(Resource):
  def get(self):
      return 'Welcome to this API'
  
api.add_resource(Home, '/')


#Get request for all the heroes in the database
class Heroes(Resource):
   def get(self):
      heroes = Hero.query.all()#To get all heroes from the database
      serialized_heroes = [hero.serialize() for hero in heroes]#Gets the serialize function for each
      return jsonify(serialized_heroes)
      
api.add_resource(Heroes,'/heroes')


#Get request for heroes by id
class HeroById(Resource):
   def get(self,id):
      hero = Hero.query.get(id)#To get all hero from the database by the ID
      if hero:
        serialized_hero = hero.serialize()#Gets the serialize function
        return jsonify(serialized_hero)
      else:
         return {'error':"Hero not found"}
      
api.add_resource(HeroById,'/heroes/<int:id>')


#Get request for all the powers in the Powers table
class Power(Resource):
   def get(self):
      powers = Powers.query.all()#To get all powers from the database
      serialized_powers = [power.serialize() for power in powers]#Gets the serialize function for each power
      return jsonify(serialized_powers)
      
api.add_resource(Power,'/powers')



class PowerById(Resource):
   #Get request for powers by id
   def get(self,id):
      power = Powers.query.get(id)#To get all power from the database by the ID
      if power:
        serialized_power = power.serialize()#Gets the serialize function
        return jsonify(serialized_power)
      else:
         return {'error':"Power not found"}
      

  #Patch request to powers
   def patch(self,id):
      data=Powers.query.filter_by(id=id).first()
      if data:
         for desc in request.form:
            setattr(data, desc,request.form[desc])
  
         db.session.add(data)
         db.session.commit()

         response_answer = data.serialize()

         response = make_response(
            jsonify(response_answer),200
         )

         return response
      else :
         return {"message":["validation errors"]}

   
  
api.add_resource(PowerById,'/powers/<int:id>')


class Heropowers(Resource):
  def get(self):
     price = request.form.get('price')
    pizza_id = request.form.get('pizza_id')
    restaurant_id = request.form.get('restaurant_id')
     
api.add_resource(Heropowers,'/hero_powers')



if __name__ == '__main__':
    app.run(port=5555)
