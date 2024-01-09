#!/usr/bin/env python3

# imports
from random import choice as rc

from faker import Faker

from app import app
from models import db, Zookeeper, Animal, Enclosure

fake = Faker()

# since we outside views
with app.app_context():
    # empty tables to avoid duplicate data
    # similar to session.query(Zookeeper).delete() in vanilla SQLAlchemy
    Animal.query.delete()
    Zookeeper.query.delete()
    Enclosure.query.delete()

    # track zookeeper objects
    zookeepers = []

    # generate 25 zookeeper objects
    for n in range(25):
        zk = Zookeeper(name=fake.name(), birthday=fake.date_between(
            start_date='-70y', end_date='-18y'))
        zookeepers.append(zk)

    # guarantees that ids will be updated
    db.session.add_all(zookeepers)

    enclosures = []
    environments = ['Desert', 'Pond', 'Ocean',
                    'Field', 'Trees', 'Cave', 'Cage']

    for n in range(25):
        e = Enclosure(environment=rc(environments),
                      open_to_visitors=rc([True, False]))
        enclosures.append(e)

    db.session.add_all(enclosures)

    animals = []
    species = ['Lion', 'Tiger', 'Bear', 'Hippo', 'Rhino', 'Elephant', 'Ostrich',
               'Snake', 'Monkey']

    for n in range(200):
        name = fake.first_name()

        # ensuring name is unique/if already generated/a new one is generated
        while name in [a.name for a in animals]:
            name = fake.first_name()
        a = Animal(name=name, species=rc(species))
        a.zookeeper = rc(zookeepers)
        a.enclosure = rc(enclosures)
        animals.append(a)

    db.session.add_all(animals)

    # effect changes
    db.session.commit()
