
class UrTube:
    def __init__(self):
        self.current_user = None # (текущий пользователь, User)
        self.current_password = 0
        self.current_age = 0
        self.videos = [] #(список объектов Video)
        self.users = [] #(список объектов User)

    def search_users(self, nickname, password):
        for i in self.users:
            if nickname == i.nickname and hash(password) == i.password:
                return i.nickname, i.password, i.age
        return None

    def log_in(self, nickname, password):
        self.current_user, self.current_password, self.current_age = self.search_users(nickname, password)
        if self.search_users(nickname, password) is not None:
            print(f"Пользователь {nickname} в аккаунте")

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if self.search_users(nickname, password) is not None:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(user)
            self.current_user = user.nickname

    def log_out(self):
        self.current_user = None

    def __eq__(self, other):
        return self == other

    def add_videos(self, *args):
        for video_in in args:
            if isinstance(video_in, Video) is False:
                continue
            if video_in in self.videos:
                print(f"файл \"{video_in.title}\" уже имеется")
            else:
                self.videos.append(video_in)
                print(f"файл \"{video_in.title}\" добавлен")

    def get_videos(self, search_video=""):
        result = []
        for video in self.videos:
            if search_video.upper() in video.title.upper():
                result.append(video.title)
        return result

    def watch_video(self, name_video):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        elif self.current_age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        for video in self.videos:
            if name_video == video.title:
                print("Конец видео")


class User:
    def __init__(self, nickname="", password="", age=0):
        self.nickname = nickname  # имя пользователя
        self.password = hash(password)  # в хэшированном виде, число
        self.age = age  # возраст, число


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
ur.add_videos(v1, v2, v1, 7)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.register('vasya', 'F8098FM8fjm9jmi', 22)
ur.register('vasya', 'F8098FM8fjm9jmi', 22)
ur.log_in('vasya', 'F8098FM8fjm9jmi')
print(ur.current_user)
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Для чего девушкам парень программист?')
ur.log_in('vasya', 'F8098FM8fjm9jmi')
ur.watch_video('Для чего девушкам парень программист?')
