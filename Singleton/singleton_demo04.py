# -*- coding: utf-8 -*-

"""
Monostate （单态）模式
"""


class Borg:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        print(id(obj.__dict__))
        obj.__dict__ = cls.__shared_state  # 将不同实例的 __dict__ 指向同一地址
        print(id(obj.__dict__))
        return obj

    def __int__(self):
        self.x = 0
        self.y = 0


b1 = Borg()
b2 = Borg()
b1.x = 1
b2.y = 2

print(f'Borg Object "b1": {b1}')
print(f'Borg Object "b2": {b2}')
print(f'Object State "b1": {b1.__dict__}')
print(f'Object State "b2": {b2.__dict__}')
