from time import sleep
#from secrets import pw
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Drive:
    def __init__(self):    
        #username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://accounts.google.com/signin/v2/identifier?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        driver.maximize_window()


        mail = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierId']"))).send_keys("testing1selen1")

        login = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/span"))).click()

        passw = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input"))).send_keys(password)

        next = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='passwordNext']/span/span"))).click()
        sleep(5)
        driver.get("https://www.google.com/maps/d/edit?mid=1U_qsdjzpjUxvh_4NWD_0wxcMw3DFlayR&ll=29.025576256879262%2C-92.41699249999999&z=4")
        driver.maximize_window()
        sleep(2)
        import_button = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Import')]"))).click()
        sleep(2)
        gdrive = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Google Drive')]"))).click()
        sleep(2)


        sleep(10)


my_bot = Drive()


