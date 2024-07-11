import json


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} Звучит")

    def eat(self):
        print(f"{self.name} ест")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "age": self.age
        }


class Bird(Animal):
    def __init__(self, name, age, wing_size):
        super().__init__(name, age)
        self.wing_size = wing_size

    def make_sound(self):
        print(f"{self.name} Поёт")

    def eat(self):
        print(f"{self.name} Клюёт")

    def to_dict(self):
        data = super().to_dict()
        data["wing_size"] = self.wing_size
        return data


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} Рычит")

    def eat(self):
        print(f"{self.name} Грызёт")

    def to_dict(self):
        data = super().to_dict()
        data["fur_color"] = self.fur_color
        return data


class Reptile(Animal):
    def __init__(self, name, age, tail_size):
        super().__init__(name, age)
        self.tail_size = tail_size

    def make_sound(self):
        print(f"{self.name} шипит")

    def eat(self):
        print(f"{self.name} глотает")

    def to_dict(self):
        data = super().to_dict()
        data["tail_size"] = self.tail_size
        return data


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name
        }


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name
        }


class Zoo:
    def __init__(self, name):
        self.animals = []
        self.staff = []
        self.name = name

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def show_animals(self):
        print(f"Животные в зоопарке {self.name}:")
        for animal in self.animals:
            print(f"{animal.name}, возраст {animal.age}")

    def show_staff(self):
        for staff in self.staff:
            print(f"{staff.name}, должность: {staff.__class__.__name__}")

    def save_to_file(self, filename):
        zoo_data = {
            "name": self.name,
            "animals": [animal.to_dict() for animal in self.animals],
            "staff": [staff.to_dict() for staff in self.staff]
        }
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(zoo_data, file, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            zoo_data = json.load(file)
            self.name = zoo_data["name"]
            self.animals = []
            for animal_data in zoo_data["animals"]:
                animal_type = animal_data["type"]
                if animal_type == "Bird":
                    self.animals.append(Bird(animal_data["name"], animal_data["age"], animal_data["wing_size"]))
                elif animal_type == "Mammal":
                    self.animals.append(Mammal(animal_data["name"], animal_data["age"], animal_data["fur_color"]))
                elif animal_type == "Reptile":
                    self.animals.append(Reptile(animal_data["name"], animal_data["age"], animal_data["tail_size"]))
            self.staff = []
            for staff_data in zoo_data["staff"]:
                staff_type = staff_data["type"]
                if staff_type == "ZooKeeper":
                    self.staff.append(ZooKeeper(staff_data["name"]))
                elif staff_type == "Veterinarian":
                    self.staff.append(Veterinarian(staff_data["name"]))


def animal_sounds(animals):
    print(f"\nЗвуки животных в зоопарке:")
    for animal in animals:
        animal.make_sound()


# Пример использования

zoo = Zoo('ZooLand')

zoo.add_animal(Bird("Гусь", 2, "10 см"))
zoo.add_animal(Mammal("Кот", 3, "Чёрный"))
zoo.add_animal(Reptile("Змея", 2, "100 см"))

zoo.add_staff(ZooKeeper("Вася"))
zoo.add_staff(Veterinarian("Пётр Михалыч"))

zoo.show_animals()

animal_sounds(zoo.animals)

# Сохранение информации о зоопарке в файл
zoo.save_to_file("zoo_info.json")

# Загрузка информации о зоопарке из файла
new_zoo = Zoo("")
new_zoo.load_from_file("zoo_info.json")
new_zoo.show_animals()
new_zoo.show_staff()
