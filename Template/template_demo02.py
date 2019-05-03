# -*- coding: utf-8 -*-

"""
模板方法模式
"""
from abc import ABCMeta, abstractmethod


class AbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operation_1(self):
        pass

    @abstractmethod
    def operation_2(self):
        pass

    def template_method(self):
        print('Defining the Algorithm. Operational follows Operation2')
        self.operation_2()
        self.operation_1()


class ConcreteClass(AbstractClass):
    def operation_1(self):
        print('My Concrete Operation1')

    def operation_2(self):
        print('Operation 2 remains same')


class Client:
    def main(self):
        self.concreate = ConcreteClass()
        self.concreate.template_method()


if __name__ == '__main__':
    client = Client()
    client.main()
