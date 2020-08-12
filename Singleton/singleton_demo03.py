# -*- coding: utf-8 -*-

"""
基于元类的单例模式
"""


# metaclass 必须继承 type
class MetaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(
                MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
print(logger1, logger2, sep='\n')
