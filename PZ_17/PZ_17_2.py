# Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
# Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
# "Человек". Каждый класс должен иметь метод, который выводит информацию о
# поле объекта.

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Пол: {self.gender}")

class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age, "Мужчина")

class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name, age, "Женщина")

# Создаем объекты классов Мужчина и Женщина
man = Man("Иван", 30)
woman = Woman("Мария", 25)

# Выводим информацию о каждом человеке
print("Информация о мужчине:")
man.info()

print("\nИнформация о женщине:")
woman.info()
