from apartment import Apartment
from  arnona import Arnona
from dotenv import load_dotenv
import os


class AprtmHerz(Apartment,):

    def __init__(self, rooms):
        load_dotenv()
        self.arnona_cost = float(os.getenv('ARNONA_COST_HERZ'))
        self.rooms = rooms
        self.city = 'Herz'
        self.price = 0
        super().__init__(rooms)

    def calc_arnona(self):
        count = 0

        for a in self.rooms:
            if count == 3:
                self.price += self.arnona_cost * a.value
                count += 1

            else:
                self.price += (self.arnona_cost * a.value) * 0.5
                count += 1
