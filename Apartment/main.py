import ast
from aprtm_haifa import AprtmHaifa
from aprtm_herz import AprtmHerz
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    # ENV LOADER
    load_dotenv('.env')


    rooms_haifa = ast.literal_eval(os.getenv('ROOMS_HAIFA'))
    rooms_herz = ast.literal_eval(os.getenv('ROOMS_HERZ'))

    haifa = AprtmHaifa(rooms_haifa)
    herz = AprtmHerz(rooms_herz)

    print(f"Herzelia arnona cost: {herz.calc_arnona()}")
    print(f"Herzelia apartment price: {herz.calc_apartment_price()}")
    herz.kitchen = os.getenv('KITCHEN_TYPE_HERZ')
    print(f"Herzelia kitchen type : {herz.kitchen}")

    print("----------------------------------------------------------")

    print(f"Haifa arnona cost: {haifa.calc_arnona()}")
    print(f"Haifa apartment price: {haifa.calc_apartment_price()}")
    haifa.kitchen = os.getenv('KITCHEN_TYPE_HAIFA')
    print(f"Haifa kitchen type : {haifa.kitchen}")