from pygame import *

class Currency(object):
    def __init__ (self, value, name, image, cap):
        self.value = value
        self.name = name
        self.image = image
        self.cap = cap
        

    def cap(self):
        if self.value >= self.cap:
            self.value = self.cap

    def change(self, amount):
        self.value += amount

    def change_cap(self, amount):
        self.cap -= amount

