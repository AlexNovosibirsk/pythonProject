num = "FWSERSg3h6w45ybuu655~67^"
hash_value = hash(num)

print(hash_value)


class UrTube:
    def __init__(self, user=None):
        self.current_user = user # (текущий пользователь, User)
        self.videos = [] #(список объектов Video)
        self.users = [] #(список объектов User)
        pass

    def log_in(self, nickname, password):
        pass

    def register(self, nickname, password, age):
        pass

    def log_out(self):
        pass

    def add(self, *args):
        for video in args:
            self.videos.append(video)

    def get_videos(self, search_video=""):
        result = []
        for video in self.videos:
            if search_video.upper() in video.title.upper():
                result.append(video.title)
        return result

    def watch_video(self, name_video):
        pass


class User:
    def __init__(self):
        self.nickname = ""  # имя пользователя
        self.password = 0  # в хэшированном виде, число
        self.age = 0  # возраст, число


class Video:

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, title="", duration=0, time_now=0, adult_mode=False):
        self.title = title  # (заголовок, строка)
        self.duration = duration  # (продолжительность, секунды)
        self.time_now = time_now  # (секунда остановки(изначально 0))
        self.adult_mode = adult_mode  # (ограничение по возрасту)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
