import logging

class LogGen:
    @staticmethod
    def setup_logger():
        """Set up the logger with a single instance."""
        logger = logging.getLogger("TestLog1002")
        if not logger.handlers:  # Avoid duplicate handlers
            handler = logging.FileHandler("C:/Users/hp/PycharmProjects/nop_comm_project/Logs/automation_test_login.log",
                                          mode="a")
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S %p"
            )
            handler.setFormatter(formatter)
            logger.setLevel(logging.INFO)
            logger.addHandler(handler)
        return logger

