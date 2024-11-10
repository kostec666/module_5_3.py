class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # Имя дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует.")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

# Примеры использования класса House
h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Горский', 30)
h3 = House('Домик в деревне', 2)

# Сравнения
print(h1 == h2)  # True
print(h1 != h3)  # True
print(h1 < h3)   # False
print(h1 > h2)   # False
print(h1 >= h2)  # True
print(h1 <= h3)  # False



