# -*- coding: utf-8 -*-

"""
现实世界的状态模式
"""


class ComputerState:
    name = 'State'
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print(f'Current: {self} => switched to new state {state}')
            self.__class__ = state
        else:
            print(f'Current: {self} => switched to {state.name} not possible')

    def __str__(self):
        return self.name


class Off(ComputerState):
    name = 'off'
    allowed = ['on']


class On(ComputerState):
    name = 'on'
    allowed = ['off', 'suspend', 'hibernate']


class Suspend(ComputerState):
    name = 'suspend'
    allowed = ['on']


class Hibernate(ComputerState):
    name = 'hibernate'
    allowed = ['on']


class Computer:
    def __init__(self, model='HP'):
        self.mode = model
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


if __name__ == '__main__':
    comp = Computer()
    # Switch on
    comp.change(On)
    # Switch off
    comp.change(Off)

    # Switch on again
    comp.change(On)
    # Suspend
    comp.change(Suspend)
    # Try to hibernate - cannot!
    comp.change(Hibernate)
    # Switch on back
    comp.change(On)
    # Finally off
    comp.change(Off)
