def creation_plateau (taille): 
    
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    plateau=[] #Liste finale
    for i in range (0,taille+1): #pour i lignes (car on perd la premiere ligne à cause des lettres des colonnes)
        liste=[] #liste de la liste finale contenant chaque ligne
        
        #Affichage lettre de colonne
        for j in range (0,taille+1): #pour j colonnes (car on perd la premiere colonne à cause des numéros des lignes)
            if (i==0) and (j==0):
                liste.append('  ') #Affichage d'un espace  en haut à gauche du tableau 
                
            elif (i==0):
                liste.append(alphabet[j-1]) #Affichage des lettres à chaque ligne (j-1 car la première lettre de l'alphabet commence à l'indice 0)        
        
            elif (j==0): #Pour le premier indice on affiche les numeros de lignes
                liste.append(i)
                
            else:
                liste.append('.')
                
        plateau.append(liste) # on ajoute la liste au plateau puis on reinitialise la liste
    return (plateau)





        
def initialisation_pions(plateau,taille):
    #on positionne à chaque fois les X et les O en diagonales (positioner au centre du plateau)
    plateau[int(taille/2)][int(taille/2)+1]= 'X' 
    plateau[int(taille/2)+1][int(taille/2)] = 'X'
    
    plateau[int(taille/2)][int(taille/2)]= 'O' 
    plateau[int(taille/2)+1][int(taille/2)+1] = 'O'
    


    
def saisie_coordonnees_pions(symb,plateau,taille):    
    #Saisie des coordonnées du symbole à ajouter
    coord=input("Saisir les coordonnées du pion à placer (ex : C3) : ")
    coord=coord.upper() #conversion en majuscule

    #Saisie securisée
    x=cases_valides(symb,plateau,taille) #Liste contenant toute les cases valides sous forme ['A1','B2',...]
    while (coord not in x):
        print("Coordonnées invalides !")
        coord=input("Saisir les coordonnées du pion à placer (ex : C3) : ")
        coord=coord.upper() #conversion en majuscule
        print()
        
    return(coord)
    
    
    
def placement_pion (symb,coord,plateau):
    
    #Attribution à la colonne un numéro j et pas une lettre
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    j=1
    while (coord[0] != alphabet[j-1]): 
        j=j+1
    
    #Transformation de la chaine de caractere contenant le numero de ligne en un entier
    if (len(coord) == 3): #si le numero de ligne contient deux éléments
        i=int(coord[1] + coord[2])
    else: # s'il en contient un seul
        i=int(coord[1])

    plateau [i][j] = symb #Modification du plateau
    
    
