from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from .db import db, environment, SCHEMA, add_prefix_for_prod


class User(db.Model, UserMixin):
    __tablename__ = "users"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    state = db.Column(db.String(2), nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)

    purchase = db.relationship("UserBuy", back_populates="buyer")
    sell = db.relationship("UserSell", back_populates="seller")
    comment = db.relationship("Review", back_populates="commenter")
    # wishs = db.relationship("Vehicle", secondary="wishlists", back_populates="user")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "state": self.state,
        }
