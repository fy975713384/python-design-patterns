# -*- coding: utf-8 -*-
"""
通过装饰器实现单例模式
"""

# 使用函数装饰器实现单例


def singleton(cls):
    _instance = {}

    def inner(*arg, **kw):
        if cls not in _instance:
            _instance[cls] = cls(*arg, **kw)
        return _instance[cls]

    return inner


@singleton
class Cls:
    def __init__(self):
        pass


cls1 = Cls()
cls2 = Cls()
print(id(cls1) == id(cls2))

# 使用类装饰器实现单例


class Singleton():
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class Cls1:
    def __init__(self):
        pass


cls1 = Cls1()
cls2 = Cls1()
print(id(cls1) == id(cls2))


class Cls2:
    def __init__(self):
        pass


cls3 = singleton(Cls2)
cls4 = singleton(Cls2)
print(id(cls2) == id(cls2))
