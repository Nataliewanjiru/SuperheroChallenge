from app import *
from random import randint,choice


with app.app_context():
    hero= Hero(name="Tony Stark", super_name="Iron man")
    power = Powers(name="Iron suit powers",description="A scientifical suit that runs on electrical energy to give extra-odinary power")
    #db.session.add(hero)
    #db.session.add(power)
    #db.session.commit()
    
    heropowers = Hero_powers(strength="Iron suit", hero_id=1, power_id =2)
    db.session.add(heropowers)
    db.session.commit()

#def seed_powers():
#    powers_data = [
#        {"name": "super strength", "description": "gives the wielder super-human strengths"},
#        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
#        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
#        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
#    ]
#
#    for power_info in powers_data:
#        power = Powers(**power_info)
#        db.session.add(power)
#
#    db.session.commit()
#    return "Powers seeded successfully"
#
## Seed the database with heroes and their powers
#def seed_heroes():
#    heroes_data = [
#        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
#        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
#        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
#        {"name": "Janet Van Dyne", "super_name": "The Wasp"},
#        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
#        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
#        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
#        {"name": "Ororo Munroe", "super_name": "Storm"},
#        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
#        {"name": "Elektra Natchios", "super_name": "Elektra"}
#    ]
#
#    strengths = ["Strong", "Weak", "Average"]
#
#    for hero_info in heroes_data:
#        hero = Hero(**hero_info)
#        db.session.add(hero)
#
#        for _ in range(randint(1, 3)):
#            power = Powers.query.get(randint(1, 4))  # Assuming there are 4 powers in the database
#            strength = choice(strengths)
#
#            hero_power = Hero_powers(hero=hero, power=power, strength=strength)
#            db.session.add(hero_power)
#
#    db.session.commit()
#    return "Heroes seeded successfully"
#
#
#if __name__ == '__main__':
#    # Make sure you create the database tables before seeding
#    with app.app_context():
#        db.create_all()
#        seed_powers()
#        seed_heroes()
#