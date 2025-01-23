import logging
import pytest
from Configrations.Read_config_file import ReadConfigData
from utilities.CustomLogger import LogGen


class TestLog1002:
    URL = ReadConfigData.get_demoapplication_url()


    @pytest.mark.regression
    def test_home_title(self, setup):
        """Test to verify the title of the home page."""
        logger = LogGen.setup_logger()
        logger.info("Starting the program")
        logger.info("*************** TestLog1002: Verifying Home Page Title ***************")

        driver = setup
        try:
            logger.info("Launching the browser and navigating to the application URL.")
            driver.maximize_window()
            driver.implicitly_wait(20)
            driver.get(self.URL)

            logger.info("Fetching the page title for validation.")
            actual_title = driver.title
            expected_title = "Demo Web Shop"

            assert actual_title == expected_title, (
                f"Home page title validation failed. "
                f"Expected: '{expected_title}', Found: '{actual_title}'"
            )
            logger.info(f"Home page title validation passed. Title: '{actual_title}'")

        except Exception as e:
            logger.error(f"An exception occurred during the test: {str(e)}")
            pytest.fail(f"Test failed due to an exception: {str(e)}")

        finally:
            logger.info("Closing the browser.")
            try:
                driver.quit()
            except Exception as e:
                logger.error(f"Failed to close the browser: {str(e)}")
