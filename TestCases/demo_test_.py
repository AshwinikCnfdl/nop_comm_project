import logging


def test_logging():
    logger = logging.getLogger('selenium')

    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler("C:/Users/hp/PycharmProjects/nop_comm_projec/Logs/demo.log")
    logger.addHandler(handler)

    logging.getLogger('selenium.webdriver.remote').setLevel(logging.WARN)
    logging.getLogger('selenium.webdriver.common').setLevel(logging.DEBUG)

    logger.info("this is useful information")
    logger.warning("this is a warning")
    logger.debug("this is detailed debug information")

    with open("C:/Users/hp/PycharmProjects/nop_comm_projec/Logs/demo.log", 'r') as fp:
        assert len(fp.readlines()) == 3