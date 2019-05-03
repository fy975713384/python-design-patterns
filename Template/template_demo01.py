# -*- coding: utf-8 -*-

"""
模板方法模式
"""
from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collect_source(self):
        pass

    @abstractmethod
    def compiler_to_object(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compile_and_run(self):
        self.collect_source()
        self.compiler_to_object()
        self.run()


class iOSCompiler(Compiler):
    def collect_source(self):
        print('Collecting Swift Source Code..')

    def compiler_to_object(self):
        print('Compiling Swift code to LLVM bitcode..')

    def run(self):
        print('Program running on runtime environment..')


if __name__ == '__main__':
    iOS = iOSCompiler()
    iOS.compile_and_run()
