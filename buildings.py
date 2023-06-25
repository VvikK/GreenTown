class Building(object):
    def __init__ (self, value, co2_contribution, happiness_contribution, money_contribution, name, image_frames, cap, mousex, mousey, placex, placey, w, h):
        self.value = value
        self.name = name
        self.co2_contribution = co2_contribution
        self.happiness_contribution = happiness_contribution
        self.money_contribution = money_contribution
        self.image_frames = image_frames
        self.cap = cap
        self.mousex = mousex
        self.mousey = mousey
        self.placex = placex
        self.placey = placey
        self.w = w
        self.h = h
        