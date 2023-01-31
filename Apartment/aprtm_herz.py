from apartment import Apartment
from arnona import Arnona
from log import Log
from dotenv import load_dotenv
import os


class AprtmHerz(Apartment, Arnona):
    LOG = Log("__main__", "aprtm_herz.log")
    logger = LOG.logger

    def __init__(self, rooms):
        """
        Name: Artiom
        Function Name:__init__
        Description: init of AprtmHerz
        :param rooms: metrage of apartment rooms
        """
        load_dotenv()
        self.arnona_cost = float(os.getenv('ARNONA_COST_HERZ'))
        super().__init__(rooms)

    def calc_arnona(self):
        """
        Name: Artiom
        Function Name: calc_arnona
        Description: Calculating arnona in Herzelia apartment
        """
        return [(v * float(os.getenv('ARNONA_COST_HERZ')) * float(os.getenv('DISCOUNT_ROOM_HERZ'))) if k == int(os.getenv('ROOM_NUM_HERZ')) else v*float(os.getenv('ARNONA_COST_HERZ'))for k, v in self.rooms.items()]

    def calc_apartment_price(self):
        """
        Name: Artiom
        Function Name: calc_apartment_price
        Description: Calculating apartment price in Haifa
        """
        for r in self.rooms.values():
            self.aprtm_price += r * self.arnona_cost
        return self.aprtm_price
