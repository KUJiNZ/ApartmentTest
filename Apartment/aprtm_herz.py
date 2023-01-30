from apartment import Apartment
from arnona import Arnona
from log import Log
from dotenv import load_dotenv
import os


class AprtmHerz(Apartment, Arnona):
    LOG = Log("__main__", "aprtm_herz.log")
    logger = LOG.logger

    def __init__(self, rooms):
        load_dotenv()
        self.arnona_cost = float(os.getenv('ARNONA_COST_HERZ'))
        self.arnona_price = 0
        super().__init__(rooms)

    def calc_arnona(self):
        room_num = 1


        for a in self.rooms.values():
            if room_num == float(os.getenv('ROOM_NUM_HERZ')) :
                self.arnona_price += self.arnona_cost * a
                room_num += 1

            else:
                self.arnona_price += (self.arnona_cost * a) * float(os.getenv('DISCOUNT'))
                room_num += 1
