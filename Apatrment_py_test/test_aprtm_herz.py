import ast
import pytest
import os
from dotenv import load_dotenv
from Apartment.log import Log
from Apartment.aprtm_herz import AprtmHerz

# LOGGER
LOG = Log("__herzytest__ ", "test_herz_log.log")
logger = LOG.logger
os.chdir("D:/PythonRepos/ApartmentTest/Apatrment_py_test")
load_dotenv('.env.test')

@pytest.fixture
def herz():
    # ENV FILE

    kitchen_type = os.getenv('KITCHEN_TYPE_HERZ')
    # HERZ ClASS
    rooms = ast.literal_eval(os.getenv('ROOMS_HERZ'))
    return AprtmHerz(rooms)


def test_setter_kitchen(herz):
    """
    Name: Artiom
    Function Name: kitchen
    Description: Testing setter of kitchen in class AprtmHerz
    """
    try:
        herz._kitchen = os.getenv('KITCHEN_TYPE_HERZ')
        assert herz._kitchen is os.getenv('KITCHEN_TYPE_HERZ')
        logger.info(f"{test_setter_kitchen.__doc__}")
        print(herz._kitchen)
    except Exception as e:
        logger.error(f"{test_setter_kitchen.__doc__}{e}")
        raise


def test_getter_kitchen(herz):
    """
    Name: Artiom
    Function Name: kitchen
    Description: Testing getter of kitchen in class AprtmHerz
    """
    try:
        x = herz._kitchen = os.getenv('KITCHEN_TYPE_HERZ')
        assert x is os.getenv('KITCHEN_TYPE_HERZ')
        logger.info(f"{test_setter_kitchen.__doc__}")
    except Exception as e:
        logger.error(f"{test_setter_kitchen.__doc__}{e}")
        raise


def test_deleter_kitchen(herz):
    """
    Name: Artiom
    Function Name: kitchen
    Description: Testing getter of kitchen in class AprtmHerz
    """
    try:
        del (herz._kitchen)
        with pytest.raises(AttributeError):
            x = herz._kitchen
        logger.info(f"{test_setter_kitchen.__doc__}")
    except Exception as e:
        logger.error(f"{test_setter_kitchen.__doc__}{e}")
        raise

def test_validate_arnona_cost(herz):
    """
    Name: Artiom
    Function Name: test_validate_arnona_cost
    Description:Testing validating of arnona cost getting right number type and not None in class AprtmHerz
    """
    try:
        x = herz.validate_arnona_cost()
        assert type(x) is float and not None
        logger.info(f"{test_calc_arnona.__doc__}")
    except Exception as e:
        logger.error(f"{test_calc_arnona.__doc__}{e}")
        raise


def test_calc_arnona(herz):
    """
    Name: Artiom
    Function Name: test_calc_arnona
    Description: Testing Calculating arnona in Herzelia apartment
    """
    try:
        x = herz.calc_arnona()
        print(x)
        assert type(x) is float and x is not None
        logger.info(f"{test_calc_arnona.__doc__}")
    except Exception as e:
        logger.error(f"{test_calc_arnona.__doc__}{e}")
        raise

def test_count_meters(herz):
    """
    Name: Artiom
    Function Name: calc_meters
    Description: Testing counting apartment meters in Herzelia
    :return: The meters of apartment
    """
    try:
        x = herz.count_meters()
        assert x is not None and x > 0
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
        logger.info(f"{test_calc_apartment_price.__doc__}")
    except Exception as e:
        logger.error(f"{test_calc_apartment_price.__doc__}{e}")
        raise
