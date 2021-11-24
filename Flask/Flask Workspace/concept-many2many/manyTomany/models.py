from manyTomany import db

subs = db.Table('subs',
                db.Column('user.id', db.Integer,
                          db.ForeignKey('user.user_id')),
                db.Column('channel_id', db.Integer,
                          db.ForeignKey('channel.channel_id'))
                )


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    subscriptions = db.relationship(
        'Channel', secondary='subs', backref=db.backref('subscribers', lazy='dynamic'))


class Channel(db.Model):
    channel_id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String(20))
