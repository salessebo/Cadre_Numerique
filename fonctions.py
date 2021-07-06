def getRotation(fichier):
    # Utiliser Pillow
    # Extraire l'information EXIF de rotation de l'image
    pass

def aspectScale(img,tailleEcran):
    # Utiliser Pillow
    # Mettre a l'echelle l'image 'img' pour s'ajuster à 'tailleEcran'.
    # Respecter les proportion de l'image originale
    pass
  
def cornerPos(img, tailleEcran):
    # Position du coin de l'image
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
