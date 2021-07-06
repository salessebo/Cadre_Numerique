from PIL import Image, ExifTags

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


def aspectScale(img,tailleEcran):
    # Utiliser Pillow (ou pas)
    # Mettre a l'echelle l'fichier 'img' pour s'ajuster à 'tailleEcran'.
    # Respecter les proportion de l'fichier originale
    rect = img.get_rect() 

    img_width = rect[2]-rect[0]
    img_height = rect[3]-rect[1]
    img_ratio = img_width/img_height
    print("img_ratio :", img_ratio)
    print("img_width :", img_width)
    print("img_height :", img_height)
    
    if img_width<img_height:    #type portrait
        ajustement = tailleEcran[1]/img_height
        print(tailleEcran[1] > img_height)
    else:                       #type paysage
        ajustement = tailleEcran[0]/img_width
        print("fit :", tailleEcran[0] > img_width)

    if ajustement < 1:          #Si le cadre est plus petit que la photo
        print("ajustement :", ajustement)
        img_width = int(ajustement*img_width)
        img_height = int(ajustement*img_height)
        print("new size :", img_width, img_height)

    return img_width, img_height

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
        
        
# getRotation("no-image.png")
# getRotation("test.jpg")