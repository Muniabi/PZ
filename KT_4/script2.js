// Вариант 26: Составить программу вычисления функции y = n∑i=1 2a^2 + ((2 sini)/i^2)
var n = 5; // Заданное значение n
var a = 2; // Заданное значение a
var sum = 0;

for (var i = 1; i <= n; i++) {
    var term = 2 * Math.pow(a, 2) + (2 * Math.sin(i) / Math.pow(i, 2));
    sum += term;
}

console.log("Результат вычисления функции y: " + sum);