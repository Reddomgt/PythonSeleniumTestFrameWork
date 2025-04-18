from selenium.webdriver.common.by import By

class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    deliveryLocation = (By.ID,"country")    #self.driver.find_element(By.ID, "country").send_keys("Ind")  # Type 'Ind' in the country search field


    def getDeliveryLocation(self):
        return self.driver.find_element(*ConfirmPage.deliveryLocation)