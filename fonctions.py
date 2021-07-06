from PIL import Image, ExifTags
from Album import Album
from ListePhotos import ListePhotos

def getRotation(fichier):
    img = Image.open(fichier) 
    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation]=='Orientation':
            break
    print("Orientation (Indice) : ", orientation)

    try:
        exifData = img._getexif()
        print("Orientation (Valeur) : ", exifData[orientation])
    except:
        print("Pas d'EXIF data")
        
        
getRotation("no-image.png")
getRotation("test.jpg")

def aspectScale(img,tailleEcran):
    # Utiliser Pillow
    # Mettre a l'echelle l'fichier 'img' pour s'ajuster à 'tailleEcran'.
    # Respecter les proportion de l'fichier originale
    pass
  
def cornerPos(img, tailleEcran):
    # Position du coin de l'fichier
    pass
  
def event_btnAlbum(channel):
    print("Event: Bouton Album")
  
def event_btnVeille(channel):
    #global etat
    if etat == SystemeEtat.VEILLE:
        etat = SystemeEtat.ALLUME
    else:
        etat = SystemeEtat.VEILLE
#test Modif
