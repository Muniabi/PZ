// Вариант 26: Составить программу вычисления функции: y=x^2 -1,еслиX≤-6,  y= 8+x,еслиX >-6
function calculateY(x) {
    if (x <= -6) {
        return Math.pow(x, 2) - 1;
    } else {
        return 8 + x;
    }
}

// Пример
var x = -8;
var result = calculateY(x);
console.log("Результат вычисления функции Y: " + result);