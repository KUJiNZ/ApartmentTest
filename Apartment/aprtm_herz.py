from Apartment.apartment import Apartment
from Apartment.arnona import Arnona
import os
import ast


class AprtmHerz(Apartment, Arnona):

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
        Description: Calculating arnona in Herzelia apartment by DISCOUNT AND ARNONA COST FROM ENV
        :return price of arnona
        """
        try:
            return sum([(v * float(os.getenv('ARNONA_COST_HERZ')) * float(os.getenv('DISCOUNT_ROOM_HERZ'))) if k == int(
                os.getenv('ROOM_NUM_HERZ')) else v * float(os.getenv('ARNONA_COST_HERZ')) for k, v in
                        self.rooms.items()])
        except Exception as e:
            raise e

    def calc_apartment_price(self):
        """
        Name: Artiom
        Function Name: calc_apartment_price
        Description: Calculating apartment price in Herzelia
                     by list of tuple PRICE_COUNTER_HERZ in env
        :return apartment price
        """
        try:
            # COUNTING ALL METERS OF APARTMENT
            self.count_meters()
            # GETTING LIST OF PRICES IN ENV
            price_counter = ast.literal_eval(os.getenv('PRICE_COUNTER_HERZ'))
            # pre_v helping to count current price after passing to next percent in price
            pre_v = 0
            # LOOP PASSING IN LIST OF PRICES AND COUNTING APARTMENT PRICE
            for v in price_counter:
                # IF START METERS AND END METERS LOWER THAN APARTMENT METERS COUNT PRICE BY END METERS AND BY PRICE
                if v[0] < self.meters >= v[1]:
                    self.aprtm_price += (v[1] - pre_v) * v[2]
                    pre_v = v[1]
                # IF START METERS LOWER THAN APARTMENT METERS BUT APARTMENT METERS IS GREATER COUNT DIFFERES OF METER LEFT OT COUNT
                elif v[0] <= self.meters <= v[1]:
                    self.aprtm_price += (self.meters - v[0]) * v[2]
            return self.aprtm_price

        except Exception as e:
            raise e

    def count_meters(self):
        """
        Name: Artiom
        Function Name: calc_meters
        Description: Counting apartment meters in Herzelia from list of rooms meters
        :return: The meters of apartment
        """
        try:
            for m in self.rooms.values():
                self.meters += m
        except Exception as e:
            raise e
