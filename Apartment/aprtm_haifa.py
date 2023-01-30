from  apartment import Apartment
from  arnona import Arnona
from dotenv import load_dotenv
import os


class AprtmHaifa(Apartment,Arnona):

    def __init__(self, rooms):
        self.arnona_cost = 30
        self.rooms = rooms
        self.city = 'Haifa'
        self.price = 0
        super().__init__(rooms)

    def calc_arnona(self):
        count = 0

        for a in self.rooms:
            if count == 2:
                self.price += self.arnona_cost * a.value
                count += 1

            else:
                self.price += (self.arnona_cost * a.value) * 0.5
                count += 1