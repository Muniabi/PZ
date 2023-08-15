// Вариант 26: Составить программу вычисления функции y = n∑i=1 2a^2 + ((2 sini)/i^2)
let n = 5;
let a = 2;
let sum = 0;

for (let i = 1; i <= n; i++) {
    let term = 2 * Math.pow(a, 2) + (2 * Math.sin(i) / Math.pow(i, 2));
    sum += term;
}

console.log("Результат вычисления функции y: " + sum);