from Apartment.apartment import  Apartment
from Apartment.arnona import Arnona
from dotenv import load_dotenv
import os


class AprtmHaifa(Apartment, Arnona):
    load_dotenv()

    def __init__(self, rooms):
        """
        Name: Artiom
        Function Name:__init__
        Description: init of AprtmHaifa
        :param rooms: metrage of apartment rooms
        """

        super().__init__(rooms)

    def calc_arnona(self):
        """
        Name: Artiom
        Function Name: calc_arnona
        Description: Calculating arnona in Haifa apartment
        :return list of arnona bills
        """
        try:
            return [(v * float(os.getenv('ARNONA_COST_HAIFA')) * float(os.getenv('DISCOUNT_ROOM_HAIFA'))) if k == int(os.getenv('ROOM_NUM_HAIFA')) else v*float(os.getenv('ARNONA_COST_HAIFA'))for k, v in self.rooms.items()]
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
            for r in self.rooms.values():
                self.aprtm_price += r * float(os.getenv('METER_PRICE_HAIFA'))
            return self.aprtm_price
        except Exception as e:
            raise e


    def count_meters(self):
        """
        Name: Artiom
        Function Name: calc_meters
        Description: Counting apartment meters in Haifa
        :return: The meters of apartment
        """
        for m in self.rooms.values():
            self.meters += m