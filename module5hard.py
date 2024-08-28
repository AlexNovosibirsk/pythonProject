"""
Задание "Свой YouTube"
"""
import time

class UrTube:

    def __init__(self):
        self.current_User_Object = None  # (текущий пользователь, User)
        self.current_user = ""    # (текущий пользователь, NickName)
        self.videos = []          # (список объектов Video)
        self.users  = []          # (список объектов User)

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_User_Object = user
                self.current_user = user.nickname
                break

    def register(self, nickname, password, age):
        flag_search = False
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                flag_search = True
                break
        if not flag_search:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_User_Object = new_user
            self.current_user = nickname

    def add_videos(self, *args):
        for new_video in args:
            if isinstance(new_video, Video) is False:
                continue
            elif self.__contains__(new_video):
                continue
            else:
                self.videos.append(new_video)

    def __contains__(self, new_video):
        return new_video in self.videos

    def get_videos(self, search_video=""):
        result = []
        for video in self.videos:
            if search_video.upper() in video.title.upper():
                result.append(video.title)
        return result

    def search_video(self, name_video):
        for video in self.videos:
            if name_video == video.title:
                return video
        return None

    def watch_video(self, name_video):
        if self.current_User_Object is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        video = self.search_video(name_video)
        if video:
            if video.adult_mode and self.current_User_Object.age < 18:
                print(f"{self.current_user}, Вам нет 18 лет, пожалуйста покиньте страницу")
            else:
                print(f"{self.current_user} смотрит \"{name_video}\",", end=" ")
                for video.time_now in range(1, video.duration + 1):
                    time.sleep(0.1)
                    print(video.time_now, end=" ")
                print("Конец видео")

    def log_out(self):
        self.current_user = None


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname        # имя пользователя
        self.password = hash(password)  # в хэшированном виде, число
        self.age = age                  # возраст, число


class Video:

    def __init__(self, title="", duration=0, adult_mode=False):
        self.title = title  # (заголовок, строка)
        self.duration = duration  # (продолжительность, секунды)
        self.adult_mode = adult_mode  # (ограничение по возрасту)
        self.time_now = 0  # (секунда остановки(изначально 0))

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


ur = UrTube()
ur.register('urban_pythonist25', 'iScX4vIJClb9YQavjAgF', 25)
ur.register('vasya22', 'F8098FM8fjm9jmi', 22)
ur.register('petya12', 'lolkekcheburek', 12)
ur.register('urban_pythonist25', 'iScX4vIJClb9YQavjAgF', 25)
ur.register('anna17', 'dsfgj674jghm', 17)
ur.register('vlad20', 'srtj123jtynz', 20)

# Добавление видео
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Физика для всех', 17)
# print(repr(v1))
ur.add_videos(v1, "abc", v2, v1, 7)
ur.add_videos(v3)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка входа в другой аккаунт
ur.register('petya12', 'F8098FM8fjm9jmi', 55)

ur.log_out()
print(ur.current_user)
ur.log_in('petya12', 'lolkekcheburek')
ur.watch_video('Физика для всех')
ur.watch_video('Для чего девушкам парень программист?')
print(ur.current_user)


