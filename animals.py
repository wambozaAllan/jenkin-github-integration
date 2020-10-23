import sys

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

def main(args):
    animal = Animal(args[1], args[2])
    print("Name = ", animal.get_name())
    print("Name = ", animal.get_color())

main(sys.argv)
