# -*- coding: utf-8 -*-

"""
单例模式的懒汉式实例化
"""


class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called..")
        else:
            print("Instance already created:", self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()
print('Object created', Singleton.get_instance())
s1 = Singleton()
