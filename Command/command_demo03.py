# -*- coding: utf-8 -*-

"""
现实世界的命令模式
"""
from abc import ABCMeta, abstractmethod


# Command
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


# ConcreteCommand
class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


# ConcreteCommand
class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


# Receiver
class StockTrade:
    def buy(self):
        print('You will buy stocks')

    def sell(self):
        print('You will sell stocks')


class Agent:
    def __init__(self):
        self.__order_queue = []

    def place_order(self, order):
        self.__order_queue.append(order)
        order.execute()


if __name__ == '__main__':
    # Client
    stock = StockTrade()
    buy_stock = BuyStockOrder(stock)
    sell_stock = SellStockOrder(stock)

    # Invoker
    agent = Agent()
    agent.place_order(buy_stock)
    agent.place_order(sell_stock)
