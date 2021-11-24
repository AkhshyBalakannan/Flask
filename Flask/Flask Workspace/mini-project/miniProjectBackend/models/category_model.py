from miniProjectBackend import db 
from miniProjectBackend.models.relation_model import Relation

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True , nullable=False)
    category_name = db.Column(db.String, nullable=False)
    rel_category = db.relationship('Relation', backref='categories', lazy=True)

    def __repr__(self):
        return f"Category('{self.category_name}')"
