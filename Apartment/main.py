import os
from dotenv import load_dotenv
from log import Log

if __name__ == '__main__':
    # ENV FILE
    load_dotenv()

    # LOGGER
    LOG = Log("__main__", "car_log_main.log")
    logger = LOG.logger