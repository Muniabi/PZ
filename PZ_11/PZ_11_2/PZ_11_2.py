punctuation = ".,;:!?"

# подсчитываем знаки препинания в файле
with open("text18-26.txt", "r") as file:
    content = file.read()
    punctuation_count = sum(char in punctuation for char in content)

# выводим содержимое файла и количество знаков препинания
print("Содержимое файла:\n" + content)
print("Количество знаков пунктуации:", punctuation_count)

# заменяем знаки препинания на '/' и сохраняем в новый файл
with open("text18-26_poetic.txt", "w") as file:
    content = content.translate(str.maketrans(punctuation, "/" * len(punctuation)))
    file.write(content)
