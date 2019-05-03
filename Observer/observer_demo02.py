# -*- coding: utf-8 -*-


"""
观察者模式
"""

from abc import ABCMeta, abstractmethod


# Subject
class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latest_news = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def add_news(self, news):
        self.__latest_news = news

    def get_news(self):
        return 'Got News:', self.__latest_news


# Observer
class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


# ConcreteObserver
class SMSSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(f'{type(self).__name__} {self.publisher.get_news()}')


# ConcreteObserver
class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(f'{type(self).__name__} {self.publisher.get_news()}')


# ConcreteObserver
class AnyOtherSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(f'{type(self).__name__} {self.publisher.get_news()}')


if __name__ == '__main__':
    news_publisher = NewsPublisher()
    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher)
    print(f'\nSubscribers: {news_publisher.subscribers()}')

    news_publisher.add_news('Hello World!')
    news_publisher.notify_subscribers()

    print(f'\nDetached: {type(news_publisher.detach()).__name__}')
    print(f'\nSubscribers: {news_publisher.subscribers()}')

    news_publisher.add_news('Second News!')
    news_publisher.notify_subscribers()
