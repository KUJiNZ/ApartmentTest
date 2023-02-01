import ast
from aprtm_haifa import AprtmHaifa
from aprtm_herz import AprtmHerz
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    # ENV LOADER
    load_dotenv()


    rooms_haifa = ast.literal_eval(os.getenv('ROOMS_HAIFA'))
    rooms_herz = ast.literal_eval(os.getenv('ROOMS_HERZ'))

    haifa = AprtmHaifa(rooms_haifa)
    herz = AprtmHerz(rooms_herz)

    print(haifa.calc_arnona())
    print(haifa.calc_apartment_price())

    print(herz.calc_arnona())
    print(herz.calc_apartment_price())
