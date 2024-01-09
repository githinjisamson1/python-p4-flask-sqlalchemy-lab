# no need to import individual fields
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# create db instance
db = SQLAlchemy(metadata=metadata)


# models
# db.model === Base in vanilla SQLAllchemy
class Zookeeper(db.Model):
    # table name
    __tablename__ = 'zookeepers'

    # columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.String)

    # relationship
    animals = db.relationship("Animal", backref="zookeeper")


class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)

    animals = db.relationship("Animal", backref="enclosure")


class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    # foreign keys
    zookeeper_id = db.Column(db.Integer, db.ForeignKey("zookeepers.id"))
    enclosure_id = db.Column(db.Integer, db.ForeignKey("enclosures.id"))
