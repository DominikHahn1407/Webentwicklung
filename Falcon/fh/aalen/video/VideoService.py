from fh.aalen.video.Video import Video
from fh.aalen.data.db_session import DBSession


class VideoService:
    @classmethod
    def __json_to_video(cls, video, json_video):
        video.title = json_video["title"]
        video.age_rating = json_video["age_rating"]
        video.description = json_video["description"]
        video.genre = json_video["genre"]
        return video

    @classmethod
    def get_videos(cls):
        session = DBSession.get_session()
        video_list = session.query(Video).all()
        return video_list

    @classmethod
    def get_video(cls, vnr):
        session = DBSession.get_session()
        video = session.query(Video).get(int(vnr))
        return video

    @classmethod
    def get_videos_by_genre(cls, genre):
        session = DBSession.get_session()
        videos = session.query(Video).filter(Video.genre==genre)
        return videos

    @classmethod
    def get_videos_by_age_rating(cls, age_rating):
        session = DBSession.get_session()
        videos = session.query(Video).filter(Video.age_rating==age_rating)
        return videos

    @classmethod
    def get_video_genres(cls):
        session = DBSession.get_session()
        genres = session.query(Video.genre).all()
        return genres

    @classmethod
    def create_video(cls, json_video):
        video = Video()
        video = cls.__json_to_video(video, json_video)
        session = DBSession.get_session()
        session.add(video)
        session.commit()

    @classmethod
    def update_video(cls, vnr, json_video):
        session = DBSession.get_session()
        video = session.query(Video).get(int(vnr))
        cls.__json_to_video(video, json_video)
        session.commit()

    @classmethod
    def delete_video(cls, vnr):
        session = DBSession.get_session()
        video = session.query(Video).get(int(vnr))
        session.delete(video)
        session.commit()

