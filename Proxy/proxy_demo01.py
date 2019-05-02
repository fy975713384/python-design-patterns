# -*- coding: utf-8 -*-


"""
代理模式
"""


class Actor:
    def __init__(self):
        self.is_busy = False

    def occupied(self):
        self.is_busy = True
        print(f'{type(self).__name__} is occupied with current movie')

    def available(self):
        self.is_busy = False
        print(f'{type(self).__name__} is free for the movie')

    def get_status(self):
        return self.is_busy


# proxy
class Agent:
    def __init__(self):
        self.principal = None

    def work(self):
        self.actor = Actor()
        if self.actor.get_status():
            self.actor.occupied()
        else:
            self.actor.available()


if __name__ == '__main__':
    r = Agent()
    r.work()
