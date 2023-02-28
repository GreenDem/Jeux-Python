
# Sans utiliser Internet, vous devez écrire un programme permettant de trouver, en un maximum de 7 tentatives, les lettres qui constitue le mot saisi par l’utilisateur (joueur 1).

# Pour chaque tentative :

# •	Dans le cas où le joueur trouve une lettre, vous afficherez la lettre trouvée à la/les bonne(s) position(s) sinon vous afficherez des « _ »
# Exemple : 
# 	Le joueur 1 saisi le mot « bonjour »
# 	Le joueur 2 saisi le lettre « o »
# _ o _ _ o _ _

# •	Dans le cas où le joueur donne une mauvaise lettre, vous décrémenterez le nombre de tentatives et vous afficherez « Raté ! » avec le nombre de tentatives restantes suivi des lettres déjà trouvées au préalable
# Exemple : 
# 	Le joueur 1 saisi le mot « bonjour »
# 	Le joueur 2 saisi le lettre « p »
# « Raté ! il vous reste 5 tentatives »
# _ o _ _ o _ _ 

# Si le mot est découvert en moins de 7 tentatives, vous devez arrêter la saisi et afficher « C’est gagné !!! ».

# Si les 7 tentatives sont atteintes sans avoir trouvé toutes les lettres, affichez : « C’est perdu… »
from copy import copy


# MISE EN PLACE DES 2 LISTES
letter=[]

myStr=input("Joueur 1: Choisis ton mot  : ")
for character in myStr:
    letter.append(character)

tips=copy(letter)
refer=copy(letter)
letterNb=len(letter)
z="-"*letterNb

# Mise en place des TIPS

tips[0:letterNb]=z

# set(l1) & set(l2) => comparer 

# DEMARRAGE DU JEU

# while tentatives<=7:

correct=0
tentatives=0

while tentatives<=7:
    hang=input("Lettre ? \o/  :")
    x=0

    if hang in refer:
        for x in range (x, x+letterNb) :
            
            if hang==letter[x] :
                tips[x]=hang
                x=x+1
                correct=correct+1
                refer.remove(*hang)

    else :
        tentatives=tentatives+1

    print(tips)
    print(str(correct) + " nombres de correct")
    print("Tentatives restantes " + str(7-tentatives))
    correct2=int(letterNb-correct)
    print(str(correct2) + " lettres restante à decouvrir")

    if correct2==0:
        break

if correct2==0:
    print("Bravo")
else:
    print("T'es nul")

