from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv


class Apartment(ABC):
    def __init__(self, rooms):
        """
        Name: Artiom
        Function Name:__init__
        Description: init of abstract class Apartment
        :param rooms: metrage of apartment rooms
        """
        self.arnona_cost = self.validate_arnona_cost()
        self.rooms = rooms
        self.meters = 0
        self.aprtm_price = 0
        self._kitchen = " "

    def validate_arnona_cost(self):
        """
        Name: Artiom
        Function Name: validate_arnona_cost
        Description: Validating if arnona cost getting right number type and not None
        :return: arnona cost
        """
        arnona_cost = float(os.getenv('ARNONA_COST_HERZ'))
        if arnona_cost is None or str():
            raise Exception
        return arnona_cost

    @property
    def kitchen(self):
        """
        Name: Artiom
        Function Name: kitchen
        Description: property of kitchen
        """
        return self._kitchen

    @kitchen.getter
    def kitchen(self):
        """
        Name: Artiom
        Function Name: kitchen
        Description: Getter of kitchen
        """
        return self._kitchen

    @kitchen.setter
    def kitchen(self, x):
        """
        Name: Artiom
        Function Name: kitchen
        Description: Setter of kitchen
        """
        self._kitchen = x

    @kitchen.deleter
    def kitchen(self):
        """
        Name: Artiom
        Function Name: kitchen
        Description: Deleter of kitchen
        """
        del self._kitchen

    @abstractmethod
    def calc_apartment_price(self):
        pass

    def calc_apartment_meters(self):
        pass

