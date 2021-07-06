from Album import Album
from Config import Config
import os
import pygame

class ListePhotos():
    def __init__(self, path):
        extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
        self.listePhotos = []
        listeTmp = os.listdir(path)
        for photo in listeTmp:
            filename, ext = os.path.splitext(photo)
            e = ext.lower()
            if e in extensions:
                self.listePhotos.append(path + photo)
        self.photoCourante = 0
        self.noImage = "no-image.png"
    def getPhoto(self):
        
        if self.photoCourante < (len(self.listePhotos) - 1):
            photo = self.listePhotos[self.photoCourante]            
            self.photoCourante = self.photoCourante + 1
        else:
            self.photoCourante = 0
            try:
                photo = self.listePhotos[self.photoCourante]
            except:
                pass
            
        if len(self.listePhotos) == 0:
            photo = self.noImage
                       
        return(photo)
if __name__ == "__main__":
    print ("Début du test\n")
        #################################
    #test_album = ListePhotos(r'C:\Users\Supreme\Desktop\Projet_3\albums\album1')
    # config = Config()
    # album = Album(config)
    # test_album = ListePhotos(album.getAlbumCourant())
    test_album = ListePhotos('C:/Users/Supreme/Desktop/Projet_3/albums/album1')
    print(test_album.getPhoto())
    print("\nFin du test")