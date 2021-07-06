import yaml

fichier = open("Exemples/categories.yaml", "r")
document = yaml.load(fichier)

print(document["sports"])
print(document["countries"])
