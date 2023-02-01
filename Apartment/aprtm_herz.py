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
                os.getenv('ROOM_NUM_HERZ')) else v * float(os.getenv('ARNONA_COST_HERZ')) for k, v in
                    self.rooms.items()]
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
            self.count_meters()

            meters_left = self.meters
            previous_k = 0
            price_counter = ast.literal_eval(os.getenv('PRICE_COUNTER_HERZ'))

            for k, v in price_counter.items():
                if 0 < self.meters >= k:
                    self.aprtm_price += (k - previous_k) * v
                    previous_k = k
                else:
                    self.aprtm_price += meters_left * v
            return self.aprtm_price

        except Exception as e:
            raise e

    def count_meters(self):
        """
        Name: Artiom
        Function Name: calc_meters
        Description: Counting apartment meters in Herzelia
        :return: The meters of apartment
        """
        for m in self.rooms.values():
            self.meters += m
        return self.meters
