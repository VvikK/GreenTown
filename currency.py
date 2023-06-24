from pygame import *

class Currency(object):
    def __init__ (self, value, name, image_frames, cap):
        self.value = value
        self.name = name
        self.image_frames = image_frames
        self.cap = cap
        img = transform.scale(image.load(self.image_frames), (640, 480))

    def cap(self):
        if self.value >= self.cap:
            self.value = self.cap

    def change(self, amount):
        self.value += amount

    def change_cap(self, amount):
        self.cap -= amount

