import string

# читаем содержимое текстового файла
with open("text18-26.txt", "r") as file:
    text = file.read()

# считаем количество знаков препинания
punctuation_count = sum(char in string.punctuation for char in text)

# Заменяем все знаки препинания на '/'
new_text = text.translate(str.maketrans("", "", string.punctuation)).replace(" ", "/")

# Записываем измененный текст в новый файл
with open("new_file.txt", "w") as file:
    file.write(new_text)

# выводим содержимое текстового файла и количество знаков препинания
print(text)
print("количество знаков пунктуации:", punctuation_count)
