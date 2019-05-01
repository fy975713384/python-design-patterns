# -*- coding: utf-8 -*-

"""
工厂方法模式
"""

from abc import ABCMeta, abstractmethod


# Product
class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


# ConcreteProduct
class PersonalSection(Section):
    def describe(self):
        print('Personal Section')


# ConcreteProduct
class AlbumSection(Section):
    def describe(self):
        print('Album Section')


# ConcreteProduct
class PatentSection(Section):
    def describe(self):
        print('Patent Section')


# ConcreteProduct
class PublicationSection(Section):
    def describe(self):
        print('Publication Section')


# Creator
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_section(self, section):
        self.sections.append(section)


# ConcreteCreator
class LinkedIn(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(PatentSection())
        self.add_section(PublicationSection())


# ConcreteCreator
class Facebook(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(AlbumSection())


if __name__ == '__main__':
    profile_type = input("Which Profile you'd like to create? [LinkedIn or Facebook]\n")
    profile = eval(profile_type)()
    print(f'Creating Profile.. {type(profile).__name__}')
    print(f'Profile has sections --', profile.get_sections())
