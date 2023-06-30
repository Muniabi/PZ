// Вариант 24: Дано целое число, лежащее в диапазоне 1-999. Вывести его строку- описание вида «четное двузначное число», «нечетное трехзначное число» и т. д.
var number = 345; // Заданное число

var description = '';

// Проверка на четность
if (number % 2 === 0) {
    description += 'четное ';
} else {
    description += 'нечетное ';
}

// Проверка на количество знаков
if (number >= 1 && number <= 9) {
    description += 'однозначное число';
} else if (number >= 10 && number <= 99) {
    description += 'двузначное число';
} else if (number >= 100 && number <= 999) {
    description += 'трехзначное число';
}

console.log("Описание числа: " + description);
