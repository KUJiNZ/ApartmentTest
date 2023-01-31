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
        """
        Name: Artiom
        Function Name:__init__
        Description: init of AprtmHaifa
        :param rooms: metrage of apartment rooms
        """
        load_dotenv()
        self.arnona_cost = float(os.getenv('ARNONA_COST_HAIFA'))
        super().__init__(rooms)

    def calc_arnona(self):
        """
        Name: Artiom
        Function Name: calc_arnona
        Description: Calculating arnona in Haifa apartment
        """
        return [(v * float(os.getenv('ARNONA_COST_HAIFA')) * float(os.getenv('DISCOUNT_ROOM_HAIFA'))) if k == int(os.getenv('ROOM_NUM_HAIFA')) else v*float(os.getenv('ARNONA_COST_HAIFA'))for k, v in self.rooms.items()]

    def calc_apartment_price(self):
        """
        Name: Artiom
        Function Name: calc_apartment_price
        Description: Calculating apartment price in Haifa
        """
        for r in self.rooms.values():
            self.aprtm_price += r * self.arnona_cost
        return self.aprtm_price


        #  aprtm_PRICE HERZELIA
        # 1 - 50 X 1000 (60 X 1000 = 60000 )
        # 50- 100 - 10% (60000+ 10 * 1100 )= 71000
        # >100 - 12%

        # Discount of arnona for Haifa 5%

    # list of tuple
