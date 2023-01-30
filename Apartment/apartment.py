from abc import ABC, abstractmethod


class Apartment(ABC):
    def __init__(self, rooms):
        self.rooms = rooms
        self.arnona_price = 0
        self.aprtm_price = 0
        self.arnona_discount = 0
        self.meter = 0
        kitchen = 'None'

    @property
    def kitchen(self):
        self.kitchen()

    @kitchen.getter
    def kitchen(self):
        return self.kitchen

    @kitchen.setter
    def kitchen(self, x=''):
        self.kitchen = x

    @kitchen.deleter
    def kitchen(self):
        del self.kitchen

    @abstractmethod
    def calc_apartment_price(self):
        pass

    def calc_apartment_meters(self):
        pass