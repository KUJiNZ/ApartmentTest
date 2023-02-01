from Apartment.apartment import  Apartment
from Apartment.arnona import Arnona
from dotenv import load_dotenv
import os
import ast

class AprtmHerz(Apartment, Arnona):
    load_dotenv()

    def __init__(self, rooms):
        """
        Name: Artiom
        Function Name:__init__
        Description: init of AprtmHerz
        :param rooms: metrage of apartment rooms
        """
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
        Description: Calculating apartment price in Herzelia
        :return apartment price
        """
        try:
            for m in self.rooms.values():
                self.meter += m
            prviuos_k = 0
            metters_left = 0
            price_counter = ast.literal_eval(os.getenv('PRICE_COUNTER_HERZ'))
            for k, v in price_counter.items():
                if 0 < self.meter >= k:
                    self.aprtm_price += (k - prviuos_k) * v
                    prviuos_k += k
                else:
                    self.aprtm_price += self.meter - (prviuos_k * v)
            return self.aprtm_price
        except Exception as e:
            raise e
