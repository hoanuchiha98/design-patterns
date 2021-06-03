from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print('Woof')


class Dog(Animal):
    def make_sound(self):
        print('Meow')


if __name__ == '__main__':
    # animal = Animal()
    '''đa hình'''
    dog = Dog()
    # dog.make_sound()
    cat = Cat()
    # cat.make_sound()
    animals = [dog, cat]
    for animal in animals:
        animal.make_sound()
