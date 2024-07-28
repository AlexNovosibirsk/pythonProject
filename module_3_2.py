
list_of_notification = ("Письмо успешно отправлено с адреса",
                        "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса",
                        "Невозможно отправить письмо с адреса",
                        "Нельзя отправить письмо самому себе!",
                        "на адрес")
templates = ("@", ".com", ".ru", ".net")


def check_email(email):
    if templates[0] in email:
        for i in templates:
            if email.endswith(i):
                return True
    else:
        return False


def send_email(message="", recipient="", *, sender="university.help@gmail.com"):
    index = 0
    flag_valid_s = check_email(sender)
    flag_valid_r = check_email(recipient)
    if flag_valid_r and flag_valid_s:
        if recipient != sender and sender == "university.help@gmail.com":
            index = 0
        elif recipient != sender and sender != "university.help@gmail.com":
            index = 1
        elif recipient == sender:
            index = 3
    elif not flag_valid_s and flag_valid_r:
        index = 2

    print(list_of_notification[index], sender, list_of_notification[4], recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

"""
Пример выполняемого кода (тесты):
1. send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
2. send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
3. send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
4. send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

Вывод на консоль:
1. Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
2. НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
3. Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
4. Нельзя отправить письмо самому себе!
"""

