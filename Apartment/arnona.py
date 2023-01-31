from abc import abstractmethod, ABC


class Arnona(ABC):
    def __int__(self):
        """
        Name: Artiom
        Function Name:__init__
        Description: init of abstract class Arnona
        """
        self.arnona_price = 0
        self.arnona_discount = 0
    @abstractmethod
    def calc_arnona(self):
        pass