from miniProjectBackend import db
from miniProjectBackend.models.relation_model import Relation


class SubCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True , nullable=False)
    sub_category_name = db.Column(db.String, nullable=False)
    rel_sub_category = db.relationship('Relation', backref='subcategories', lazy=True)

    def __repr__(self):
        return f"Category('{self.sub_category_name}')"