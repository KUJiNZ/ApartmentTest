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


@pytest.mark.herz_test_setter_kitchen
def test_setter_kitchen(herz):
    """
    Name: Artiom
    Function Name: kitchen
    Description: Testing setter of kitchen in class AprtmHerz
    """
    try:
        herz._kitchen = os.getenv('KITCHEN_TYPE_HERZ')
        assert herz._kitchen is os.getenv('KITCHEN_TYPE_HERZ')
        logger.info(
            f"{test_setter_kitchen.__doc__}\nActual: {herz._kitchen} Expected:{os.getenv('KITCHEN_TYPE_HERZ')}\n")
        print(herz._kitchen)
    except Exception as e:
        logger.exception(f"{test_setter_kitchen.__doc__}{e}\n")
        raise


@pytest.mark.herz_test_getter_kitchen
def test_getter_kitchen(herz):
    """
    Name: Artiom
    Function Name: kitchen
    Description: Testing getter of kitchen in class AprtmHerz
    """
    try:
        x = herz._kitchen = os.getenv('KITCHEN_TYPE_HERZ')
        assert x is os.getenv('KITCHEN_TYPE_HERZ')
        logger.info(f"{test_setter_kitchen.__doc__} \nActual: {x} Expected:{os.getenv('KITCHEN_TYPE_HERZ')}\n")
    except Exception as e:
        logger.exception(f"{test_setter_kitchen.__doc__}{e}\n")
        raise


@pytest.mark.herz_test_deleter_kitchen
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
        logger.info(f"{test_setter_kitchen.__doc__} \nActual: {AttributeError} Expected: {AttributeError}\n")
    except Exception as e:
        logger.exception(f"{test_setter_kitchen.__doc__}{e}\n")
        raise


@pytest.mark.herz_test_validate_arnona_cost
def test_validate_arnona_cost(herz):
    """
    Name: Artiom
    Function Name: test_validate_arnona_cost
    Description:Testing validating of arnona cost getting right number type and not None in class AprtmHerz
    """
    try:
        x = herz.validate_arnona_cost()
        assert type(x) is float and not None
        logger.info(f"{test_calc_arnona.__doc__}\nActual: {type(x)} Expected: (float and not None)\n")
    except Exception as e:
        logger.exception(f"{test_calc_arnona.__doc__}{e}\n")
        raise


@pytest.mark.herz_test_calc_arnona
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
        logger.info(f"{test_calc_arnona.__doc__}\nActual: {type(x)} Expected: (float and not None)\n")
    except Exception as e:
        logger.exception(f"{test_calc_arnona.__doc__}{e}\n")
        raise


@pytest.mark.herz_test_count_meters
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
        logger.info(f"{test_calc_arnona.__doc__}\nActual: {x} Expected:(x > 0 and not None)\n")
    except Exception as e:
        logger.exception(f"{test_calc_arnona.__doc__}{e}")
        raise

@pytest.mark.herz_test_calc_apartment_price
def test_calc_apartment_price(herz):
    """
    Name: Artiom
    Function Name: calc_apartment_price
    Description: Test Calculating apartment price in Herzelia
    """
    try:
        x = herz.calc_apartment_price()
        assert x > 0 and not None
        logger.info(f"{test_calc_apartment_price.__doc__}\nActual: {x} Expected:(x > 0 and not None)\n")
    except Exception as e:
        logger.exception(f"{test_calc_apartment_price.__doc__}{e}\n")
        raise
