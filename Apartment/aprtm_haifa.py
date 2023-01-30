import collections

from apartment import Apartment
from arnona import Arnona
from log import Log
from dotenv import load_dotenv
import os


class AprtmHaifa(Apartment, Arnona):
    LOG = Log("__main__", "aprtm_haifa.log")
    logger = LOG.logger

    def __init__(self, rooms):
        load_dotenv()
        self.arnona_cost = float(os.getenv('ARNONA_COST_HAIFA'))
        super().__init__(rooms)

    def calc_arnona(self):
        return [v * 30 if k == 3 else (v * 0.5 * 30) for k, v in self.rooms.items()]

    def calc_apartment_price(self):
        for r in self.rooms.values():
            self.aprtm_price += r
        self.aprtm_price *= self.arnona_cost
        # return self.aprtm_price
        return

        #  aprtm_PRICE HERZELIA
        # 1 - 50 X 1000 (60 X 1000 = 60000 )
        # 50- 100 - 10% (60000+ 10 * 1100 )= 71000
        # >100 - 12%

        # Discount of arnona for Haifa 5%

    # list of tuple
