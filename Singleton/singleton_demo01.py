# -*- coding: utf-8 -*-

"""
单例模式的经典实现方式
注意事项：该单例类的所有后代类均会继承单例特性
"""


class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print("Object created", s)
s1 = Singleton()
print("Object created", s1)
