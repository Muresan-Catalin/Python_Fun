class Rectangle:
    width = 0
    height = 0
    def __init__(self, w, h):
        #check if arguments are strings
        w = self.check_str(w)
        h = self.check_str(h)

        self.set_width(w)
        self.set_height(h)

    def check_str(self, val):
        a = val
        if isinstance(val, str):
            a = val.split('=')
            a = int(a[1])

        return a

    def set_width(self, w):
        self.width = self.check_str(w)

    def set_height(self, h):
        self.height = self.check_str(h)

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return(2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        i = 1
        j = 1
        txt = ""
        for i in range(self.height):
            for j in range(self.width):
                txt += '*'
            txt += '\n'

        return txt

    def get_amount_inside(self, shape):
        area = shape.get_area()
        return int(self.get_area() / area)

    def __str__(self):
        if self.width == self.height:
            txt = "Square"
            txt +='(side='
            txt += str(self.height)
            txt += ')'
        else:
            txt = "Rectangle"
            txt += '(width='
            txt += str(self.width)
            txt += ', height='
            txt += str(self.height)
            txt += ')'

        return txt



class Square(Rectangle):
    def __init__(self, h):
        if isinstance(h, str):
            h = h.split('=')
            h = int(h[1])
        Rectangle.width = h
        Rectangle.height = h

    def set_side(self, s):
        Rectangle.width = s
        Rectangle.height = s

    def set_width(self, w):
        self.set_side(w)

    def set_height(self, h):
        self.set_side(h)

a = Rectangle(4, 8)
a.set_width(7)
a.set_height(3)
a.get_picture()
