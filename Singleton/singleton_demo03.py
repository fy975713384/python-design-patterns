# -*- coding: utf-8 -*-

"""
Monostate （单态）模式
"""


class Borg:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj

    def __int__(self):
        self.x = 0
        self.y = 0


b = Borg()
b1 = Borg()
b.x = 1
b1.y = 2

print(f'Borg Object "b": {b}')
print(f'Borg Object "b1": {b1}')
print(f'Object State "b": {b.__dict__}')
print(f'Object State "b1": {b1.__dict__}')
