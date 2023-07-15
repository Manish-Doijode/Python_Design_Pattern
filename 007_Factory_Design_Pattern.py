# 007_Factory_Design_Pattern.py
# allows modularity


from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def person_method(self):
        """Interface Method"""
        print("hello")

# p1 = IPerson() # this gives error TypeError: Can't instantiate abstract class IPerson with abstract methods person_method


class Student(IPerson):

    def __init__(self):
        self.name = "Manish"


s1 = Student()