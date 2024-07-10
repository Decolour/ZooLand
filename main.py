class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} Звучит")

    def eat(self):
        print(f"{self.name} ест")


class Bird(Animal):
    def __init__(self, name, age, wing_size):
        super().__init__(name, age)
        self.wing_size = wing_size

    def make_sound(self):
        print(f"{self.name} Поёт")

    def eat(self):
        print(f"{self.name} Клюёт")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} Рычит")

    def eat(self):
        print(f"{self.name} Грызёт")


class Reptile(Animal):
    def __init__(self, name, age, tail_size):
        super().__init__(name, age)
        self.tail_size = tail_size

    def make_sound(self):
        print(f"{self.name} шипит")

    def eat(self):
        print(f"{self.name} глотает")


class Zoo():
    def __init__(self, name):
        self.animals = []
        self.staff = []
        self.name = name

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def show_animals(self):
        print(f"Животные в зоопарке {zoo.name}:")
        for animal in self.animals:
            print(f"{animal.name}, возраст {animal.age}")

    def show_staff(self):
        for staff in self.staff:
            print(f"{staff.name}, должность: {staff.__class__.__name__}")


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")


zoo = Zoo('ZooLand')

zoo.add_animal(Bird("Гусь", 2, "10 см"))
zoo.add_animal(Mammal("Кот", 3, "Чёрный"))
zoo.add_animal(Reptile("Змея", 2, "100 см"))

zoo.add_staff(ZooKeeper("Вася"))
zoo.add_staff(Veterinarian("Пётр Михалыч"))

zoo.show_animals()


def animal_sounds(animals):
    print(f"\nЗвуки животных в зоопарке {zoo.name}:")
    for animal in animals:
        animal.make_sound()


animal_sounds(zoo.animals)
