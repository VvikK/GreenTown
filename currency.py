from pygame import *

class Currency(object):
    def __init__ (self, value, name, image, cap, stbar, xpos, ypos):
        self.value = value
        self.name = name
        self.image = image
        self.cap = cap
        self.stbar = stbar
        self.xpos = xpos
        self.ypos = ypos
        

    def cap(self):
        if self.value >= self.cap:
            self.value = self.cap

    def change(self, amount):
        self.value += amount

    def change_cap(self, amount):
        self.cap -= amount

    def set_bar_status(self):
        if self.name == "money":
            return self.value, 
        elif self.name == "happiness":
            length = 400*(self.value/self.cap)
            if self.value/self.cap <= 0.33:
                return self.stbar[1], length
            if self.value/self.cap <= 0.66 and self.value/self.cap > 0.33:
                return self.stbar[2], length
            if self.value/self.cap > 0.66:
                return self.stbar[3], length
        elif self.name == "CO2":
            length = 400*(self.value/self.cap)
            return self.stbar[4], length
        


                


            
        
            
