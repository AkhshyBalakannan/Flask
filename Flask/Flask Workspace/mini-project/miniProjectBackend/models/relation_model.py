from miniProjectBackend import db 


class Relation(db.Model):
    id = db.Column(db.Integer, primary_key=True , nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    sub_category_id = db.Column(db.Integer, db.ForeignKey('subcategory.id'), nullable=True)

    def __repr__(self):
        return f"Relation('{self.category_id}', '{self.sub_category_id}')"
