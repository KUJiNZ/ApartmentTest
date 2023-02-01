from abc import abstractmethod, ABC
import os
from dotenv import load_dotenv


class Arnona(ABC):
    load_dotenv()
    def __int__(self):
        """
        Name: Artiom
        Function Name:__init__
        Description: init of abstract class Arnona
        """
        self.arnona_cost = float(os.getenv('ARNONA_COST_HAIFA'))
        self.arnona_price = 0
        self.arnona_discount = 0

    @abstractmethod
    def calc_arnona(self):
        pass