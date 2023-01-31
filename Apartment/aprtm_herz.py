from Apartment.apartment import  Apartment
from Apartment.arnona import Arnona
from dotenv import load_dotenv
import os


class AprtmHerz(Apartment, Arnona):
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
        :return list of arnona bills
        """
        try:
            return [(v * float(os.getenv('ARNONA_COST_HERZ')) * float(os.getenv('DISCOUNT_ROOM_HERZ'))) if k == int(
                os.getenv('ROOM_NUM_HERZ')) else v * float(os.getenv('ARNONA_COST_HERZ')) for k, v in self.rooms.items()]
        except Exception as e:
            raise e

    def calc_apartment_price(self):
        """
        Name: Artiom
        Function Name: calc_apartment_price
        Description: Calculating apartment price in Haifa
        :return apartment price
        """
        try:
            for m in self.rooms.values():
                self.meter += m
            temp = 0
            counter = {50: 1000, 100: 1100, 101: 1200}
            for k, v in counter.items():
                if 0 < self.meter >= k:
                    self.aprtm_price += (k - temp) * v
                    temp += k
                else:
                    self.aprtm_price += self.meter - (temp * v)
            return self.aprtm_price
        except Exception as e:
            raise e
