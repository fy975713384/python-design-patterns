# -*- coding: utf-8 -*-

"""
门面模式
"""


# 简化接口的门面
class EventManager:

    def __init__(self):
        print('Event Manager:: Let me talk to the folks\n')

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirments()

        self.caterer = Caterer()
        self.caterer.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()


# 子系统1
class Hotelier:
    def __init__(self):
        print('Arranging the Hotel for Marriage? --')

    def __is_available(self):
        print('Is the Hotel free for the event on given day?')

    def book_hotel(self):
        if self.__is_available():
            print('Registered the Booking\n\n')


# 子系统2
class Florist:
    def __init__(self):
        print('Flower Decorations for the Event? --')

    def set_flower_requirments(self):
        print('Carnations, Roses and Lilies would be used for Decorations\n\n')


# 子系统3
class Caterer:
    def __init__(self):
        print('Food Arrangements for the Event --')

    def set_cuisine(self):
        print('Chinese & Continental Cuisine to be served\n\n')


# 子系统4
class Musician:
    def __init__(self):
        print('Musical Arrangements for the Marriage --')

    def set_music_type(self):
        print('Jazz and Classical will be played\n\n')


# 客户端
class You:
    def __init__(self):
        print('You:: Whoa! Marriage Arrangements??!!!')

    def ask_envent_manager(self):
        print('You:: Let\'s Contact the Event Manager\n\n')
        em = EventManager()
        em.arrange()

    def __del__(self):
        print('You:: Thanks to Event Manager, all preparations done! Phew!')


you = You()
you.ask_envent_manager()
