class Animal:
    def __init__(self, name):
        self.alive = True  # живой
        self.fed = False  # накормленный
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:
    def __init__(self, name):
        self.edible = False  # проверяем съедобность
        self.name = name


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False  # цветок не съедобен


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # фрукт съедобен

# животные
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
a3 = Predator('Бурый медведь')
a4 = Mammal('Олень Свен')
# растения
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
p3 = Fruit('Яблоко')

print(a1.name)
print(p1.name)
print(a3.name)


print(a1.alive)
print(a2.fed)
print(a4.fed)

print('Кушает:')
a1.eat(p1)
a2.eat(p2)
a4.eat(p3)

print(a1.alive)
print(a2.fed)
print(a4.fed)
