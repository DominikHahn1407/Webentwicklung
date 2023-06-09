class VideoController:

    def __init__(self, app, res):
        self.app = app
        self.res = res

        self.app.add_route("/videos", self.res, suffix="videos")
        self.app.add_route("/video/{vnr}", self.res, suffix="video")
        self.app.add_route("/video", self.res, suffix="video")
        self.app.add_route("/videosbygenre/{genre}", self.res, suffix="videosbygenre")
        self.app.add_route("/videosbyagerating/{age_rating}", self.res, suffix="videosbyagerating")
        self.app.add_route("/videogenres", self.res, suffix="videogenres")
        self.app.add_route("/videonumbers", self.res, suffix="videonumbers")

        # self.app.add_static_route('/', 'C:/Users/ZBook/OneDrive/Studium/Dozent/Webentwicklung/Übungen/Rest-API')
        self.app.add_static_route('/', 'C:/Users/Dominik Hahn/OneDrive/Studium/Dozent/Webentwicklung/Übungen/Rest-API')

