# перезаписали все по принципу "Liskov substitution", принцип которого заключается в том. что наследуемый класс должен
# взаимозаменяем с родительским классом


class Animal:                                             # перзаписали класс, задав в него аргументы имя и возраст
    def __init__(self, name, age):
        self.attributes = {'name': name, 'age': age}

    def eat(self, _amount=0):                             # добавили в метод еще один аргумент по умолчанию, чтобы
        print("Ate some food!")                           # везде было по 2 аргумента


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self, amount=0.1):
        if amount > 0.3:
            print("Can't eat that much!")
        else:
            print("Ate some cat food!")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self, _amount=0):
        print("Ate some dog food!")


pluto = Dog('Pluto', 3)                                    # перезаписали, чтобы можно было везде одинаково задать
goofy = Dog('Goofy', 2)                                    # аргументы
buttons = Cat('Mr. Buttons', 4)

animals = (pluto, goofy, buttons)

for animal in animals:
    if animal.attributes['age'] > 2:
        print(animal.attributes['name'])
