import numpy as np
import scipy.io
import matplotlib.pyplot as plt
#Pour la fonction kppv :
#cette fonction retourne la classe obtenu pour un nouveau individu
#Le parametre apprent : il s'agit de tout les individus de l'apprentisage
#Le parametre k : le nombre de voisins utilises dans l'algorithme.
#Le parametre individu : c'est l'individu a classer
#Le parametre classe_origin : classe origine est un vecteur qui indique la classification de l'ensemble d'apprentissage.
def kppv (apprent,k,individu,classe_origin):

    nbr_colonnes_apprent=len(apprent[1,:])
    #dist : la liste des distances entre le nouveau individu avec l'ensemble de l'apprentissage
    dist=[]
    #Pour chaque individu de l'ensemble d'apprentissage on calcule sa distance avec le nouveau individu
    #Ici on utilise une distance Euclidienne pour notre calcul
    for iteration_colonne_apprent in range(0,nbr_colonnes_apprent):
         dist.append(np.sqrt(((individu[0]-apprent[0,iteration_colonne_apprent])**2)+
                             ((individu[1]-apprent[1,iteration_colonne_apprent])**2)))
    # on ordonne notre tableau de distance sachant que ce tableau stocke les indices par ordre croissant
    dist_ordonne=np.argsort(dist)

    nbr_classe_1 = 0
    nbr_classe_2 = 0
    nbr_classe_3 = 0
    #On initialise le nombre de classe 1 ,classe 2 , classe3
    #Pour un k donne , on parcour la liste qui contient les indices des individus qui sont les plus proches du nouveau individu
    # et apres on cherche sa classe et on incremente de 1 la classe correspondante pour chaque iteration
    # la variable nbr_claase va nous aider a savoir dans quel classe on doit classer notre nouveau individu
    for ind in range(0,k):
        if(classe_origin[dist_ordonne[ind]]==1):
              nbr_classe_1=nbr_classe_1+1
        elif(classe_origin[dist_ordonne[ind]]==2):
             nbr_classe_2=nbr_classe_2+1
        else:
             nbr_classe_3=nbr_classe_3+1
# Ici on cherche le max pour les trois classes pour pouvoir choisir la classe qui doit etre affecte notre nouveau individu
    if(nbr_classe_1<nbr_classe_2):
        if(nbr_classe_2<nbr_classe_3):
            return 3
        else:
            return 2
    else:
        if(nbr_classe_1<nbr_classe_3):
            return 3
        else:
            return 1
#Pour la fonction affichageKNN :
#Cette fonction permet d'afficher les individus qu'on a classes ( chaque classe a sa propre couleur)
#Le parametre titre : correspond au titre de l'exercice
#Le parametre nbr_colonnes_individus : il s'agit du nombre des individus qu'on va les classes
#Le parametre individus : il s'agit des individus qu'on va classes
#Le parametre classes : il s'agit des clsses obtenus apres l'execution de l'algorithme du  KPPV
def affichageKNN(titre,nbr_colonnes_individus,individus,classes):
 plt.title(titre)
 plt.xlabel("Abscisse x")
 plt.ylabel("Ordonne y")
 for j in range(0, nbr_colonnes_individus):# X 300 individus
    if (classes[j] == 1):
        plt.plot(individus[0, j], individus[1, j], 'o', color="red")
    elif (classes[j] == 2):
        plt.plot(individus[0, j], individus[1, j], 'o', color="blue")
    else:
        plt.plot(individus[0, j], individus[1, j], 'o', color="yellow")
 plt.show()

#Pour la fonction affichageTauxErreur :
#Cette fonction retourne une courbe des erreurs pour chaque k = 1,3,5,7,13,15 on aura une errur affiche
#Le parametre titre : le titre de l'exercice
#Le parametre erreur : est une liste des k-erreurs
def affichageTauxErreur(titre,erreurs):
     plt.title(titre)
     plt.xlabel(" k")
     plt.ylabel("erreur(en %)")
     vecteur_x=[1,3,5,7,13,15]
     vecteaur_y=[erreurs[0],erreurs[1],erreurs[2],erreurs[3],erreurs[4],erreurs[5]]
     plt.plot(vecteur_x,vecteaur_y, color="red")
     plt.show()
     return plt



