from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# association table
zookeeper_enclosures = db.Table(
    "zookeeper_enclosures",
    db.Column(
        "zookeeper_id", db.Integer, db.ForeignKey("zookeepers.id"), primary_key=True
    ),
    db.Column(
        "enclosure_id", db.Integer, db.ForeignKey("enclosures.id", primary_key=True)
    ),
    extend_existing=True,
)


class Zookeeper(db.Model):
    __tablename__ = "zookeepers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, onpudate=db.func.now(), server_onupdate=db.func.now()
    )

    animals = db.relationship("Animal", backref="zookeeper", lazy=True)

    def __repr__(self):
        return f"<Zookeeper {self.name}>"


class Enclosure(db.Model):
    __tablename__ = "enclosures"

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(50), nullable=False)
    open_to_visitors = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # lazy argument is set to True to load the relationship when it is accessed
    animals = db.relationship("Animal", backref="enclosure", lazy=True)

    def __repr__(self):
        return f"<Enclosure {self.environment}>"


class Animal(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey("zookeepers.id"), nullable=False)
    enclosure_id = db.Column(db.Integer, db.ForeignKey("enclosures.id"), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"<Animal {self.name}>"
