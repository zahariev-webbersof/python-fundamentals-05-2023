# class Person:
#
#     # class attribute
#     species = 'Human'
#
#     def __init__(self, name):
#         self.name = name
#
# person1 = Person('Ivan')
# person2 = Person('Maria')
#
# print(person1.species)
# print(person2.species)
#
# Person.species = 'Homo sapiens'
#
# print(person1.species)
# print(person2.species)
#

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def resize(self, new_length, new_width):
        self.length = new_length
        self.width = new_width

rect = Rectangle(4, 5)

area = rect.calculate_area()
print(area)

rect.resize(6, 7)
print(rect.calculate_area())