#Pour la fonction tauxErreur :
#Cette fonction retourne l'erreur on comparant le resultat obtenu et le resultat souhaite
#Le parametre nbr_colonnes_individus : il s'agit du nombre des individus qu'on va les classes
#le parametre class_apprent : il s'agit les classes souhaites
#Le parametre classes : il s'agit des classes obtenus

def tauxErreur (nbr_colonnes_individus,class_apprent,classes):
    echec = 0
    for p in range(0, nbr_colonnes_individus):
        if (class_apprent[0, p] != classes[p]):
            echec = echec + 1
    return (float(echec)/(nbr_colonnes_individus))*100
#Pour la fonction classeOrigin_exemple1 :
#Cette fonction permet de retourner la classe pour chaque individu de l'apprentissage
def classeOrigin_exemple1():
    classe_origin=[]
    for count in range(0, 150):
        if (count in range(0, 50)):
            classe_origin.append(1)
        elif (count in range(50, 100)):
            classe_origin.append(2)
        else:
            classe_origin.append(3)
    return classe_origin
#Pour la fonction classeOrigin_exemple3 :
#Cette fonction permet de retourner la classe pour chaque individu de l'apprentissage
def classeOrigin_exemple3():
    classe_origin=[]
    for count in range(0, 60):
        if (count in range(0, 20)):
            classe_origin.append(1)
        elif (count in range(20, 40)):
            classe_origin.append(2)
        else:
            classe_origin.append(3)
    return classe_origin

#Pour la fonction classeOrigin_exemple4 :
#Cette fonction permet de retourner la classe pour chaque individu de l'apprentissage
def classeOrigin_exemple4():
    classe_origin=[]
    for count in range(0, 450):
        if (count in range(0, 150)):
            classe_origin.append(1)
        elif (count in range(150, 300)):
            classe_origin.append(2)
        else:
            classe_origin.append(3)
    return classe_origin
#Pour la fonction classeOrigin_exemple5:
#Cette fonction permet de retourner la classe pour chaque individu de l'apprentissage
def classeOrigin_exemple5():
    classe_origin=[]
    for count in range(0, 210):
        if (count in range(0, 70)):
            classe_origin.append(1)
        elif (count in range(70, 140)):
            classe_origin.append(2)
        else:
            classe_origin.append(3)
    return classe_origin
#Pour la fonction vecteurToList:
#Cette fonction permet de prendre en parametre un vecteur et de retourner a la fin une liste
def vecteurToList(vecteur_origine):
    list_final=[]
    for indice_v in vecteur_origine[0,:]:
        list_final.append(indice_v)
    return list_final




if __name__ == "__main__":

#------------ Comparaison standard-------------KPPV-----------
  data1 = scipy.io.loadmat('.\Data\p1_data1')
  individus1=data1['x']
  apprent1=data1['test']
  class_apprent1=data1['clasapp']
  # Pour chaque k ={1,3,5,7,13,15} on une classe qui est une liste qui va stocker les classes de nos nouveaux individus
  classes1k1=[]
  classes1k3=[]
  classes1k5=[]
  classes1k7=[]
  classes1k13=[]
  classes1k15=[]
  #Cette liste stocke toutes les erreurs pour tout les k k ={1,3,5,7,13,15}
  erreurs=[]
  #nbr_colonnes_individus1 : la taille des nouveaux individus
  nbr_colonnes_individus1 = len(individus1[1, :]) #300
  #nbr_colonnes_apprent1 : la taille des individus notre ensemble d'apprentissage
  nbr_colonnes_apprent1=len(apprent1[1,:]) #150
     #----K=1-----
  for iteration_colonne_individu1 in range(0, nbr_colonnes_individus1):
    classes1k1.append(kppv(apprent1,1,individus1[:,iteration_colonne_individu1],classeOrigin_exemple1()))

  affichageKNN("Comparaison standard avec l'agorithme KNN",nbr_colonnes_individus1,individus1,classes1k1)
  print("taux erreur comparaison standard pour k=1   = " + str(tauxErreur(nbr_colonnes_individus1,class_apprent1,classes1k1)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus1,class_apprent1,classes1k1))
