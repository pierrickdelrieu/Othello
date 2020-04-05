#DONNEES
from my_fcts import * #fichier contenant toutes les fonctions
import random #choix aleatoire pour mode solo


#.............................................................................MENU_PRESENTATION............................................................................
suppr_console()
#Initialisation des couleurs
R= "\033[31m" #rouge
B= "\033[34m" #bleu
W= "\033[0m"  #blanc
O= "\033[33m" #orange

print(45*' ' + O,"Black & White") #titre
print(W,'')
print("Le jeu de Black & White est un jeu qui se joue à deux joueurs, l’un joue avec le camp des pions",R,"X",W,", l’autre avec le camp des pions",B,"O",W,".") #Regle

print(W," ") #Réinitialisation de la couleur + saut de ligne

#Entrez pour continuer
continuer=input("Appuyez sur entrer pour continuer ")
while (continuer):
    print()
    continuer=input("Appuyez sur entrer pour continuer ")
suppr_console()
    
print("Bienvenue,")
print()

recommencer = 'R' #Initialisation de la variable
while (recommencer =='R'): #Condition pour recommencer
    
    #Choix du mode
    mode=input(("Choisissez en mode : multijoueur (M) ou solo (S) : "))
    mode=mode.upper() #conversion en majuscule
    while (mode != 'M') and (mode != 'S'): #Saisie sécurisée
        mode=input(("Choisissez en mode : multijoueur (M) ou solo (S) : "))
        mode=mode.upper() #conversion en majuscule
    print()
    
    
    
    
    
#............................................................................PROGRAMME EN MODE MULTIJOUEUR............................................................................
    if (mode== 'M'):

        #Saisie nom des joueurs
        print("Entrez le nom des joueurs")
        
        nom1=input("Joueur 1 : ")
        nom1=nom1.capitalize() #Conversion de type Prénom
    
        nom2=input("Joueur 2 : ")
        nom2=nom2.capitalize() #Conversion de type Prénom
        print()
      
        print("Bonjour",R,(nom1),W,"et",B,(nom2))
        print()



        #Attribution des pions
        pion1='X'
        pion2='O'

        print(W,"Le pion de",R,(nom1),W,"est ",R,(pion1))
        print(W,"Le pion de",B,(nom2),W,"est ",B,(pion2))
        print(W," ") #Réinitialisation de la couleur + saut de ligne
    
        #Possibilité de changement de pion
        changer=input("Saississez 'change' pour changer de pion, sinon appuyez sur entrer ")
        changer=changer.lower() #conversion en minuscule

        while (changer != 'change') and (changer): #Saisie sécurisée
            changer=input("Saississez 'change' pour changer de pion, sinon appuyez sur entrer ")
            changer=changer.lower() #conversion en minuscule

        if (changer=='change') : #Affichage du changement
            pion1='O'
            pion2='X'
            print(W,"Le pion de",B,(nom1),W,"est",B,(pion1))
            print(W,"Le pion de",R,(nom2),W,"est",R,(pion2))
        print(W,'')


    
        #Saisie taille tableau
        taille_valide=['6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26'] #Liste taille valide sous forme de chaine de caractere
        taille = input("Saisir la taille du plateau : ")

        while (taille not in taille_valide): #Saisie sécurisée
            taille = input("Saisir la taille du plateau (min : 6 et max : 26) : ") 
        taille=int(taille) #Conversion chaine de caractere en entier si la taille saisie est valide
        print()
    
    
    
        #PROGRAMME
        
        #Initialisation  plateau, numero de tour et action
        plateau = []
        avancement_jeu={}
        plateau=creation_plateau(taille)
        initialisation_pions(plateau,taille)
        tour=0
        action=0
        
        
    
    
        while (action !='Q') and (condition_arret(plateau,taille)==0): #On continue tant que ...
            suppr_console() #supprimer la console
            tour = tour + 1 #Compteur de tour
            avancement_jeu[tour]=plateau
            
            
            #Attribution du joueur qui doit jouer en fonction du tour (1 tour sur 2 en alternance)
            if(tour%2==0): 
                pion='O'
            else:
                pion='X'
            
            
            #Affichage plateau + menu
            menu=creation_menu(pion,tour,plateau) #Création d'un nouveau menu personnalisé à chaque tour
            affichage(pion,plateau,taille,action,menu) #Affichage du plateau à chaque tour
            print()
    
            #Si le joueur doit passer son tour
            if (len(cases_valides(pion,plateau,taille)) ==0):
                print ("Vous ne pouvez pas jouer !")
                print("Vous passez votre tour")
                timer_4s()
        
            #Si le joueur ne passe pas son tour alors il joue
            else:
                
                #Saisie de la commande
                action=input("Saisir une commande : ") #P : Placer un pion, A : Afficher aide, Q : Quitter
                action=action.upper() #Convertion en majuscule
                while (action !='P') and (action !='A') and (action !='Q') : #Saisie sécurisé
                    action=input("Saisir une commande : ")
                    action=action.upper() #Conversion en majuscule
    
                #Placer un pion
                if (action=='P'): 
                    coordonnees = saisie_coordonnees_pions(pion,plateau,taille)
                    placement_pion(pion,coordonnees,plateau)
                    reverse_pion(plateau,coordonnees,pion,taille)
                    print()
                    
                #Affichage case valide + placer un pion ou quitter
                elif(action=='A'): 
                    print()
                    menu=creation_menu(pion,tour,plateau)
                    affichage(pion,plateau,taille,action,menu)
                    action=input("Saisir une commande : ")
                    action=action.upper() #Convertion en majuscule
                    
                    while (action !='P') and (action !='Q'): #Saisie sécurisée
                        action=input("Saisir une commande (P ou Q) : ")
                        action=action.upper() #Conversion en majuscule
                        
                    if (action=='P'): #placer un pion
                        coordonnees = saisie_coordonnees_pions(pion,plateau,taille)
                        placement_pion(pion,coordonnees,plateau)
                        reverse_pion(plateau,coordonnees,pion,taille)
                        print()
  
                
        
        #determination gagnant
        suppr_console()
        menu=creation_menu(pion,tour,plateau)
        affichage(pion,plateau,taille,action,menu)
        affichage_résultat_multi (nom1,nom2,changer,plateau,taille)
        print()
        
        
        
        
