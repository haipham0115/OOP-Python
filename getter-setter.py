class Square:
    def __init__(self):
        self.__height = 2
        self.__width = 2

    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side
    
    # getter: grab the protected data, allow it to be readable
    def get_height(self):
        return self.__height

    # setter: change the initial data
    def set_height(self, h):
        if h >= 0:
            self.__height = h
        else:
            raise Exception("value needs to be 0 or larger")


square = Square()
square.set_height(-3)  # raises AttributeError
print(square.get_height())
