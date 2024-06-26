from datetime import datetime

from .db import db, environment, SCHEMA, add_prefix_for_prod


class UserBuy(db.Model):
    __tablename__ = "user_buys"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False
    )
    vehicle_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("vehicles.id")), nullable=False
    )
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    delivery_address = db.Column(db.String(200), nullable=False)
    finalized = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    buyer = db.relationship("User", back_populates="purchase")
    vehicle = db.relationship("Vehicle", back_populates="purchase")

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "vehicleId": self.vehicle_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "deliveryAddress": self.delivery_address,
            "finalized": self.finalized,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }
