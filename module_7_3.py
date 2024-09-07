"""
Задача "Найдёт везде"
Mother Goose - Monday’s Child.txt
Rudyard Kipling - If.txt
Walt Whitman - O Captain! My Captain!.txt
"""


class WordsFinder:
    symbol_to_delete = [',', '.', '=', '!', '?', ';', ':', ' — ']

    def __init__(self, *args):
        self.file_names = []
        for arg in args:
            self.file_names.append(arg)

    def get_all_words(self):
        all_words = dict()
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                string = file.read()
                for i in range(len(self.symbol_to_delete)):
                    string = string.replace(self.symbol_to_delete[i], ' ').lower()
                list_w = string.split()
                all_words.update({name: list_w})
        return all_words

    def find(self, word):
        dict_result = dict()
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dict_result.update({name: word})
        return dict_result

    def count(self, word):
        dict_result = dict()
        for name, words in self.get_all_words().items():
            dict_result.update({name: words.count(word.lower())})
        return dict_result

wf = WordsFinder('Mother Goose - Monday’s Child.txt',
                 'Rudyard Kipling - If.txt',
                 'Walt Whitman - O Captain! My Captain!.txt')

print(wf.find("child"))
print(wf.count("If"))


