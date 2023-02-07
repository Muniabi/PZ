def average_positive_elements(matrix): # объявление функции average_positive_elements с аргументом matrix
    positive_elements = [element for row in matrix for element in row if element > 0] # создание списка positive_elements, состоящего из элементов element, удовлетворяющих условию element > 0, для каждой строки row в матрице matrix
    average = sum(positive_elements) / len(positive_elements) if positive_elements else 0 # вычисление среднего арифметического положительных элементов, если список positive_elements не пуст, иначе значение 0
    return average # возвращение результата функции, т.е. среднего арифметического положительных элементов

matrix = [[1, -2, 3], [4, 5, -6], [7, 8, 9]] # определение матрицы matrix
result = average_positive_elements(matrix) # вызов функции average_positive_elements с аргументом matrix и присваивание результата переменной result
print(result) # вывод результата на экран






