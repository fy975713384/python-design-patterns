# -*- coding: utf-8 -*-

"""
命令模式
"""


class Wizard:

    def __init__(self, src, root_dir):
        self.choices = []
        self.src = src
        self.root_dir = root_dir

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print(f'Copying binaries -- {self.src} to {self.root_dir}')
            else:
                print('No Operation')


if __name__ == '__main__':
    # Client Code
    wizard = Wizard('python', '/usr/bin/')
    # Users chooses to install python only
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    wizard.execute()
