import pytest
from selenium import webdriver
#scope="function": A new Chrome browser opens and closes for each 
# test case, giving every test a fresh browser session.
@pytest.fixture(scope="function")
def setup_browser():
    
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()# Maximize the browser window
    driver.implicitly_wait(10)  # Set an implicit wait time of 10 seconds
    yield driver  # Provide the driver to the test case
    driver.quit()  # Close the browser after the test case is done
    