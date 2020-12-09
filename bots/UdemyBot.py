from selenium import webdriver
from time import sleep
from json import load

FICHIER_CONFIG = "../config.json"
CATEGORIES = [
    'development',
    'it-and-software'
]
MIN_NOTE = 4.2
MIN_NB_NOTES = 200

class UdemyBot():

    def __init__(self):
        self.driver = webdriver.Firefox()
        with open(FICHIER_CONFIG) as fichier:
            donnees = load(fichier)
            config = donnees["udemy"]
            self.email = config["email"]
            self.password = config["password"]
    
    def login(self):
        self.driver.get('https://www.udemy.com/')
        sleep(2)

        self.driver.find_element_by_xpath("//span[contains(text(), 'Se connecter')]").click()
        sleep(2)

        self.driver.find_element_by_xpath("//input[@name=\"email\"]").send_keys(self.email)
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.password)
        sleep(1)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        
    def logout(self):
        self.driver.find_element_by_xpath("//div[contains(text(), 'Se déconnecter')]").click()
        sleep(2)

    def run(self):
        try:
            self.login()
            self.logout()
        finally:
            self.driver.quit()

udemyBot = UdemyBot()
udemyBot.login()
udemyBot.logout()
