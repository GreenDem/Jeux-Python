import random

def deal(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

J=11
Q=12
K=13
A=14
fullPack=[2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,J,J,J,J,Q,Q,Q,Q,K,K,K,K,A,A,A,A]
player1=[]
player2=[]
desk=[]



# print(fullPack)
random.shuffle(fullPack)
# print(fullPack)
player1,player2=deal(fullPack)
# print(player1)
# print(player2)

p1=len(player1)
p2=len(player2)
manche=0
manches2=0
bataille=0

# print(p1)
# print(p2)

if p1>0 and p2>0:
    while p1>0 and p2>0:
        print("Player 1 joue " + str(player1[0]))
        print("Player 2 joue " + str(player2[0]))
        manche=manche+1
        manches2=manches2+1

        player1[0]
        player2[0]

        # Pour eviter les parties infinis
        if manche == 2000:
            random.shuffle(player1)
            random.shuffle(player2)
            manche=0

        # PLAYER 1 WIN LA MANCHE
        elif player1[0]> player2[0] :
            player1.append(player1[0])
            player1.append(player2[0])
            del player2[0]
            del player1[0]

        # PLAYER 2 WIN LA MANCHE
        elif player1[0]< player2[0] :
            player2.append(player1[0])
            player2.append(player2[0])
            del player1[0]
            del player2[0]
                    
        # BATAILLE
        else:
            while player1[0]==player2[0] and p1>0 and p2>0:
                print("BATAILLE")
                bataille=bataille+1

                if p1==2:
                    desk.append(player2[0])
                    del player2[0]
                    desk.append(player1[0])
                    del player1[0]
                    desk.append(player2[0])
                    del player2[0]
                    if player1[0]> player2[0] :
                        print("Player 1 joue " + str(player1[0]))
                        print("Player 2 joue " + str(player2[0]))
                        player1.append(player1[0])
                        player1.append(player2[0])
                        player1.extend(desk)
                        del player2[0]
                        del player1[0]
                        desk.clear()
                        print("Player 1 wins BATAILLE")

                    elif player1[0]< player2[0] :
                        print("Player 1 joue " + str(player1[0]))
                        print("Player 2 joue " + str(player2[0]))
                        player2.append(player1[0])
                        player2.append(player2[0])
                        player2.extend(desk)
                        del player2[0]
                        del player1[0]
                        desk.clear()
                        print("Player 2 wins BATAILLE")

                elif p1==1:
                    desk.append(player2[0])
                    del player2[0]
                    desk.append(player2[0])
                    del player2[0]
                    if player1[0]> player2[0] :        
                        print("Player 1 joue " + str(player1[0]))
                        print("Player 2 joue " + str(player2[0]))
                        player1.append(player1[0])
                        player1.append(player2[0])
                        player1.extend(desk)
                        del player2[0]
                        del player1[0]
                        desk.clear()
                        print("Player 1 wins BATAILLE")
                    elif player1[0]< player2[0] :
                        print("Player 1 joue " + str(player1[0]))
                        print("Player 2 joue " + str(player2[0]))
                        player2.append(player1[0])
                        player2.append(player2[0])
                        player2.extend(desk)
                        del player2[0]
                        del player1[0]
                        desk.clear()
                        print("Player 2 wins BATAILLE")

                elif p2==2:
                    desk.append(player1[0])
                    del player1[0]
                    desk.append(player1[0])
                    del player1[0]
                    desk.append(player2[0])
                    del player2[0]
                    if player1[0]> player2[0] :
                        print("Player 1 joue " + str(player1[0]))
                        print("Player 2 joue " + str(player2[0]))
                        player1.append(player1[0])
                        player1.append(player2[0])
                        player1.extend(desk)
                        del player2[0]
                        del player1[0]
                        desk.clear()
                        print("Player 1 wins BATAILLE")

                    elif player1[0]< player2[0] :
                        print("Player 1 joue " + str(player1[0]))
                        print("Player 2 joue " + str(player2[0]))
                        player2.append(player1[0])
                        player2.append(player2[0])
                        player2.extend(desk)
                        del player1[0]
                        del player2[0]
                        desk.clear()
                        print("Player 2 wins BATAILLE")

                elif p2==1:
                    desk.append(player1[0])
                    del player1[0]
                    desk.append(player1[0])
                    del player1[0]            
                    if player1[0]> player2[0] :
                        print("Player 1 joue " + str(player1[0]))
                        print("Player 2 joue " + str(player2[0]))
                        player1.append(player1[0])
                        player1.append(player2[0])
                        player1.extend(desk)
                        del player2[0]
                        del player1[0]
                        desk.clear()
                        print("Player 1 wins BATAILLE")

                    elif player1[0]< player2[0] :
                        print("Player 1 joue " + str(player1[0]))
                        print("Player 2 joue " + str(player2[0]))
                        player2.append(player1[0])
                        player2.append(player2[0])
                        player2.extend(desk)
                        del player1[0]
                        del player2[0]
                        desk.clear()
                        print("Player 2 wins BATAILLE")

                else:
                    desk.append(player1[0])
                    del player1[0]
                    desk.append(player2[0])
                    del player2[0]
                    desk.append(player1[0])
                    del player1[0]
                    desk.append(player2[0])
                    del player2[0]
                    if player1[0]> player2[0] :
                        print("Player 1 joue " + str(player1[0]))
                        print("Player 2 joue " + str(player2[0]))
                        player1.append(player1[0])
                        player1.append(player2[0])
                        player1.extend(desk)
                        del player2[0]
                        del player1[0]
                        desk.clear()
                        print("Player 1 wins BATAILLE")

                    elif player1[0]< player2[0] :
                        print("Player 1 joue " + str(player1[0]))
                        print("Player 2 joue " + str(player2[0]))
                        player2.append(player1[0])
                        player2.append(player2[0])
                        player2.extend(desk)
                        del player1[0]
                        del player2[0]
                        desk.clear()
                        print("Player 2 wins BATAILLE")

                p1=len(player1)
                p2=len(player2)
                print(str(p1) + " player 1 fin bataille" )
                print(str(p2) + " player 2 fin bataille" )
                print("FIN BATAILLE")
                if p1==0 or p2==0:
                    break


        p1=len(player1)
        p2=len(player2)

        p1=len(player1)
        p2=len(player2)
        print("-----------RESUMER-----------")
        print("Player 1 à " + str(p1) + " carte(s) à la fin de la manche")
        print("Player 2 à " + str(p2) + " carte(s) à la fin de la manche")

        print(str(manches2) + " Manche(s)")
        print("Nombres de batailles : " + str(bataille))
        print("Nombres de reset : " + str(manches2//2000))
        if p2==0:
            print("PLAYER 1 WINS")
        elif p1==0:
            print("PLAYER 2 WINS")