def cases_valides(symb,plateau,taille): 
    liste=[]
    
    #Attribution en fonction du pion qui cherche à jouer et du pion de l'adversaire
    if (symb=='X'):
        symb_inv='O'
    elif (symb=='O'):
        symb_inv='X'
    
    #On parcours le tableau et on verifie les cases valides avec des conditions
    for i in range (1,taille+1):
        for j in range (1,taille+1):
            if (plateau[i][j] == '.'): #condition initiale
                
                #case au dessus a gauche
                if (i>=3) and (j>=3) and (plateau[i-1][j-1]==symb_inv): #On etudie seulement cette case si elle se situe au moins à la 3ème ligne et colonne
                    a=1 #Initialisation
                    while (i-a !=0) and (j-a !=0) and (plateau[i-a][j-a]==symb_inv): #Tant que la ligne n’est pas celle d’indice 0 et les cases au-dessus a gauche sont des pions adverses
                        a=a+1 #On incrémente 1 pour étudier à chaque itération la ligne au-dessus a gauche
                    #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
                    if (i-a !=0) and (j-a!=0) and (plateau[i-a][j-a]==symb): #On verifie que la case est dans le plateau jouable et que cette case est un pion au joueur
                        liste.append(j)
                        liste.append(i)
                        
                #case au dessus
                if (i>=3) and (plateau[i-1][j]==symb_inv): #On etudie seulement cette case si elle se situe au moin a la 3ème ligne 
                    a=1 #Initialisation
                    while (i-a != 0) and (plateau[i-a][j]==symb_inv):
                        a=a+1#On incrémente 1 pour étudier à chaque itération la ligne au-dessus
                    #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
                    if (i-a !=0) and (plateau[i-a][j]==symb): #On verifie que la case est dans le plateau jouable et que cette case est un pion au joueur
                        liste.append(j)
                        liste.append(i)
                        
                #case au dessus a droite 
                if (i >=3) and (j+1 <= taille) and (plateau[i-1][j+1]==symb_inv): #On etudie seulement cette case si elle se situe au moins a la 3ème ligne et que la colonne est inferieur a la taille
                    a=1 #Initialisation
                    while (i-a !=0) and (j+a <= taille) and (plateau[i-a][j+a]==symb_inv):
                        a=a+1 #On incrémente 1 pour étudier à chaque itération la ligne au-dessus a droite
                    #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
                    if (i-a !=0) and (j+a <= taille) and (plateau[i-a][j+a]==symb): #On verifie que la case est dans le plateau jouable et que cette case est un pion au joueur
                        liste.append(j)
                        liste.append(i)
                        
                #case a gauche
                if (j>=3) and (plateau[i][j-1]==symb_inv): #On etudie seulement cette case si elle se situe au moins a la 3ème colonne 
                    a=1 #Initialisation
                    while (j-a !=0) and (plateau[i][j-a]==symb_inv):
                        a=a+1 #On incrémente 1 pour étudier à chaque itération la ligne a gauche
                    #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
                    if (j-a !=0) and (plateau[i][j-a]==symb): #On verifie que la case est dans le plateau jouable et que cette case est un pion au joueur
                        liste.append(j)
                        liste.append(i)
                        
                #case a droite
                if (j+1 <= taille) and (plateau[i][j+1]==symb_inv): #On etudie seulement cette case si sa colonne est inferieur a la taille
                    a=1 #Initialisation
                    while (j+a <= taille) and (plateau[i][j+a]==symb_inv):
                        a=a+1 #On incrémente 1 pour étudier à chaque itération la ligne a droite
                    #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
                    if (j+a <= taille) and (plateau[i][j+a]==symb): #On verifie que la case est dans le plateau jouable et que cette case est un pion au joueur
                        liste.append(j)
                        liste.append(i)
                        
                #case en dessous a gauche
                if (i+1 <= taille) and (j>=3) and (plateau[i+1][j-1]==symb_inv): #On etudie seulement cette case si elle se situe au moins a la 3ème colonne et la ligne est inferieure a la taille
                    a=1 #Initialisation
                    while (i+a <= taille) and (j-a!=0) and (plateau[i+a][j-a]==symb_inv):
                        a=a+1 #On incrémente 1 pour étudier à chaque itération la ligne au-dessous a gauche
                    #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
                    if (i+a <= taille) and (j-a!=0) and (plateau[i+a][j-a]==symb): #On verifie que la case est dans le plateau jouable et que cette case est un pion au joueur
                        liste.append(j)
                        liste.append(i)
                        
                #case en dessous
                if (i+1 <= taille) and (plateau[i+1][j]==symb_inv): #On etudie seulement cette case si sa ligne est inferieure a la taille
                    a=1 #Initialisation
                    while (i+a <= taille) and (plateau[i+a][j]==symb_inv) :
                        a=a+1 #On incrémente 1 pour étudier à chaque itération la ligne au-dessous 
                    #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
                    if (i+a <= taille) and (plateau[i+a][j]==symb): #On verifie que la case est dans le plateau jouable et que cette case est un pion au joueur
                        liste.append(j)
                        liste.append(i)
                        
                #case en dessous a droite
                if (i +1 <= taille) and (j+1 <= taille) and (plateau[i+1][j+1]==symb_inv): #On etudie seulement cette case si ligne et sa colonne est inferieur a la taille
                    a=1 #Initialisation
                    while (i+a <= taille) and (j+a <= taille) and (plateau[i+a][j+a]==symb_inv): 
                        a=a+1 #On incrémente 1 pour étudier à chaque itération la ligne au-dessous a droite
                    #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
                    if (i+a <= taille) and (j+a <= taille) and (plateau[i+a][j+a]==symb): #On verifie que la case est dans le plateau jouable et que cette case est un pion au joueur
                        liste.append(j)
                        liste.append(i)              
    
    
    #Creation d'une liste du type ['A2','B8',...]
    liste1=[]
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(0,len(liste)):
        if (i%2 ==0):
            liste1.append(alphabet[liste[i]-1] + str(liste[i+1]))
    
    
    return (liste1)


