example = 'Топинамбур'
print(example[0]) #Выведите первый символ.
print(example[-1])#Выведите последний символ (используя отрицательный индекс).
# halfWord = len(example)/2
# print("len", len(example), "halfWord", halfWord, "round", round(halfWord))
# Выведите вторую половину этой строки (С нечётным количеством символов)
print(example[round(len(example)/2) - (not bool((len(example)/2) % 2)):])
print(example[::-1])#Выведите строку наоборот
print(example[1::2])#Выведите каждый второй символ этой строки