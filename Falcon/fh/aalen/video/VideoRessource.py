import json
import falcon

from fh.aalen.video.VideoService import VideoService


class VideoRessource:
    def on_get_videos(self, req, resp):
        video_list = VideoService.get_videos()
        resp.text = json.dumps([v.to_dict() for v in video_list], ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

    def on_get_video(self, req, resp, vnr):
        resp.text = None
        v = VideoService.get_video(int(vnr))
        resp.text = json.dumps(v.to_dict(), ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

    def on_get_videosbygenre(self, req, resp, genre):
        video_list = VideoService.get_videos_by_genre(genre)
        resp.text = json.dumps([v.to_dict() for v in video_list], ensure_ascii=False, indent=2)

    def on_get_videosbyagerating(self, req, resp, age_rating):
        video_list = VideoService.get_videos_by_age_rating(age_rating)
        resp.text = json.dumps([v.to_dict() for v in video_list], ensure_ascii=False, indent=2)

    def on_get_videogenres(self, req, resp):
        genre_list = VideoService.get_video_genres()
        result = [dict(row) for row in genre_list]
        resp.text = json.dumps(result, ensure_ascii=False, indent=2)

    def on_post_video(self, req, resp):
        video_json = json.load(req.bounded_stream)
        VideoService.create_video(video_json)
        resp.text = "Video added successfully"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_put_video(self, req, resp, vnr):
        video_json = json.load(req.bounded_stream)
        VideoService.update_video(int(vnr), video_json)
        resp.text = f"Video with the ID {vnr} updated successfully!"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_delete_video(self, req, resp, vnr):
        VideoService.delete_video(int(vnr))
        resp.text = f"Video with the ID {vnr} deleted successfully!"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT
