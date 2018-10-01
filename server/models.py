from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Video(db.Model):
    
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(150), nullable=False)
    view_count = db.Column(db.Integer, default=0)
    like_count = db.Column(db.Integer, default=0)
    code = db.Column(db.String, unique=True, nullable=False)
    thumb = db.Column(db.String(300))
    show_time = db.Column(db.DateTime, nullable=False)
    hide_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Video %r>' % self.title

    def as_dict(self):
       return {i.name: getattr(self, i.name) for i in self.__table__.columns}