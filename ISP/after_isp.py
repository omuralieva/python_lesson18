# перезаписали все по принципу "interface segregation", принцип которого заклчается в том, что много интерфейсов
# специально предназначенных для клиентов, лучше чем один интерфейс общего назначения, т.е. клиент не должен включать
# в себя методы, которые он не использует


class Creature:
    def __init__(self, name):
        self.name = name


class SwimmerInterface:                        # создали несколько подклассов и разделили методы, поместив их
    def swim(self):                            # в эти подклассы, чтобы можно было клиентам наследоваться от
        pass                                   # от нескольких подклассов


class WalkerInterface:
    def walk(self):
        pass


class TalkerInterface:
    def talk(self):
        pass


class Human(Creature, SwimmerInterface, WalkerInterface, TalkerInterface):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")

    def walk(self):
        print(f"I'm {self.name} and I can walk")

    def talk(self):
        print(f"I'm {self.name} and I can talk")


class Fish(Creature, SwimmerInterface):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")


class Cat(Creature, SwimmerInterface, WalkerInterface):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")

    def walk(self):
        print(f"I'm {self.name} and I can walk")


human = Human("John Doe")                                  # задали аргументы в классах и вызвали методы
human.swim()
human.walk()
human.talk()

fish = Fish("Nemo")
fish.swim()

cat = Cat("Mr. Buttons")
cat.walk()
cat.swim()