#............................................................................PROGRAMME EN MODE SOLO............................................................................
    else:
        
        #Saisie nom du joueur
        nom=input("Entrez votre nom : ")
        nom=nom.capitalize()#Conversion de type Prénom
        print()
      
        print("Bonjour",R,(nom))
        print()
        
        #Attribution des pions
        pion1='X'
        pion2='O'

        print(W,"Votre pion est",R,(pion1))
        print(W," ")
    
        #Changement de pion
        changer=input("Saississez 'change' pour changer de pion, sinon appuyez sur entrer ")
        changer=changer.lower()#conversion en minuscule

        while (changer != 'change') and (changer): #saisie sécurisée
            changer=input("Saississez 'change' pour changer de pion, sinon appuyez sur entrer ")
            changer=changer.lower() #conversion en minuscule

        if (changer=='change') :
            pion1='O'
            print(W,"Votre pion est",B,(pion1))
            pion2='X'
        print(W,'')
        
        #Saisie de la taille du plateau
        taille_valide=['6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26'] #Liste taille valide sous forme de chaine de caractere
        taille = input("Saisir la taille du plateau : ")

        while (taille not in taille_valide): #saisie sécurisé
            taille = input("Saisir la taille du plateau (min : 6 et max : 26) : ")
        taille=int(taille) #Conversion chaine de caractere en entier si la taille saisie est valide
        print()
    
    
    
        #Initialisation 
        plateau = []
        plateau=creation_plateau(taille)
        initialisation_pions(plateau,taille)
        tour=0
        action=0
        
        
    
    
        while (action !='Q') and (condition_arret(plateau,taille)==0):
            tour = tour + 1 #Compteur de tour
            
            #Attribution du joueur qui doit jouer en fonction du tour (1 tour sur 2 en alternance)
            if(tour%2==0):
                pion='O'
            else:
                pion='X'
            
            menu=creation_menu(pion,tour,plateau)
            affichage(pion,plateau,taille,action,menu)
            print()
            
            #Si le joueur est l'ordinateur
            if (pion==pion2):
                print("Au tour de l'ordinateur")
                
                #Si l'ordinateur doit passer son tour
                if (len(cases_valides(pion,plateau,taille)) ==0):
                    timer_4s()
                    suppr_console()
                    print ("L'ordinateur ne peut pas jouer !")
                    print("L'ordinateur passe son tour")
                    timer_4s()
                    
                #Sinon l'ordinateur choisi de maniere aléatoire une coordonnée parmi celles valides
                else:
                    coordonnees = random.choice(cases_valides(pion,plateau,taille)) #choix de coordonnées valides sous forme de chaine de caractere ('A1')
                    placement_pion(pion,coordonnees,plateau)
                    reverse_pion(plateau,coordonnees,pion,taille)
                    print()
                    timer_4s() 
                    suppr_console() #supprimer la console
                    print("L'ordinateur a joué en",coordonnees)
                    print()
                    
            #Si le joueur et l'utilisateur
            else:
                
                #Si le joueur doit passer son tour
                if (len(cases_valides(pion,plateau,taille)) ==0):
                    print ("Vous ne pouvez pas jouer !")
                    print("Vous passez votre tour")
                    timer_4s()
        
                #sinon le joueur joue
                else:
                    
                    #Saisie de la commande
                    action=input("Saisir une commande : ")
                    action=action.upper() #conversion en majuscule
                    
                    while (action !='P') and (action !='A') and (action !='Q'): #Saisie sécurisé
                        action=input("Saisir une commande : ")
                        action=action.upper() #conversion en majuscule
    
                    #realisation de l'action en fonction de la commande saisie
                    #Placement d'un pion
                    if (action=='P'):
                        coordonnees = saisie_coordonnees_pions(pion,plateau,taille)
                        placement_pion(pion,coordonnees,plateau)
                        reverse_pion(plateau,coordonnees,pion,taille)
                        print()
                    
                    #Affichage de l'aide + placement pion
                    elif(action=='A'):
                        print()
                        menu=creation_menu(pion,tour,plateau)
                        affichage(pion,plateau,taille,action,menu)
                        action=input("Saisir une commande : ")
                        action=action.upper() #conversion en majuscule
                        
                        while (action !='P') and (action !='Q'): #saisie sécurisé
                            action=input("Saisir une commande (P ou Q) : ")
                            action=action.upper() #conversion en majuscule
                        
                        #Placemetn pion
                        if (action=='P'):
                            coordonnees = saisie_coordonnees_pions(pion,plateau,taille)
                            placement_pion(pion,coordonnees,plateau)
                            reverse_pion(plateau,coordonnees,pion,taille)
                            print()

                    suppr_console() #supprimer la console
                
                
        
        #determination gagnant
        suppr_console()
        menu=creation_menu(pion,tour,plateau)
        affichage(pion,plateau,taille,action,menu)
        print()
        affichage_résultat_solo (nom,changer,plateau,taille)
        print()
        
        
        
        
        
    
    recommencer=input("Pour recommencer, appuyer sur R ! Pour quitter, appuyer sur Q : ")
    recommencer=recommencer.upper() #conversion en majuscule
    while (recommencer != 'R') and (recommencer != 'Q'): #Saisie sécurisée
        recommencer=input("Pour recommencer, appuyer sur R ! Pour quitter, appuyer sur Q : ")
        recommencer=recommencer.upper() #conversion en majuscule
        
        
print()       
print("Merci d'avoir joué")

    



