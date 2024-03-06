
class CarMixin:
    Audi = 3500
    Bmv = 4500
    Lada = 200

    def __init__(self, name: str, drivng_experience: int):
        self.driving_experience = drivng_experience
        self.name = name

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    can_drive: bool = False

    def get_name_age(self):
        return f"{self.name}, {self.age}"

    def __post_init__(self):
        if self.age >= 18:
            self.can_drive = True


class Comparison(CarMixin):
    def __ge__(self, other):
        if isinstance(other, CarMixin):
            return self.driving_experience >= other.driving_experience
        raise ValueError()

    def __gt__(self, other):
        if isinstance(other, CarMixin):
            return self.driving_experience > other.driving_experience
        raise ValueError()

    def __eq__(self, other):
        if isinstance(other, CarMixin):
            return self.driving_experience == other.driving_experience
        raise ValueError()

    def __le__(self, other):
        if isinstance(other, CarMixin):
            return self.driving_experience <= other.driving_experience
        raise ValueError()

    def __lt__(self, other):
        if isinstance(other, CarMixin):
            return self.driving_experience < other.driving_experience
        raise ValueError()


class Balance(CarMixin):
    @property
    def balance(self):
        return f'Баланс = {self.balance}'

    @balance.setter
    def balance(self, other):
        if isinstance(other, (int, float)):
            self.balance = other
        else:
            raise TypeError

    @balance.deleter
    def balance(self):
        del self.balance


class Cart(Balance, Comparison):
    __number_of_audi_in_the_cart = 0
    __number_of_bmv_in_the_cart = 0
    __number_of_lada_in_the_cart = 0
    cost_cars_in_the_cart = 0
    number_of_cars_in_the_cart = 0
    def balance(self):
        super().balance()
        print('balance =', self.balance())
    from abc import abstractmethod

    @classmethod
    @abstractmethod
    def add_audi_in_the_cart(cls,other):
        cls.__number_of_audi_in_the_cart += other
        return cls.__number_of_audi_in_the_cart

    @classmethod
    def add_bmv_in_the_cart(cls,other):
        cls.__number_of_bmv_in_the_cart += other
        return cls.__number_of_bmv_in_the_cart

    @classmethod
    def add_lada_in_the_cart(cls,other):
        cls.__number_of_lada_in_the_cart += other
        return cls.__number_of_lada_in_the_cart

    @classmethod
    def show_cart(cls):
        number_of_cars_in_the_cart = (cls.__number_of_audi_in_the_cart +
                                      cls.__number_of_bmv_in_the_cart +
                                      cls.__number_of_lada_in_the_cart)
        cost_cars_in_the_cart = cls.Audi+cls.Bmv+cls.Lada
        return (f'Numbers of cars =  {number_of_cars_in_the_cart}',
                f'Cost of cars= {cost_cars_in_the_cart}')

    @staticmethod
    def buy():
            print('Корзина оплачена')



class CarDealership(Cart):
    def __call__(self):
        return f'Имя {self.name}', f'Стаж вождения (лет) {self.driving_experience} '


client1 = CarDealership('Danil', 2)
client2 = CarDealership('Vlad', 4)
kirill = Person("kirill", 22)
print(kirill.can_drive)
print(client1.driving_experience == client2.driving_experience)
client1.add_audi_in_the_cart(1)
client1.add_bmv_in_the_cart(2)
print(client1.show_cart())
client1.balance = 300
print(client1.balance)
client1.buy()
print(client1())

