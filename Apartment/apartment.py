
class Apartment(object):
    def __init__(self, aprt):
        self.dict = aprt
        self.kitchen = ''

    @property
    def kitchen(self):
        self.kitchen()

    @kitchen.getter
    def kitchen(self):
        return self.kitchen

    @kitchen.setter
    def kitchen(self, x=''):
        self.kitchen = x

    @kitchen.deleter
    def kitchen(self):
        del self.kitchen