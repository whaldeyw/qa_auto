from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    url = "https://www.saucedemo.com/"
    driver.get(url)
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    sleep(5)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a').click()
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('Oleg')
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('Tyulnew')
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('606380')
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    sleep(5)

if __name__ == "__main__":
    test()