#----K=3-----
  for iteration_colonne_individu1 in range(0, nbr_colonnes_individus1):
    classes1k3.append(kppv(apprent1, 3, individus1[:, iteration_colonne_individu1], classeOrigin_exemple1()))
  print("taux erreur comparaison standard pour k=3  = " + str(tauxErreur(nbr_colonnes_individus1, class_apprent1, classes1k3)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus1, class_apprent1, classes1k3))
#----K=5-----
  for iteration_colonne_individu1 in range(0, nbr_colonnes_individus1):
    classes1k5.append(kppv(apprent1, 5, individus1[:, iteration_colonne_individu1], classeOrigin_exemple1()))
  print("taux erreur comparaison standard pour k=5   = " + str(tauxErreur(nbr_colonnes_individus1, class_apprent1, classes1k5)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus1, class_apprent1, classes1k5))
#----K=7-----
  for iteration_colonne_individu1 in range(0, nbr_colonnes_individus1):
    classes1k7.append(kppv(apprent1, 7, individus1[:, iteration_colonne_individu1], classeOrigin_exemple1()))
  print("taux erreur comparaison standard pour k=7   = " + str(tauxErreur(nbr_colonnes_individus1, class_apprent1, classes1k7)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus1, class_apprent1, classes1k7))
#----K=13-----
  for iteration_colonne_individu1 in range(0, nbr_colonnes_individus1):
    classes1k13.append(kppv(apprent1, 13, individus1[:, iteration_colonne_individu1], classeOrigin_exemple1()))
  print("taux erreur comparaison standard pour k=13   = " + str(tauxErreur(nbr_colonnes_individus1, class_apprent1,classes1k13)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus1, class_apprent1,classes1k13))
  pl1=affichageKNN("Algorithme KNN pour la comparaison standard avec K=13", nbr_colonnes_individus1, individus1, classes1k13)
  #pl1.figure()
#----K=15-----
  for iteration_colonne_individu1 in range(0, nbr_colonnes_individus1):
    classes1k15.append(kppv(apprent1, 15, individus1[:, iteration_colonne_individu1], classeOrigin_exemple1()))
  print("taux erreur comparaison standard pour k=15   = " + str(tauxErreur(nbr_colonnes_individus1, class_apprent1, classes1k15)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus1, class_apprent1, classes1k15))

# ------------ Absence de professeur-------------KPPV-----------
  data2 = scipy.io.loadmat('.\Data\p1_data2')
  individus2=data2['x']
  apprent2=data2['test']
  class_apprent2=data2['clasapp']
  classes2k1=[]
  classes2k3=[]
  classes2k5=[]
  classes2k7=[]
  classes2k13=[]
  classes2k15=[]

  erreurs=[]
  classe_origine=data2['orig']
  nbr_colonnes_individus2 = len(individus2[1, :]) #300
  nbr_colonnes_apprent2=len(apprent2[1,:]) #150
#----K=1----
  for iteration_colonne_individu2 in range(0, nbr_colonnes_individus2):
    classes2k1.append(kppv(apprent2,1,individus2[:,iteration_colonne_individu2],vecteurToList(classe_origine)))
  print("taux erreur Absence de professeur pour k=1  = " + str(tauxErreur(nbr_colonnes_individus2,class_apprent2,classes2k1)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus2,class_apprent2,classes2k1))
#----K=3-----
  for iteration_colonne_individu2 in range(0, nbr_colonnes_individus2):
    classes2k3.append(kppv(apprent2, 3, individus2[:, iteration_colonne_individu2], vecteurToList(classe_origine)))
  print("taux erreur Absence de professeur pour k=3  = " + str(tauxErreur(nbr_colonnes_individus2, class_apprent2, classes2k3)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus2, class_apprent2, classes2k3))
#----K=5-----
  for iteration_colonne_individu2 in range(0, nbr_colonnes_individus2):
    classes2k5.append(kppv(apprent2, 5, individus2[:, iteration_colonne_individu2], vecteurToList(classe_origine)))
  print("taux erreur Absence de professeur pour k=5   = " + str(tauxErreur(nbr_colonnes_individus2, class_apprent2, classes2k5)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus2, class_apprent2, classes2k5))
  pl2 = affichageKNN("Algorithme KNN pour l'absence de professeur avec K=5", nbr_colonnes_individus2, individus2,classes2k5)
  #pl2.figure()


