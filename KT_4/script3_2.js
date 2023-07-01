// Вариант 25: Создать одномерный массив на семь элементов. Найти сумму кубов элементов массива. Результат вывести в консоль.
let array = [1, 2, 3, 4, 5, 6, 7];
let sumOfCubes = 0;

for (let i = 0; i < array.length; i++) {
    let cube = Math.pow(array[i], 3);
    sumOfCubes += cube;
}

console.log("Сумма кубов элементов массива: " + sumOfCubeslet)