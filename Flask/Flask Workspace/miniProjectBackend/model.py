from miniProjectBackend import db 

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True , nullable=False)
    category_name = db.Column(db.String, nullable=False)
    rel_category = db.relationship('Relation', backref='categories.id', lazy=True)

    def __repr__(self):
        return f"Category('{self.category_name}')"

class SubCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True , nullable=False)
    sub_category_name = db.Column(db.String, nullable=False)
    rel_subcategory = db.relationship('Relation', backref='subcategories', lazy=True)

    def __repr__(self):
        return f"Category('{self.sub_category_name}')"

class Relation(db.Model):
    id = db.Column(db.Integer, primary_key=True , nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    sub_category_id = db.Column(db.Integer, db.ForeignKey('subcategory.id'))

    def __repr__(self):
        return f"Relation('{self.category_id}')"

# -------------------------------------------------------------------------------------

# from miniProjectBackend import db 

# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True , nullable=False)
#     category_name = db.Column(db.String, nullable=False)
#     rel_category = db.Column(db.Integer, db.ForeignKey('relation.category_id'), nullable=False)

#     def __repr__(self):
#         return f"Category('{self.category_name}')"

# class SubCategory(db.Model):
#     id = db.Column(db.Integer, primary_key=True , nullable=False)
#     sub_category_name = db.Column(db.String, nullable=False)
#     rel_subcategory = db.Column(db.Integer, db.ForeignKey('relation.subcategory_id'))

#     def __repr__(self):
#         return f"Category('{self.sub_category_name}')"

# class Relation(db.Model):
#     id = db.Column(db.Integer, primary_key=True , nullable=False)
#     category_id = db.relationship('Category', backref='categories', lazy=True)
#     subcategory_id = db.relationship('SubCategory', backref='subcategories', lazy=True)

#     def __repr__(self):
#         return f"Relation('{self.category_id}')"

