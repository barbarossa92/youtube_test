from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from models import db, Video
from datetime import datetime

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)
YOUTUBE_API_KEY = "AIzaSyCgP4gCtfsy8ppaiVr5zmWH615RLTmkRNM"

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'youtube_db',
    'host': 'db',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)


@app.route('/videos', methods=['GET'])
def get_videos():
    with app.app_context():
        sorting = request.args.get("sort")
        now = datetime.now()
        videos = Video.query.filter(Video.show_time <= now).filter(Video.hide_time >= now)
        if sorting == "likes":
            return jsonify({"videos": [video.as_dict() for video in videos.order_by(Video.like_count.desc())]})
        elif sorting == "views":
            return jsonify({"videos": [video.as_dict() for video in videos.order_by(Video.view_count.desc())]})
        return jsonify({"videos": [video.as_dict() for video in videos.all()]})




if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port="5000")