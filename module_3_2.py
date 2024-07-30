"""
Задача "Рассылка писем"
"""
list_of_notification = ("Письмо успешно отправлено с адреса",
                        "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса",
                        "Невозможно отправить письмо с адреса",
                        "Нельзя отправить письмо самому себе!",
                        "на адрес")
templates = ("@", ".com", ".ru", ".net")
default_sender = "university.help@gmail.com"


def check_email(email):
    result = False
    list_ = email.split(templates[0])
    if len(list_) == 2:
        for i in range(1, len(templates)):
            list_ = email.split(templates[i])
            if len(list_) == 2 and list_[1] == "":
                result = True
    return result


def send_email(message="", recipient="", *, sender=default_sender):
    flag_valid_s = check_email(sender)
    flag_valid_r = check_email(recipient)
    if not flag_valid_s and not flag_valid_r:
        return
    elif not flag_valid_s and flag_valid_r:
        print(list_of_notification[2], sender, list_of_notification[4], recipient)
        return
    elif recipient == sender:
        print(list_of_notification[3])
    elif sender == default_sender:
        print(list_of_notification[0], sender, list_of_notification[4], recipient)
        return
    elif sender != default_sender:
        print(list_of_notification[1], sender, list_of_notification[4], recipient)
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

"""
Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
Нельзя отправить письмо самому себе!
"""

