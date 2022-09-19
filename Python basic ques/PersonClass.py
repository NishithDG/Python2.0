import abc
from abc import ABC
class Person(ABC):
    @abc.abstractmethod
    def get_gender(self):
        pass

class Male(Person):
    def get_gender(self):
        print('Male...')

class Female(Person):
    def  get_gender(self):
        print('Female...')


m = Male()
m.get_gender()


f = Female()
f.get_gender()
