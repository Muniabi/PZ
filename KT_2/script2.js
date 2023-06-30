// вариант 26: Составить программу вычисления функции: y=2 - x, еслиX <-7,   y= 4x, если -7 ≤ x ≤ 1,   y = 9-х^2,еслиX >1
function calculateY(x) {
    if (x < -7) {
        return 2 - x;
    } else if (x >= -7 && x <= 1) {
        return 4 * x;
    } else {
        return 9 - Math.pow(x, 2);
    }
}

// Пример использования функции
var x = 2; // Задайте значение переменной x, для которого нужно вычислить Y
var result = calculateY(x);
console.log("Результат вычисления функции Y: " + result);