#----K=7-----
  for iteration_colonne_individu2 in range(0, nbr_colonnes_individus2):
    classes2k7.append(kppv(apprent2, 7, individus2[:, iteration_colonne_individu2], vecteurToList(classe_origine)))
  print("taux erreur Absence de professeur pour k=7   = " + str(tauxErreur(nbr_colonnes_individus2, class_apprent2, classes2k7)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus2, class_apprent2, classes2k7))
#----K=13-----
  for iteration_colonne_individu2 in range(0, nbr_colonnes_individus2):
    classes2k13.append(kppv(apprent2, 13, individus2[:, iteration_colonne_individu2], vecteurToList(classe_origine)))
  print("taux erreur Absence de professeur pour k=13   = " + str(tauxErreur(nbr_colonnes_individus2, class_apprent2,classes2k13)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus2, class_apprent2,classes2k13))
#----K=15-----
  for iteration_colonne_individu2 in range(0, nbr_colonnes_individus2):
    classes2k15.append(kppv(apprent2, 15, individus2[:, iteration_colonne_individu2], vecteurToList(classe_origine)))
  print("taux erreur Absence de professeur pour k=15   = " + str(tauxErreur(nbr_colonnes_individus2, class_apprent2, classes2k15)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus2, class_apprent2, classes2k15))

# ------------ Influence de la taille de l'ensemble d'apprentissage : taille reduite-------------KPPV-----------
  data3 = scipy.io.loadmat('.\Data\p1_data3a')
  individus3=data3['x']
  apprent3=data3['test']
  class_apprent3=data3['clasapp']
  classes3k1=[]
  classes3k3=[]
  classes3k5=[]
  classes3k7=[]
  classes3k13=[]
  classes3k15=[]

  erreurs=[]
  nbr_colonnes_individus3 = len(individus3[1, :]) #300
  nbr_colonnes_apprent3=len(apprent3[1,:]) #60
#----K=1----
  for iteration_colonne_individu3 in range(0, nbr_colonnes_individus3):
    classes3k1.append(kppv(apprent3,1,individus3[:,iteration_colonne_individu3],classeOrigin_exemple3()))
  print("taux erreur Influence de la taille de l'ensemble d'apprentissage : taille reduite pour k=1  = " + str(tauxErreur(nbr_colonnes_individus3,class_apprent3,classes3k1)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus3,class_apprent3,classes3k1))
#----K=3-----
  for iteration_colonne_individu3 in range(0, nbr_colonnes_individus3):
    classes3k3.append(kppv(apprent3, 3, individus3[:, iteration_colonne_individu3], classeOrigin_exemple3()))
  print("taux erreur Influence de la taille de l'ensemble d'apprentissage : taille reduite  pour k=3  = " + str(tauxErreur(nbr_colonnes_individus3, class_apprent3, classes3k3)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus3, class_apprent3, classes3k3))
#----K=5-----
  for iteration_colonne_individu3 in range(0, nbr_colonnes_individus3):
    classes3k5.append(kppv(apprent3, 5, individus3[:, iteration_colonne_individu3], classeOrigin_exemple3()))
  print("taux erreur Influence de la taille de l'ensemble d'apprentissage : taille reduite  pour k=5   = " + str(tauxErreur(nbr_colonnes_individus3, class_apprent3, classes3k5)) + " %")
  erreurs.append( tauxErreur(nbr_colonnes_individus3, class_apprent3, classes3k5))
  pl3 = affichageKNN("Algorithme KNN pour l'influence de la taille de l'ensemble d'apprentissage : taille reduite avec K=5", nbr_colonnes_individus3, individus3,classes3k5)
  #pl3.figure()

#----K=7-----
  for iteration_colonne_individu3 in range(0, nbr_colonnes_individus3):
    classes3k7.append(kppv(apprent3, 7, individus3[:, iteration_colonne_individu3], classeOrigin_exemple3()))
  print("taux erreur Influence de la taille de l'ensemble d'apprentissage : taille reduite  pour k=7   = " + str(tauxErreur(nbr_colonnes_individus3, class_apprent3, classes3k7)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus3, class_apprent3, classes3k7))
