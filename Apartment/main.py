from aprtm_haifa import AprtmHaifa
from aprtm_herz import AprtmHerz
from dotenv import load_dotenv
from log import Log
import os

if __name__ == '__main__':
    # ENV FILE
    load_dotenv()

    # LOGGER
    LOG = Log("__aprtmmain__", "apartment_log_main.log")
    logger = LOG.logger

    rooms = {1:12, 2:13, 3:15, 4:20, 5:100}

    haifa = AprtmHaifa(rooms)
    herz = AprtmHerz(rooms)

    print(haifa.calc_arnona())
    print(haifa.calc_apartment_price())

    print(herz.calc_arnona())
    print(herz.calc_apartment_price())
