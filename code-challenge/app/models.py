from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


db = SQLAlchemy()

#Model on superheroes
class Hero(db.Model,SerializerMixin):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #Relationship between hero and the her_powers
    heropowers = db.relationship("Hero_powers", backref='hero')
   
    def serialize(self):
        return{
            "id":self.id,
            "name":self.name,
            "super_name":self.super_name
        }



#Model on powers
class Powers(db.Model,SerializerMixin):
    __tablename__='powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #Relationship between powers and the her_powers
    heropowers = db.relationship("Hero_powers", backref='powers')
    
    def serialize(self):
        return{
            "id": self.id ,
            "name": self.name,
            "description": self.description
        }


#Model on hero_powers
class Hero_powers(db.Model,SerializerMixin):
    __tablename__ ='hero_power'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


     #Validates the strength attribute
    @validates("strength")
    def validate_strength(self, key, strength):
        strengths = ["Strong", "Weak", "Average"]
        if not strength in strengths:
            raise ValueError(
                "Strength must be one of the following values: 'Strong', 'Weak', 'Average'"
            )
        return strength
    

    
    def serialize(self):
        power = Powers.query.filter_by( id = self.power_id).first()
        return power.serialize()


