import logging
import yaml
import os

class Config():
    def __init__(self):
        # Niveau des log
        self.LOG_LEVEL = logging.DEBUG
        #self.LOG_LEVEL = logging.CRITICAL
        
        self.CONFIG_FILE_NAME = "Config.yaml"

        """ À compléter: la lecture du fichier de config """
        fichier = open(self.CONFIG_FILE_NAME, "r")
        config = yaml.load(fichier)

        self.WAKEUP = config['wakeup']
        self.CLOSE = config['close']
        self.PERIOD = config['period']
        self.PATH = config['path']
        
        self.SCREEN_WIDTH = config['screen_width']
        self.SCREEN_HEIGHT = config['screen_height']
        self.SCREEN_SIZE = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.FPS = config['fps']
        
        
    def affiche(self):
        """ À compléter: Afficher tout les attributs de la classe """
        print("CONFIG_FILE_NAME", self.CONFIG_FILE_NAME)
        print("LOG_LEVEL", self.LOG_LEVEL)
        print("CONFIG_FILE_NAME",self.CONFIG_FILE_NAME)

        print("WAKEUP", self.WAKEUP)
        print("CLOSE", self.CLOSE)
        print("PERIOD", self.PERIOD)
        print("PATH", self.PATH)

        print("SCREEN_WIDTH", self.SCREEN_WIDTH)
        print("SCREEN_HEIGHT", self.SCREEN_HEIGHT)
        print("SCREEN_SIZE", self.SCREEN_SIZE)
        print("FPS", self.FPS)


    def getPeriod(self):
        chaine = self.PERIOD 
        heure,minute,seconde = map(int, chaine.split(':'))
        return (heure * 3600 + minute * 60 + seconde)

if __name__ == "__main__":
    print ("Début du test\n")
    
    a = Config()
    a.affiche()
    print("PERIOD", a.getPeriod())

    print("\nFin du test")