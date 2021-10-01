#!/usr/bin/python3
""" Module square"""


class Square():
    """ class Square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Instantiation of class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Calculate the area of square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Calculate the Perimter of square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Print the result """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create an object of Square """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())