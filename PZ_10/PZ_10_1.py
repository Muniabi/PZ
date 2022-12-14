try:
    magistr = {'Лермонтов','Достоевский','Пушкин','Тютчев'}
    bookhouse = {'Толстой','Грибоедов','Чехов','Пушкин'}
    gallery = {'Чехов','Тютчев','Пушкин'}
    print("Книги есть во всех магазинах ", magistr & bookhouse & gallery)
    print("Полный список всех книг", magistr | bookhouse | gallery)
    print("Есть не во всех магазинах", magistr - bookhouse - gallery)
except:
    print("Что-то не так")