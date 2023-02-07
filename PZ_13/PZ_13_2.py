def cube_elements(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        matrix[i][0] = matrix[i][0] ** 3
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = cube_elements(matrix)
print(result)

# Этот код определяет функцию cube_elements
# которая принимает в качестве аргумента список (матрицу)
# и рассчитывает количество строк и столбцов в матрице
# Затем функция возводит элементы первого столбца в куб
# Измененная матрица возвращается и выводится, чтобы показать результат