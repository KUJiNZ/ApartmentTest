from aprtm_haifa import AprtmHaifa
from aprtm_herz import AprtmHerz
from dotenv import load_dotenv
from log import Log
import os

if __name__ == '__main__':
    # ENV FILE
    load_dotenv()

    # LOGGER
    LOG = Log("__main__", "apartment_log_main.log")
    logger = LOG.logger

    d = {1:12,2:13,3:15,4:20,5:100}

    haifa = AprtmHaifa(d)
    # herz = AprtmHerz(d)
    print(haifa.calc_arnona())