#----K=13-----
  for iteration_colonne_individu3 in range(0, nbr_colonnes_individus3):
    classes3k13.append(kppv(apprent3, 13, individus3[:, iteration_colonne_individu3], classeOrigin_exemple3()))
  print("taux erreur Influence de la taille de l'ensemble d'apprentissage : taille reduite  pour k=13   = " + str(tauxErreur(nbr_colonnes_individus3, class_apprent3,classes3k13)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus3, class_apprent3,classes3k13))
#----K=15-----
  for iteration_colonne_individu3 in range(0, nbr_colonnes_individus3):
    classes3k15.append(kppv(apprent3, 15, individus3[:, iteration_colonne_individu3], classeOrigin_exemple3()))
  print("taux erreur Influence de la taille de l'ensemble d'apprentissage : taille reduite  pour k=15   = " + str(tauxErreur(nbr_colonnes_individus3, class_apprent3, classes3k15)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus3, class_apprent3, classes3k15))

#--------Influence de la taille de l'ensemble d'apprentissage : taille importante-----kppv---------
  data4 = scipy.io.loadmat('.\Data\p1_data3b')
  individus4=data4['x']
  apprent4=data4['test']
  class_apprent4=data4['clasapp']
  classes4k1=[]
  classes4k3=[]
  classes4k5=[]
  classes4k7=[]
  classes4k13=[]
  classes4k15=[]

  erreurs=[]

  nbr_colonnes_individus4 = len(individus4[1, :]) #300
  nbr_colonnes_apprent4=len(apprent4[1,:]) #450
#----K=1----
  for iteration_colonne_individu4 in range(0, nbr_colonnes_individus4):
    classes4k1.append(kppv(apprent4,1,individus4[:,iteration_colonne_individu4],classeOrigin_exemple4()))

  print("taux erreur Influence de la taille de l'ensemble d'apprentissage : taille importante pour k=1  = " + str(tauxErreur(nbr_colonnes_individus4,class_apprent4,classes4k1)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus4,class_apprent4,classes4k1))
#----K=3-----
  for iteration_colonne_individu4 in range(0, nbr_colonnes_individus4):
    classes4k3.append(kppv(apprent4, 3, individus4[:, iteration_colonne_individu4], classeOrigin_exemple4()))
  print("taux erreur Influence de la taille de l'ensemble d'apprentissage : taille importante  pour k=3  = " + str(tauxErreur(nbr_colonnes_individus4, class_apprent4, classes4k3)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus4, class_apprent4, classes4k3))
#----K=5-----
  for iteration_colonne_individu4 in range(0, nbr_colonnes_individus4):
    classes4k5.append(kppv(apprent4, 5, individus4[:, iteration_colonne_individu4], classeOrigin_exemple4()))
  print("taux erreur Influence de la taille de l'ensemble d'apprentissage : taille importante pour k=5   = " + str(tauxErreur(nbr_colonnes_individus4, class_apprent4, classes4k5)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus4, class_apprent4, classes4k5))
#----K=7-----
  for iteration_colonne_individu4 in range(0, nbr_colonnes_individus4):
    classes4k7.append(kppv(apprent4, 7, individus4[:, iteration_colonne_individu4], classeOrigin_exemple4()))
  print("taux erreur Influence de la taille de l'ensemble d'apprentissage : taille importante  pour k=7   = " + str(tauxErreur(nbr_colonnes_individus4, class_apprent4, classes4k7)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus4, class_apprent4, classes4k7))
  pl4 = affichageKNN("Algorithme KNN pour l'influence de la taille de l'ensemble d'apprentissage : taille importante avec K=7",nbr_colonnes_individus4, individus4, classes4k7)
  #pl4.figure()

