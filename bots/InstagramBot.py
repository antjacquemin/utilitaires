from selenium import webdriver
from time import sleep
from json import load, dump
from datetime import datetime

FICHIER_CONFIG = "../config.json"
NB_MAX_LIKES_HEURE = 350
NB_MAX_LIKES_JOUR = 1000
COEFF_EVO_LIKES = 1.5
NB_MAX_TAGS = 5
NB_MAX_HASHTAGS = 30
NB_MAX_FOLLOWS_HEURE = 30
NB_MAX_FOLLOWS_JOUR = 720
NB_MAX_FOLLOW = 7500
TEMPS_INTER_LIKE = 36
TEMPS_INTER_FOLLOW = 38
TEMPS_INTER_COMMENT = 400
TEMPS_NOUVEAU = 48
NB_LIKES_NOUVEAU = 5
NB_MOIS_NOUVEAU_PROFIL = 6
NB_HEURES_INTERDICTION = 72

class InstagramBot():

    def __init__(self):
        self.driver = webdriver.Firefox()
        with open(FICHIER_CONFIG) as fichier:
            donnees = load(fichier)
            config = donnees["instagram"]
            self.username = config["username"]
            self.password = config["password"]  
            self.dateJour = datetime.today()
            if ("nbMaxLikes" in config and "dateDerniereConnexion" in config):
                self.nbMaxLikes = config["nbMaxLikes"]
                self.dateDerniereConnexion = config["dateDerniereConnexion"]
            else:
                self.nbMaxLikes = NB_LIKES_NOUVEAU
                self.dateDerniereConnexion = self.dateJour.strftime("%Y-%m-%d")
            
    def updateConfig(self):
        with open(FICHIER_CONFIG,'r+') as fichier: 
            donnees = load(fichier)
            config = donnees["instagram"]
            config["nbMaxLikes"] = self.nbMaxLikes 
            config["dateDerniereConnexion"] = self.dateDerniereConnexion 
            fichier.seek(0)
            dump(donnees, fichier, indent=4)
            fichier.truncate() 

    def nouveauProfil(self):
        return 

    def login(self):
        self.driver.get('https://www.instagram.com/')

        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Accepter')]").click()
        sleep(2)

        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.username)
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.password)
        sleep(1)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()

        sleep(4)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Plus tard')]").click()

        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Plus tard')]").click()

    def logout(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]').click()
        sleep(2)
        self.driver.find_element_by_xpath("//div[contains(text(), 'Déconnexion')]").click()
        sleep(2)

    def like(self):
        self.driver.find_element_by_class_name('wpO6b ').click()
        sleep(2)
    
    def unlike(self):
        self.driver.find_element_by_class_name('wpO6b ').click()
        sleep(2)

    def run(self):
        try:
            self.login()
            self.logout()
        finally:
            self.driver.quit()

instaBot = InstagramBot()
instaBot.updateConfig()
instaBot.run()
print(datetime.today().date)
date_time_str = '2018-06-29'
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
print(date_time_obj.date())