from  app.models import *

def seed_powers():
    powers_data = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
    ]

    for power_info in powers_data:
        power = Power(**power_info)
        db.session.add(power)

    db.session.commit()
    return "Powers seeded successfully"

# Seed the database with heroes and their powers
@app.route('/seed_heroes')
def seed_heroes():
    heroes_data = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Janet Van Dyne", "super_name": "The Wasp"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
        {"name": "Elektra Natchios", "super_name": "Elektra"}
    ]

    strengths = ["Strong", "Weak", "Average"]

    for hero_info in heroes_data:
        hero = Hero(**hero_info)
        db.session.add(hero)

        for _ in range(randint(1, 3)):
            power = Power.query.get(randint(1, 4))  # Assuming there are 4 powers in the database
            strength = choice(strengths)

            hero_power = HeroPower(hero=hero, power=power, strength=strength)
            db.session.add(hero_power)

    db.session.commit()
    return "Heroes seeded successfully"