#----K=13-----
  for iteration_colonne_individu4 in range(0, nbr_colonnes_individus4):
    classes4k13.append(kppv(apprent4, 13, individus4[:, iteration_colonne_individu4], classeOrigin_exemple4()))
  print("taux erreur Influence de la taille de l'ensemble d'apprentissage : taille importante pour k=13   = " + str(tauxErreur(nbr_colonnes_individus4, class_apprent4,classes4k13)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus4, class_apprent4,classes4k13))
#----K=15-----
  for iteration_colonne_individu4 in range(0, nbr_colonnes_individus4):
    classes4k15.append(kppv(apprent4, 15, individus4[:, iteration_colonne_individu4], classeOrigin_exemple4()))
  print("taux erreur Influence de la taille de l'ensemble d'apprentissage : taille importante  pour k=15   = " + str(tauxErreur(nbr_colonnes_individus4, class_apprent4, classes4k15)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus4, class_apprent4, classes4k15))


#--------Distribution inconnue-----kppv---------
  data5 = scipy.io.loadmat('.\Data\p1_data4')
  individus5=data5['x']
  apprent5=data5['test']
  class_apprent5=data5['clasapp']
  classes5k1=[]
  classes5k3=[]
  classes5k5=[]
  classes5k7=[]
  classes5k13=[]
  classes5k15=[]

  erreurs=[]

  nbr_colonnes_individus5 = len(individus5[1, :]) #300
  nbr_colonnes_apprent5=len(apprent5[1,:]) #210
#----K=1----
  for iteration_colonne_individu5 in range(0, nbr_colonnes_individus5):
    classes5k1.append(kppv(apprent5,1,individus5[:,iteration_colonne_individu5],classeOrigin_exemple5()))
  print("taux erreur de la Distribution inconnue pour k=1  = " + str(tauxErreur(nbr_colonnes_individus5,class_apprent5,classes5k1)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus5,class_apprent5,classes5k1))
#----K=3-----
  for iteration_colonne_individu5 in range(0, nbr_colonnes_individus5):
    classes5k3.append(kppv(apprent5, 3, individus5[:, iteration_colonne_individu5], classeOrigin_exemple5()))
  print("taux erreur de la Distribution inconnue pour k=3  = " + str(tauxErreur(nbr_colonnes_individus5, class_apprent5, classes5k3)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus5,class_apprent5,classes5k3))
#----K=5-----
  for iteration_colonne_individu5 in range(0, nbr_colonnes_individus5):
    classes5k5.append(kppv(apprent5, 5, individus5[:, iteration_colonne_individu5], classeOrigin_exemple5()))
  print("taux erreur de la Distribution inconnue pour k=5   = " + str(tauxErreur(nbr_colonnes_individus5, class_apprent5, classes5k5)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus5,class_apprent5,classes5k5))
#----K=7-----
  for iteration_colonne_individu5 in range(0, nbr_colonnes_individus5):
    classes5k7.append(kppv(apprent5, 7, individus5[:, iteration_colonne_individu5], classeOrigin_exemple5()))
  print("taux erreur de la Distribution inconnue  pour k=7   = " + str(tauxErreur(nbr_colonnes_individus5, class_apprent5, classes5k7)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus5,class_apprent5,classes5k7))
  pl5 = affichageKNN("Algorithme KNN pour la Distribution inconnue avec K=7",nbr_colonnes_individus5, individus5, classes5k7)
  #pl5.figure()
  plt.close()

#----K=13-----
  for iteration_colonne_individu5 in range(0, nbr_colonnes_individus5):
    classes5k13.append(kppv(apprent5, 13, individus5[:, iteration_colonne_individu5], classeOrigin_exemple5()))
  print("taux erreur de la Distribution inconnue pour k=13   = " + str(tauxErreur(nbr_colonnes_individus5, class_apprent5,classes5k13)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus5,class_apprent5,classes5k13))
#----K=15-----
  for iteration_colonne_individu5 in range(0, nbr_colonnes_individus5):
    classes5k15.append(kppv(apprent5, 15, individus5[:, iteration_colonne_individu5], classeOrigin_exemple5()))
  print("taux erreur de la Distribution inconnue  pour k=15   = " + str(tauxErreur(nbr_colonnes_individus5, class_apprent5, classes5k15)) + " %")
  erreurs.append(tauxErreur(nbr_colonnes_individus5,class_apprent5,classes5k3))
