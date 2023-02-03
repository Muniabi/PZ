# записываем числа в первый файл
with open("first_file.txt", "w") as file:
    file.write("1\n2\n-3\n4\n")

# записываем числа во второй файл
with open("second_file.txt", "w") as file:
    file.write("2\n-1\n5\n-3\n")

# обрабатка чисел в двух файлах
with open("first_file.txt") as first_file, open("second_file.txt") as second_file:
    first_numbers = set(map(int, first_file.read().split()))
    second_numbers = set(map(int, second_file.read().split()))
    only_in_first = first_numbers - second_numbers
    only_in_second = second_numbers - first_numbers
    all_numbers = first_numbers.union(second_numbers)

# записываем обработанные числа в третий файл
with open("third_file.txt", "w") as file:
    file.write("Элементы в первом файле, которых нет во втором:\n")
    file.write(" ".join(map(str, only_in_first)))
    file.write("\nЭлементы во втором файле, которых нет в первом:\n")
    file.write(" ".join(map(str, only_in_second)))
    file.write("\nВсе элементы:\n")
    file.write(" ".join(map(str, all_numbers)))
    file.write("\nКоличество элементов: " + str(len(all_numbers)))
    file.write("\nИндекс первого минимального элемента: " + str(min(all_numbers)))
    file.write("\nИндекс последнего максимального элемента: " + str(max(all_numbers)))