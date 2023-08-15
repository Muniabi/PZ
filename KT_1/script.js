// Вариант 24 Составить программу вычисления функции: Y = x^2 + 2x + 3
function calculateY(x) {
    return Math.pow(x, 2) + (2 * x) + 3;
}

// Пример
let x = 5;
let result = calculateY(x);
console.log("Результат вычисления функции Y: " + result);