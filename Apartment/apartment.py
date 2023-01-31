from abc import ABC, abstractmethod


class Apartment(ABC):

    def __init__(self, rooms):
        """
        Name: Artiom
        Function Name:__init__
        Description: init of abstract class Apartment
        :param rooms: metrage of apartment rooms
        """
        self.rooms = rooms
        self.meter = 0
        # self.kitchen = 'None'

    @property
    def kitchen(self):
        """
        Name: Artiom
        Function Name: kitchen
        Description: property of kitchen
        """
        self.kitchen()

    @kitchen.getter
    def kitchen(self):
        """
        Name: Artiom
        Function Name: kitchen
        Description: Getter of kitchen
        """
        return self.kitchen

    @kitchen.setter
    def kitchen(self, x=''):
        """
        Name: Artiom
        Function Name: kitchen
        Description: Setter of kitchen
        """
        self.kitchen = x

    @kitchen.deleter
    def kitchen(self):
        """
        Name: Artiom
        Function Name: kitchen
        Description: Deleter of kitchen
        """
        del self.kitchen

    @abstractmethod
    def calc_apartment_price(self):
        pass

    def calc_apartment_meters(self):
        pass