def reverse_pion(plateau,coord,pion,taille):
    
    #ATTRIBUTION DE I ET DE J
    #Numero de ligne
    if (len(coord)==2):
        i=int(coord[1])
    elif (len(coord)==3):
        i=int(coord[1] + coord[2])
    
    #Numero de colonne
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    j=1
    while (coord[0] != alphabet [j-1]):
        j=j+1    
    
    
    #Attribution en fonction du pion qui cherche a jouer du pion de l'adversaire
    if (pion=='X'):
        pion_inv='O'
    elif (pion=='O'):
        pion_inv='X'
        
    #ETUDE DE TOUTES LES POSSIBILITEES
    
    #case au dessus a gauche
    if (i-1 != 0) and (j-1 != 0) and (plateau[i-1][j-1]==pion_inv): 
        a=1 #initialisation de a
        while (i-a != 0) and (j-a !=0) and (plateau[i-a][j-a]==pion_inv): #tant que la case étudiée contient un pion inverse
            a=a+1 #on incrémente a pour étudier les cases suivantes dans la diagonale
        #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
        if (i-a != 0) and (j-a !=0) and (plateau[i-a][j-a]==pion):  
            for b in range (1,a):
                plateau[i-b][j-b]=pion #on place un pion joueur à la place du pion inverse
                
    #case au dessus            
    if (i-1 != 0) and (j!=0) and (plateau[i-1][j]==pion_inv): #tant que la case étudiée contient un pion inverse
        a=1
        while (i-a != 0) and (plateau[i-a][j]==pion_inv):
            a=a+1 #on incrémente a pour étudier les cases suivantes dans la colonne au dessus
        #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
        if (i-a != 0) and (plateau[i-a][j]==pion):
            for b in range (1,a):
                plateau[i-b][j]=pion #on place un pion joueur à la place du pion inverse
    
    #case au dessus a droite
    if (i-1 != 0) and (j+1 <= taille) and (plateau[i-1][j+1]==pion_inv): #tant que la case étudiée contient un pion inverse
        a=1
        while (i-a != 0) and (j+a <= taille) and (plateau[i-a][j+a]==pion_inv):
            a=a+1 #on incrémente a pour étudier les cases suivantes dans la diagonale
        #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
        if (i-a != 0) and (j+a <= taille) and (plateau[i-a][j+a]==pion):
            for b in range (1,a):
                plateau[i-b][j+b]=pion #on place un pion joueur à la place du pion inverse
    
    #case a gauche
    if (j-1 != 0) and (plateau[i][j-1]==pion_inv): #tant que la case étudiée contient un pion inverse
        a=1
        while (j-a != 0) and (plateau[i][j-a]==pion_inv):
            a=a+1 #on incrémente a pour étudier les cases suivantes dans la ligne à gauche
        #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
        if (j-a != 0) and (plateau[i][j-a]==pion):
            for b in range (1,a):
                plateau[i][j-b]=pion #on place un pion joueur à la place du pion inverse
    
    #case a droite
    if (j+1 <= taille) and (plateau[i][j+1]==pion_inv): #tant que la case étudiée contient un pion inverse
        a=1
        while (j+a <= taille)and (plateau[i][j+a]==pion_inv):
            a=a+1 #on incrémente a pour étudier les cases suivantes dans la ligne à droite
        #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
        if (j+a <= taille) and (plateau[i][j+a]==pion):
            for b in range (1,a):
                plateau[i][j+b]=pion #on place un pion joueur à la place du pion inverse
    
    #case en dessous a gauche
    if (i+1 <= taille) and (j-1 !=0) and (plateau[i+1][j-1]==pion_inv): #tant que la case étudiée contient un pion inverse
        a=1
        while (i+a <= taille) and (j-a !=0) and (plateau[i+a][j-a]==pion_inv):
            a=a+1 #on incrémente a pour étudier les cases suivantes dans la diagonale
        #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
        if (i+a <= taille) and (plateau[i+a][j-a]==pion):
            for b in range (1,a):
                plateau[i+b][j-b]=pion #on place un pion joueur à la place du pion inverse
    
    #case en dessous    
    if (i+1 <= taille) and (plateau[i+1][j]==pion_inv): #tant que la case étudiée contient un pion inverse
        a=1
        while (i+a <= taille) and (plateau[i+a][j]==pion_inv):
            a=a+1 #on incrémente a pour étudier les cases suivantes dans la colonne en dessous
        #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
        if (i+a <= taille) and (plateau[i+a][j]==pion):
            for b in range (1,a):
                plateau[i+b][j]=pion #on place un pion joueur à la place du pion inverse
    
    #case au dessous a droite
    if (i+1 <= taille) and (j+1 <= taille) and (plateau[i+1][j+1]==pion_inv): #tant que la case étudiée contient un pion inverse
        a=1
        while (i+a <= taille) and (j+a <= taille) and (plateau[i+a][j+a]==pion_inv):
            a=a+1 #on incrémente a pour étudier les cases suivantes dans la diagonale
        #Une fois que la case n'est plus un pion adverse alors on regade si la case suivante est un pion au joueur
        if (i+a <= taille) and (j+a <= taille) and (plateau[i+a][j+a]==pion):
            for b in range (1,a):
                plateau[i+b][j+b]=pion #on place un pion joueur à la place du pion inverse
                
                
                
                
                
                
                
