"""
Задача "Однокоренные":
Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word,
а далее неограниченную последовательность в параметр *other_words.
Функция должна составить новый список same_words только из тех слов списка other_words,
которые содержат root_word или наоборот root_word содержит одно из этих слов.
После вернуть список same_words в качестве результата своей работы.
"""


def single_root_words(root_word, *other_words):
    set_ = set()
    same_words = []
    for tuple_ in other_words:
        txt = str(tuple_)
        if txt.upper() in root_word.upper():
            same_words.append(txt)
            set_.add(txt)
        if root_word.upper() in txt.upper():
            same_words.append(txt)
            set_.add(txt)
    return set_, same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
# немного изменим входные данные - 'rich' присутствует и слева и справа
result3 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies', 'rich')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result3)
print(result2)

"""
результат выведем двумя коллекциями 
({'richies', 'orichalcum', 'richiest'}, ['richiest', 'orichalcum', 'richies'])

({'richies', 'orichalcum', 'rich', 'richiest'}, ['richiest', 'orichalcum', 'richies', 'rich', 'rich'])

({'Able', 'Disable'}, ['Able', 'Disable'])
"""