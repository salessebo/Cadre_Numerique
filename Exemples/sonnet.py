
#Lire un fichier
print("\nExemple 1: \n")
fichier  = open("sonnet.txt", "r", encoding='utf-8')
texte = fichier.read()
print(texte)
fichier.close()


#Lire un fichier ligne par ligne
print("\nExemple 2: \n")
fichier  = open("sonnet.txt", "r", encoding='utf-8')
ligne = fichier.readline()
while ligne != "":
    print(ligne)
    ligne = fichier.readline()
fichier.close()


#Inserer les lignes d'un fichier dans une liste
print("\nExemple 3: \n")
fichier  = open("sonnet.txt", "r", encoding='utf-8')
lignes = fichier.readlines()
for ligne in lignes:
    print(ligne[:-1])
fichier.close()

#with open as ferme automatiquement apres avoir terminé
print("\nExemple 4: \n")
mots = ["et","Et"]
with open("sonnet.txt", "r", encoding='utf-8') as fichier:
    ligne = fichier.readline()
    while ligne != "":
        if any(mot in ligne for mot in mots):
        #if "Et" in ligne or "et" in ligne:
            print(ligne.strip())
        ligne = fichier.readline()
        
print("\nExemple 5: \n")

import os
fichiers = os.listdir()
print(fichiers)

fichiers = os.listdir("C:/Users/Supreme/Downloads")
print(len(fichiers),fichiers[:10])

sub = 'zip'
print("\n".join(s for s in fichiers if "zip".lower() in s.lower()))
print(s for s in fichiers if "zip".lower() in s.lower())
print(len(list(s for s in fichiers if "zip".lower() in s.lower())),".zip files")