def creation_menu(pion,tour,plateau):
    
    #Compteur nombre de pions
    nb_X=0
    nb_O=0
    for i in range (1,len(plateau)):
        for j in range (1,len(plateau)):
            if (plateau[i][j] == 'X'):
                nb_X=nb_X +1
            elif (plateau[i][j] == 'O'):
                nb_O=nb_O +1
    
    menu=[[' ']]
    #Creation menu
    for i in range (1,12):
        liste=[]
        if (i==1):
            menu.append("TOUR " + str(tour))
        elif (i==2):
            menu.append(" C'est le tour de" + pion)
        elif (i==3):
            menu.append(pion + "vous pouvez jouer")
        elif(i==4):
            menu.append(' ')
        elif(i==5):
            menu.append(" Pion :" + 'O' + ' '  + str(nb_O) )
        elif(i==6):
            menu.append('       ' + 'X' + ' ' + str(nb_X) )
        elif(i==7):
            menu.append(' ')
        elif (i==8):
            menu.append("Commandes :")
        elif (i==9):
            menu.append(" P : Placer un pion")
        elif (i==10):
            menu.append(" A : Affichage cases valides")
        elif(i==11):
            menu.append(" Q : Quitter la partie")
                
    return (menu)


    
def affichage(symb,plateau,taille,action,menu):
    W="\033[0m"       #Noir
    R="\033[31m"      #Rouge
    O="\033[33m"      #Orange
    B="\033[34m"      #Bleu
    G="\033[32m"      #Vert
    
    
    #CREATION D'UNE LISTE AVEC LES CASES VALIDES SOUS FORME [[j,i]...]
    pion_valide=cases_valides(symb,plateau,taille)
    #Création d'une liste avec numéro de colonne a la place des lettres et de str --> int
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    liste=[]#liste finale
    for i in range(0,len(pion_valide)): #on parcourt de la liste pion_valide
        liste1=[] #liste de transition
        cpt=1
        while(pion_valide[i][0] != alphabet [cpt-1]): #attribution a la place d'une lettre de colonne, un chiffre équivalent = cpt
            cpt=cpt+1
        liste1.append(cpt)
        if (len(pion_valide[i]) == 2): #en fonction du nombre d'argument de ex : (taille(C3) ≠ taile(C15))
            liste1.append(int(pion_valide[i][1]))
        elif (len(pion_valide[i]) == 3):
            liste1.append(int(pion_valide[i][1] + pion_valide[i][2]))
        liste.append(liste1) # a chaque fin de conversion d'une case, on ajoute cette case et reinitialise la liste de transition
        
        
    #Affichage general
    for i in range (0,taille+1):
        
        #AFFICHAGE PLATEAU
        for j in range (0,taille+1):
            
            #Affichage symbole en couleur
            if (plateau[i][j] =='X') and (i!=0): #Pour ne pas afficher la colonne X en rouge
                print(R,plateau[i][j],end='')
            elif (plateau[i][j] == 'O') and (i!=0): #Pour ne pas afficher la colonne O en rouge
                print(B,plateau[i][j],end='')
            
            #Affichage des numeros de lignes et de colonnes en couleur
            elif (i==0):
                print(O,plateau[i][j],end='') #Affichage numero colonne en couleur
            elif (j==0 and (i < 10)):
                print(O,plateau[i][j],end='') #Affichage numero ligne et colonne en couleur
                print(' ',end='')
            elif (j==0 and (i >= 10)):
                print(O,plateau[i][j],end='') #Affichage numero ligne et colonne en couleur
            
            #affichage des cases où il est possible de jouer
            elif(action=='A') and ([j,i] in  (liste)):
                print(G,'?',end='') #Affichage case valide
                
            #Affichage des cases du tableau avec des  '.'
            else:
                print(' ',end='')
                print(plateau[i][j],end='')
            print(W,'',end='')#reinitialisation de la couleur
        
        
        #AFFICHAGE MENU
        
        #Affichage espace
        print(10*' ',end='') #Affichage de 10 espaces entre le tableau et le menu
        
        #Affichage nom en orange : 
        if (i==8) or (i==1):
            print(O,menu[i],end='')
            
        #Affichage X et O en couleur
        elif (i<12):
            for j in range (0,len(menu[i])):
                    if ((i==2) and (j==17)) or ((i==3) and (j==0)):
                        if (menu[i][j] =='X'):
                            print(R,menu[i][j],end='')
                        elif (menu[i][j] =='O'):
                            print(B,menu[i][j],end='')
                        print(W,'',end='')
            
                    #affichage pions en couleurs lignes 5 et 6
                    elif ((i==5) and (j==7)) :
                        print(B,menu[i][j],end='')
                    elif ((i==6) and (j==7)) :
                        print(R,menu[i][j],end='')
                
                    else:
                        print(menu[i][j],end='')
        print(W,'')
    
    #Affichage des éléments du menu qui n'ont pas pu être affichés a la suite du plateau
    for j in range(i+1,12):
        print('  ' + ((taille*3) * ' ') + (11* ' '),end='')
        if (j==8):
            print(' ' + O,menu[j])
        else:
            print(W,menu[j])
            

