# -*- coding: utf-8 -*-


"""
MVC 模式
"""


class Model:
    def logic(self):
        data = 'Got it!'
        print('Model: Crunching data as per business logic')
        return data


class View:
    def update(self, data):
        print(f'View: Updating the view with results: {data}')


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def interface(self):
        print('Controller: Relayed the Client asks')
        data = self.model.logic()
        self.view.update(data)


class Client:
    print('Client: asks for certain information')
    controller = Controller()
    controller.interface()
