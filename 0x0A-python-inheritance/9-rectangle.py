#!/usr/bin/python3
'''module definition of rectangle class definition'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry
'''importing parent directory to be used'''


class Rectangle(BaseGeometry):
    '''class rectangle definition'''

    def __init__(self, width, height):
        '''rectangle class initialization'''

        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        '''implementing area method'''
        return self.__width * self.__height

    def __str__(self):
        '''initializing the str method'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
