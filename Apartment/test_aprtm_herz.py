import pytest
import os
from dotenv import load_dotenv
from Apartment.log import Log
from Apartment.aprtm_herz import AprtmHerz

# LOGGER
LOG = Log("__herzytest__ ", "test_herz_log.log")
logger = LOG.logger


@pytest.fixture
def herz():
    # ENV FILE
    load_dotenv()

    # HERZ ClASS
    rooms = {1: 12, 2: 13, 3: 15, 4: 20, 5: 100}
    return AprtmHerz(rooms)


def test_calc_arnona(herz):
    """
    Name: Artiom
    Function Name: test_calc_arnona
    Description: Testing Calculating arnona in Herzelia apartment
    """
    try:
        x = herz.calc_arnona()
        assert type(x) is list and not None
        logger.info(f"{test_calc_arnona.__doc__}")
    except Exception as e:
        logger.error(f"{test_calc_arnona.__doc__}{e}")
        raise


def test_calc_apartment_price(herz):
    """
    Name: Artiom
    Function Name: calc_apartment_price
    Description: Test Calculating apartment price in Herzelia
    """
    try:
        x = herz.calc_apartment_price()
        assert x > 0 and not None
        logger.info(f"{test_calc_arnona.__doc__}")
    except Exception as e:
        logger.error(f"{test_calc_arnona.__doc__}{e}")
        raise
