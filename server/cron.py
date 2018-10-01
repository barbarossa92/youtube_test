import requests
from models import Video, db
from datetime import datetime, timedelta
from app import YOUTUBE_API_KEY, app
import schedule, time


def get_videos_from_youtube():
    with app.app_context():
        youtube_api = "https://www.googleapis.com/youtube/v3/"
        videos_url = youtube_api + 'search?key={key}&q={q}&part=id,snippet&maxResults=50&order=date'
        statistic_url = youtube_api + "videos?part=statistics,id&id={video_ids}&key={key}"
        search_query = "gta 5"
        response = requests.get(videos_url.format(key=YOUTUBE_API_KEY, q=search_query))
        if response.status_code == 200:
            videos_data = response.json()
            videos = videos_data.get("items", [])
            videos_ids = [i["id"]["videoId"] for i in videos if i.get("id") and i["id"].get("videoId")]
            resp = requests.get(statistic_url.format(video_ids=",".join(videos_ids), key=YOUTUBE_API_KEY))
            if resp.status_code == 200:
                statistics = resp.json()["items"]
                for video in videos:
                    for stat in statistics:
                        if video.get("id") and video["id"].get("videoId") and stat.get("id"):
                            if video["id"]["videoId"] == stat["id"] and not Video.query.filter_by(code=stat["id"]).one_or_none():
                                video_obj = Video()
                                snippet = video.get("snippet")
                                video_obj.title = snippet.get("title") if snippet else None
                                if snippet.get("thumbnails") and snippet["thumbnails"].get("high") and snippet["thumbnails"]["high"].get("url"):
                                    video_obj.thumb = snippet["thumbnails"]["high"]["url"]
                                video_obj.code = stat["id"]
                                vid_stat = stat.get("statistics")
                                video_obj.view_count = vid_stat.get("viewCount")
                                video_obj.like_count = vid_stat.get("likeCount")
                                video_obj.show_time = datetime.now()
                                video_obj.hide_time = datetime.now() + timedelta(minutes=30)
                                db.session.add(video_obj)
                db.session.commit()
                print("OK")
                return "OK"
            print(response.json())
        return "Not ok"


schedule.every(1).minutes.do(get_videos_from_youtube)

def run_cron():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":  
    run_cron()