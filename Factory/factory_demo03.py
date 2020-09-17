# -*- coding: utf-8 -*-

"""
抽象工厂模式
"""

from abc import ABCMeta, abstractmethod


# AbstractFactory
class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_non_veg_pizza(self):
        pass


# ConcreteFactory
class IndianPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return DeluxeVeggiePizza()

    def create_non_veg_pizza(self):
        return ChickenPizza()


# ConcreteFactory
class USPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return MexicanVegPizza()

    def create_non_veg_pizza(self):
        return HamPizza()


# AbstractProduct
class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        pass


# AbstractProduct
class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, veg_pizza):
        pass


# ConcreteProduct
class DeluxeVeggiePizza(VegPizza):
    def prepare(self):
        print(f'Prepare {type(self).__name__}')


# ConcreteProduct
class MexicanVegPizza(VegPizza):
    def prepare(self):
        print(f'Prepare {type(self).__name__}')


# ConcreteProduct
class ChickenPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print(
            f'{type(self).__name__} is served with Chicken on {type(veg_pizza).__name__}')


# ConcreteProduct
class HamPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print(f'{type(self).__name__} is served with Ham on {type(veg_pizza).__name__}')


class PizzaStore:
    def __init__(self):
        pass

    def make_pizza(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.non_veg_pizza = self.factory.create_non_veg_pizza()
            self.veg_pizza = self.factory.create_veg_pizza()
            self.veg_pizza.prepare()
            self.non_veg_pizza.serve(self.veg_pizza)


pizza = PizzaStore()
pizza.make_pizza()
