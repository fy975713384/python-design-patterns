# -*- coding: utf-8 -*-

"""
现实世界中的模板模式
"""

from abc import ABCMeta, abstractmethod


class Trip(metaclass=ABCMeta):
    @abstractmethod
    def set_transport(self):
        pass

    @abstractmethod
    def day_1(self):
        pass

    @abstractmethod
    def day_2(self):
        pass

    @abstractmethod
    def day_3(self):
        pass

    @abstractmethod
    def return_home(self):
        pass

    def itinerary(self):
        self.set_transport()
        self.day_1()
        self.day_2()
        self.day_3()
        self.return_home()


class VeniceTrip(Trip):
    def set_transport(self):
        print('Take a boat and find your way in the Grand Canal')

    def day_1(self):
        print('Visit St Mark\'s Basilica in St Mark\'s Square')

    def day_2(self):
        print('Appreciate Doge\'s Palace')

    def day_3(self):
        print('Enjoy the food near the Rialto Bridge')

    def return_home(self):
        print('Get souvenirs for friends and get back')


class MaldivesTrip(Trip):
    def set_transport(self):
        print('On foot, on any island, Wow!')

    def day_1(self):
        print('Enjoy the marine life of Banana Reef')

    def day_2(self):
        print('Go for the water sports and snorkelling')

    def day_3(self):
        print('Relax on the bench and enjoy the sun')

    def return_home(self):
        print('Dont fell like leaving the beack..')


class TravelAgency:
    def arrange_trip(self):
        choice = input('What kind of place you\'d like to go historical or to a beach?\n')
        if choice == 'historical':
            self.trip = VeniceTrip()
            self.trip.itinerary()
        if choice == 'beach':
            self.trip = MaldivesTrip()
            self.trip.itinerary()


TravelAgency().arrange_trip()
