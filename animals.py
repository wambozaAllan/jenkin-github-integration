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
    print("Animal name = ", animal.get_name())
    print("Animal color = ", animal.get_color())

main(sys.argv)
