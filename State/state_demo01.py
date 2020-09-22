# -*- coding: utf-8 -*-

"""
状态模式
"""

from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass


class ConcreteStateB(State):
    def handle(self):
        print('ConcreteStateB')


class ConcreteStateA(State):
    def handle(self):
        print('ConcreteStateA')


class Context(State):
    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def handle(self):
        self.state.handle()


if __name__ == '__main__':
    context = Context()
    stateA = ConcreteStateA()
    stateB = ConcreteStateB()

    context.set_state(stateA)
    context.handle()
