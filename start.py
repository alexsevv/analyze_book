from collections import Counter

#менеджер контекста with as закроет файл автоматически
with open('book.txt', 'r') as file:
    my_line = [line.strip() for line in file]
    string = " ".join(my_line)

#метод подсчета количества вхождений символов в тексте написанный вручную
def count_letters2(text):
    my_string = text.replace(" ", "").lower()
    dict_symbols = {}
    for symbol in my_string:
        if symbol not in dict_symbols:
            dict_symbols[symbol] = my_string.count(symbol)

    sort_dict = dict(sorted(dict_symbols.items(), key=lambda item: -item[1]))
    print (len(sort_dict))
    for key in sort_dict.keys():
        print(f"Количество вхождений символа  {key}  - {sort_dict[key]}")


#метод для подсчета вхождений символов в тексте с помощью библиотеки
def dict_symbols(text):
    #убираем пробелы
    string = " ".join(text.split()).lower()
    #делаем массив
    symbols = string.split()
    new_symbols = " ".join(string.split()).replace(" ", "")

    sort_dict = Counter(new_symbols)

    sort_dict_new = dict(sorted(sort_dict.items(), key=lambda item: -item[1]))
    print (len(sort_dict_new))
    for key in sort_dict_new.keys():
        print(f"Количество вхождений  {key}  - {sort_dict[key]}")

count_letters2(string)
print (" ")
dict_symbols(string)
