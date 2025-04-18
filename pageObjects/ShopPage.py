from selenium.webdriver.common.by import By

class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")                      #driver.find_elements(By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")               #driver.find_elements(By.CSS_SELECTOR, ".card-footer button")
    shopCheckout = (By.XPATH, "//a[@class='nav-link btn btn-primary']") #driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']")

    # cartCheckout = (By.XPATH, "//button[@class='btn btn-success']")   #driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
    
    def getCardTitles(self):
        return self.driver.find_elements(*ShopPage.cardTitle)
    
    def getCardFooter(self):
        return self.driver.find_elements(*ShopPage.cardFooter)
    
    def shopCheckoutItems(self):
        return self.driver.find_element(*ShopPage.shopCheckout)