def condition_arret(plateau,taille):
    point=0 #initialisation d'un compteur de '.' étant dans le plateau
    valide=0
    for i in range (1,taille+1): #on parcourt le plateau
        for j in range (1,taille+1):
            if plateau[i][j]=='.': #s'il y a un '.' sur le plateau
                point=point+1 #alors on incrémente le compteur point de +1
                
    #si la liste de cases valides ne contientt aucun élément pour le pion X et le pion O, la varaible valide prend la valeur de 1
    #ou si le plateau est plein c'est-à-dire qu'il n'y a plus de '.' sur le plateau
    if ((len(cases_valides('X',plateau,taille))==0) and (len(cases_valides('O',plateau,taille))==0)) or (point==0): 
        valide=1 
        
    return (valide)


def affichage_résultat_multi (nom1,nom2,changer,plateau,taille):
    #Détermination du gagnant
    symbX=0 #compteur des pions 'O'
    symbO=0 #compteur des pions 'X'
    for i in range (1,taille+1): #on parcourt toutes les lignes
        for j in range (1,taille+1):# et toutes les colonnes du plateau
            if plateau[i][j]=='X': #s'il y a un pion 'X' sur le plateau
                symbX=symbX+1 #on incrémente le compteur de +1
            elif plateau[i][j]=='O': #s'il y a un pion 'O' sur le plateau
                symbO=symbO+1 #on incrémente le compteur de +1
                
    if (changer != 'change'):      
        if (symbX)>(symbO):
            print("BRAVO",nom1,"gagne")
        elif (symbX)<(symbO):
            print("BRAVO",nom2,"gagne")
        elif (symbX==symbO):
            print("Match nul")
    elif (changer == 'change'):      
        if (symbX)>(symbO):
            print("BRAVO",nom2,"gagne")
        elif (symbX)<(symbO):
            print("BRAVO",nom1,"gagne")
        elif (symbX==symbO):
            print("Match nul")
            
def affichage_résultat_solo (nom,changer,plateau,taille):
    #Détermination du gagnant
    symbX=0 #compteur des pions 'O'
    symbO=0 #compteur des pions 'X'
    for i in range (1,taille+1): #on parcourt toutes les lignes
        for j in range (1,taille+1):# et toutes les colonnes du plateau
            if plateau[i][j]=='X': #s'il y a un pion 'X' sur le plateau
                symbX=symbX+1 #on incrémente le compteur de +1
            elif plateau[i][j]=='O': #s'il y a un pion 'O' sur le plateau
                symbO=symbO+1 #on incrémente le compteur de +1
                
    if (changer != 'change'):      
        if (symbX)>(symbO):
            print("BRAVO",nom,"! Vous avez gagné")
        elif (symbX)<(symbO):
            print("DOMMAGE, l'ordinateur gagne")
        elif (symbX==symbO):
            print("Match nul")
    elif (changer == 'change'):      
        if (symbX)>(symbO):
            print("DOMMAGE, l'ordinateur gagne")
        elif (symbX)<(symbO):
            print("BRAVO",nom,"! Vous avez gagné")
        elif (symbX==symbO):
            print("Match nul")


def timer_4s():
    for i in range (0,100000000):
        x=1
        
def suppr_console():
    for i in range (0,100):
        print()
