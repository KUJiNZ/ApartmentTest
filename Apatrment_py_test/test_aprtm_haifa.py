import ast

import pytest
import os
from dotenv import load_dotenv
from Apartment.log import Log
from Apartment.aprtm_haifa import AprtmHaifa

# LOGGER
LOG = Log("__haifaytest__ ", "test_haifa_log.log")
logger = LOG.logger


@pytest.fixture
def haifa():
    # ENV FILE
    load_dotenv('.env.test')
    kitchen_type = os.getenv('KITCHEN_TYPE_HAIFA')
    # HAIFA ClASS
    rooms = ast.literal_eval(os.getenv('ROOMS_HERZ'))
    return AprtmHaifa(rooms)


@pytest.mark.haifa_test_setter_kitchen
def test_setter_kitchen(haifa):
    """
    Name: Artiom
    Function Name: kitchen
    Description: Testing setter of kitchen in class AprtmHaifa
    """
    try:
        haifa._kitchen = os.getenv('KITCHEN_TYPE_HERZ')
        assert haifa._kitchen is os.getenv('KITCHEN_TYPE_HERZ')
        logger.info(
            f"{test_setter_kitchen.__doc__}\nActual: {haifa._kitchen} Expected: {os.getenv('KITCHEN_TYPE_HERZ')}\n")
    except Exception as e:
        logger.exception(f"{test_setter_kitchen.__doc__}{e}\n")
        raise


@pytest.mark.haifa_test_getter_kitchen
def test_getter_kitchen(haifa):
    """
    Name: Artiom
    Function Name: kitchen
    Description: Testing getter of kitchen in class AprtmHaifa
    """
    try:
        x = haifa._kitchen = os.getenv('KITCHEN_TYPE_HERZ')
        assert x is os.getenv('KITCHEN_TYPE_HERZ')
        logger.info(f"{test_setter_kitchen.__doc__}\nActual: {x} Expected: {os.getenv('KITCHEN_TYPE_HERZ')}\n")
    except Exception as e:
        logger.exception(f"{test_setter_kitchen.__doc__}{e}\n")
        raise


@pytest.mark.haifa_test_deleter_kitchen
def test_deleter_kitchen(haifa):
    """
    Name: Artiom
    Function Name: kitchen
    Description: Testing getter of kitchen in class AprtmHaifa
    """
    try:
        del (haifa._kitchen)
        with pytest.raises(AttributeError):
            x = haifa._kitchen
        logger.info(f"{test_setter_kitchen.__doc__}\nActual: {AttributeError} Expected: {AttributeError}\n")
    except Exception as e:
        logger.exception(f"{test_setter_kitchen.__doc__}{e}\n")
        raise


@pytest.mark.haifa_test_validate_arnona_cost
def test_validate_arnona_cost(haifa):
    """
    Name: Artiom
    Function Name: test_validate_arnona_cost
    Description:Testing validating of arnona cost getting right number type and not None in class AprtmHaifa
    """
    try:
        x = haifa.validate_arnona_cost()
        assert type(x) is float and not None
        logger.info(f"{test_calc_arnona.__doc__}\nActual: {type(x)} Expected: {float}\n")
    except Exception as e:
        logger.exception(f"{test_calc_arnona.__doc__}{e}\n")
        raise


@pytest.mark.haifa_test_calc_arnona
def test_calc_arnona(haifa):
    """
    Name: Artiom
    Function Name: test_calc_arnona
    Description: Testing Calculating arnona in Haifa apartment
    """
    try:
        x = haifa.calc_arnona()
        assert type(x) is float and not None
        logger.info(f"{test_calc_arnona.__doc__}\nActual: {type(x)} Expected: {float}\n")
    except Exception as e:
        logger.exception(f"{test_calc_arnona.__doc__}{e}\n")
        raise


@pytest.mark.haifa_test_calc_apartment_price
def test_calc_apartment_price(haifa):
    """
    Name: Artiom
    Function Name: calc_apartment_price
    Description: Test Calculating apartment price in Haifa
    """
    try:
        x = haifa.calc_apartment_price()
        assert x > 0 and not None
        logger.info(f"{test_calc_arnona.__doc__}\nActual: {x} Expected: (x > 0 and not None)\n")
    except Exception as e:
        logger.exception(f"{test_calc_arnona.__doc__}{e}\n")
        raise
