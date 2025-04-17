import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")  # Get the browser name from command line options

    if browser_name == 'chrome':
        # Get the path to the ChromeDriver from environment variables
        chromedriver_path = os.getenv('CHROMEDRIVER_PATH') 
        # Initialize the Chrome driver with the specified service
        service_obj = Service(chromedriver_path)  
        driver = webdriver.Chrome(service=service_obj)  # Initialize the Chrome WebDriver with the service object

    elif browser_name == 'firefox':
        # Get the path to the GeckoDriver from environment variables
        geckodriver_path = os.getenv('GECKODRIVER_PATH')  
        # Initialize the Firefox driver with the specified service
        service_obj = Service(geckodriver_path)  
        driver = webdriver.Firefox(service=service_obj)

    elif browser_name == 'edge':
        # Get the path to the EdgeDriver from environment variables
        edgedriver_path = os.getenv('EDGEDRIVER_PATH')  
        # Initialize the Edge driver with the specified service
        service_obj = Service(edgedriver_path)  
        driver = webdriver.Edge(service=service_obj)

    # Open the specified URL in the browser
    driver.get("https://rahulshettyacademy.com/angularpractice/")  # Open the webpage
    
    #driver refers to local driver and cls.driver is the class driver
    request.cls.driver = driver

    #Anything after yield will be executed at the end
    yield
    driver.close()
