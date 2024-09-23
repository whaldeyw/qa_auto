from time import sleep
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

def test2():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.set_window_size(1800, 1100)


    url = "https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%26source%3Dheader-home"
    driver.get(url)
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(os.getenv('username'))
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(os.getenv('password'))
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[13]').click()
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div/aside/div/div/loading-context/div/div[1]/div/div[1]/a/span/span[2]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id=":r9:"]').send_keys('github_api')
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id=":rb:"]').send_keys('github_api_create')
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/main/react-app/div/form/div[5]/button/span/span').click()
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[1]/div[1]/div/div[2]/nav/ul/li[1]/a/span').click()
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a/span[1]').click()
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/main/div/div/div[2]/turbo-frame/div/div[2]/ul/li[1]/div[1]/div[1]/h3/a').click()
    sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[9]/a/span[1]').click()
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div[2]/div/div/div/div[9]/ul/li[5]/div[1]/form/button/span/span').click()
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div[2]/div/div/div/div[9]/ul/li[5]/div[1]/form/dialog-helper/dialog/div[2]/div/button/span/span').click()
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div[2]/div/div/div/div[9]/ul/li[5]/div[1]/form/dialog-helper/dialog/div[2]/div/div/button/span/span').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="verification_field"]').send_keys(f'{os.getenv("username")}/github_api')
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div[2]/div/div/div/div[9]/ul/li[5]/div[1]/form/dialog-helper/dialog/div[2]/div/div/button/span/span').click()
    sleep(3)

if __name__ == "__main__":
    test2()
