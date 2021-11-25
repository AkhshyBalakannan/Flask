from miniProjectBackend import db


relation = db.Table('relation',
                db.Column('movie_id', db.Integer,
                          db.ForeignKey('movie.movie_id')),
                db.Column('seat_id', db.Integer,
                          db.ForeignKey('seats.seat_id'))
                )


class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(20))
    seats_alloated = db.relationship(
        'Seats', secondary='relation', backref=db.backref('movies_seat', lazy='dynamic'))


class Seats(db.Model):
    seat_id = db.Column(db.Integer, primary_key=True)
    seat_type = db.Column(db.String(20))
