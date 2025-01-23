import logging

from utilities.CustomLogger import LogGen


class Test_HomeTitle:
    URL = "http://demowebshop.tricentis.com/"  # Add your application URL here

    def __init__(self):
        self.logger = LogGen.loggener()  # Initialize logger

    def test_Home1_title(self,setup):
        self.logger.info("*************** Test_Reg_001: Verifying Home Page Title ***************")

        driver = setup  # Assuming setup is a WebDriver instance
        try:
            self.logger.info("Launching the browser and navigating to the application URL.")
            driver.maximize_window()
            driver.implicitly_wait(20)
            driver.get(self.URL)

            self.logger.info("Fetching the page title for validation.")
            actual_title = driver.title
            expected_title = "Demo Web Shop"

            if actual_title == expected_title:
                self.logger.info(f"Home page title validation passed. Title: '{actual_title}'")
                assert True
            else:
                self.logger.error(
                    f"Home page title validation failed. Expected: '{expected_title}', Found: '{actual_title}'")
                assert False, f"Title mismatch. Expected: '{expected_title}', Found: '{actual_title}'"

        except Exception as e:
            self.logger.error(f"An exception occurred during the test: {str(e)}")
            assert False, f"Test failed due to an exception: {str(e)}"

        finally:
            self.logger.info("Closing the browser.")
            driver.quit()
