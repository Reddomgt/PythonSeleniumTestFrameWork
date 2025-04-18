from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    deliveryLocation = (By.ID,"country")    #self.driver.find_element(By.ID, "country").send_keys("Ind")  # Type 'Ind' in the country search field
    dropdownIndia = (By.LINK_TEXT,"India")  #self.driver.find_element(By.LINK_TEXT, "India").click()  # Click on the 'India' link
    checkbox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")    #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    purchaseBtn = (By.XPATH, "//input[@class='btn btn-success btn-lg']") #self.driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()

    def getDeliveryLocation(self):
        return self.driver.find_element(*ConfirmPage.deliveryLocation)
    
    def getDropdownIndia(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        return self.driver.find_element(*ConfirmPage.dropdownIndia)
    
    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)
    
    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn)


    

    
