""""
2. Le Saloon

— Où est le saloon de ce trou perdu ?
Demanda l'inconnu au shérif après avoir refusé de s'identifier malgré le splendide 
formulaire que vous lui avez gracieusement fourni. Le shérif, ahuri par la confiance du
mystérieux cavalier, lui désigna un vieux bâtiment fraichement construit dont les vibrations 
de l'ambiance festive à l'intérieur parvenaient aux oreilles aiguisées du mystérieux cowboy.

Une fois à l'intérieur, le vacarme candide fut remplacé par un silence de mort. 
Après un long moment d'échange de regards furtifs du côté des fêtards, le nouvel arrivant 
dit d'une voix sèche : 

— J'ai soif, qu'est-ce qu'il y a à boire ?

Le barman consulta son inventaire puis annonça :
— J'ai seulement un fichier JSON. On aurait besoin d'un tech artist pour visualiser 
les données…

À ce moment, tout le bar se tourna vers vous et votre ordinateur.
 Aidez notre cowboy à commander son drink en lui bâtissant un outil pour afficher 
 dans un tableau les différents drinks à l'aide de PySide6.
 """

import sys
import json #librairy built in 

json_file = sys.argv[1]
print("JSON FILE >>>" + json_file) #on recup le path ici, il est copié dans le launch.json dans argv


#le try et except permetent de ne pas faire crash le programme sur le file n'est pas le bon
try:
    file = open(json_file) #fonction open avec le parametres json_file = la variable file
    data = json.load(file)
    #print(data)
    print(type(data))#permet de vérifier le type de la variable, ici il s'Agit d'un list équivalent de array de string en c++
except:
    print(f"Could not load data from {json_file}") #permet d'afficher un message d'erreur qui indique aussi le nom du fichier

#boucle for pour écrire ligne après ligne le data. Trois type a print voir plus bas

print("------- for loop qui print les key and values -------\n") #sert simplement a mieux visualiser les différences pour mes notes, a commenter plus tard
#for loop key and values
for i in data:
    print(f"    - {i}") #print les valeurs et leur type



print("\n")

print("------- for loop qui print les key -------\n")#sert simplement a mieux visualiser les différences pour mes notes, a commenter plus tard
#for loop key
for i in data:
     for k in i.keys(): #le dict contient des keys, aucune idée c'Est quoi
            print(f"    - {k}") #print le nom des keyss


print("\n")

print("------- for loop qui print les items -------\n")#sert simplement a mieux visualiser les différences pour mes notes, a commenter plus tard
#for loop values, 
for i in data:
    for e in i.items(): #afficher que les valeurs
        print(f"    - {e}") 
         
#i est un dict, donc un array contenant des array qui contiennent des tuple, les tuple sont composé de paire key and value

print("\n")

#version différente comme dans exemple

print("version différente mieux organiser les différents types")
for i in data:
    print("Keys\n")
    for k in i.keys():
          print(f"    - {k}")  
    print("\n")    
    print("Values\n")
    for v in i.values():
        print(f"     - {v}")
    print("\n")  
    print("items\n")  
    for e in i.items():
         print(f"     - {e}")
    print("\n")
