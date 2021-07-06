import time
from datetime import datetime
import pygame
from Config import Config
from ListePhotos import ListePhotos
from Album import Album
from EtatSysteme import EtatSysteme
from fonctions import *


pygame.init()

config = Config()
screen = pygame.display.set_mode(config.SCREEN_SIZE)
clock = pygame.time.Clock()
album = Album(config)
listePhotos = ListePhotos(album.getAlbumCourant())
etat = EtatSysteme.ACTIF
photo = listePhotos.getPhoto()
img = pygame.image.load(photo)
new_size = aspectScale(img,config.SCREEN_SIZE)
new_position = cornerPos(img,config.SCREEN_SIZE)
temps1 = time.time()
print(datetime.now(), photo)

running = True
while running:
    """ Boucle pygame """
    # clock.tick(config.FPS)
    
    for event in pygame.event.get():
        """ Gestion des évenements et bouttons pygame (quitter, veille, prochain album"""
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            photo = listePhotos.getPhoto()
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_LEFT: # Simule le bouton GPIO 17
                listePhotos = ListePhotos(album.getNextAlbum())
                print(album.getAlbumCourant())
                photo = listePhotos.getPhoto()
            elif event.key == pygame.K_RIGHT: # Simule le bouton GPIO 18
                if etat == EtatSysteme.VEILLE:
                    etat = EtatSysteme.ACTIF
                    temps1 = time.time()
                else:
                    etat = EtatSysteme.VEILLE
                print(etat)
         
    if etat == EtatSysteme.VEILLE:
        """ Affichage noir lorsqu'en veille """      
        screen.fill("#000000")

    
    else:
        """ Affichage des photos lorsqu'actif """  
        """ Selection de la photo à afficher selon le temps """
        temps2 = time.time()
        temps_ecoule = temps2-temps1
        #print(temps_ecoule)
        if temps_ecoule>config.getPeriod():
            temps1 = temps2
            photo = listePhotos.getPhoto()
            print("\n",datetime.now(), photo)
            img = pygame.image.load(photo)
            """ Traitement de la photo """
            #rotation = getRotation(photo)

            new_size = aspectScale(img,config.SCREEN_SIZE)
            img = pygame.transform.scale(img, (new_size))

            new_position = cornerPos(img,config.SCREEN_SIZE)
            print(new_position)


            img.convert() 
        
        
        
        
        # if rotation != 0:
        #     img = pygame.transform.rotate(img, rotation)

        screen.fill("#000000")
        screen.blit(img, new_position)
    

        
    """ Mise a jour de l'affichage """
    pygame.display.flip()
        

        #TO DO : Fonctions d'images
        # img = pygame.image.load(photo)
        # rotation = getRotation(photo)
        # if rotation != 0:
        #     img = pygame.transform.rotate(img, rotation)
        #     img = aspectScale(img, config.SCREEN_SIZE)
        # screen.blit(img, cornerPos(img,config.SCREEN_SIZE))
        # img = aspectScale(img, config.SCREEN_SIZE)
    
pygame.quit()