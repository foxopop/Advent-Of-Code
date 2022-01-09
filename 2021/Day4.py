#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import os
#import re     # expressions regulières
import collections
import string

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""   Initialisation en dur des entrées : ne pas copier  """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lines = []







# Attention : volontairement écrasé par ci-dessous :

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""   Initialisation des entrées à partir de input1.txt : ne pas copier    """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nomFichier = ""
nomFichier = "input4.txt" 
#nomFichier = "test4.txt" 



if nomFichier != "":
    sys.stderr.write("\n"+"ATTENTION : LECTURE FICHIER "+nomFichier+"\n\n")
    fichier = open(nomFichier, "r")
    lines = fichier.readlines()
    fichier.close()
    # on enleve les EOF
    for i in range(0, len(lines)):
         lines[i] = lines[i].rstrip('\n')


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""   Fin init entrées                                   """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



############################################################
############      REPRENDRE A PARTIR D'ICI     #############      <=   COPIE
############################################################
    
test_debug = True

def debug(s) :
    if test_debug:
        sys.stderr.write(str(s) + '\n')   
  
def debugL(s) :
    if test_debug:
        sys.stderr.write(str(s) )   
  

def printL(s) :
  sys.stdout.write(str(s) )
  
def deb(*args, **kwargs):
  if test_debug:
    print(*args, file=sys.stderr, **kwargs)

  

#####################################################    LECTURE LIGNES


def afficherGrille(g):
  for l in range(5):
      print( g[l] )
    


debug ("================= DEBUT ================")


grilles = []

grille = [" "] * 5 * 5




nbTirages = len(lines[0]) 
tirages = lines[0].split(",")

i=2

###############################################################


def coord(gr, tir):
  x =0
  
  Trouve = False
  
  while not Trouve and x<5:
    y=0
    while not Trouve and y<5:
      if gr[y][x] == tir:
        Trouve = True
        return x,y
      y += 1
    x+=1  
  
  return -1, -1  


def gain( gr, tir ):
  score = 0
  
  afficherGrille(grillesCochees[gr])
  
  for y in range(5):
    for x in range(5):
      if grillesCochees[gr][y][x] != "T" :
        case = grillesCochees[gr][y][x]
        score += int( case )
  score = score * int(tir )    
  return score


##################################### remplissage des grilles

nbGrilles = 0

while i<len(lines)-1:
  
  # lecture une grille
  
  for l in range(0,5):
    grille[l] = lines[i+l].split()
    #print( grille[l])
    
  # ajout de la grille
  grilles.append( grille.copy() )  
  i+=6
  nbGrilles +=1
    
for g in grilles:
  afficherGrille(g)
  print(" ")
  
grillesCochees = grilles.copy()  
  
######################################  tirages


print ( any ("58" in sslist for sslist in grilles))

score = 0

grillesGagnantes = ["P"] * nbGrilles

print( grillesGagnantes)

for t in tirages :
  
  #if score != 0 :
  #  break

  if grillesGagnantes.count("P") == 0:
    break
  
  for g in range( len(grilles)) :
    
    #print ("Recherche ", t, " dans la grille ", g)
    
    # si present ds la grille
    xT,yT = coord( grilles[g], t)
    if (xT, yT) != (-1,-1) :
     
      grillesCochees[g][yT][xT] = "T"
      
      # on regarde si on vient de completer une ligne
      if grillesCochees[g][yT].count("T") == 5:
          score = gain (g, t)
          print ("grille ",g ," gagnante en ligne ",yT, " : ", score )
          grillesGagnantes[g] = "G"
          if grillesGagnantes.count("P") == 0:
            break
          
      
      # on regarde si on vient de completer une colonne
      gagne = True # par defaut
      for y in range(5):
        if grillesCochees[g][y][xT] != "T":
          gagne = False
      if gagne:    
        score = gain (g, t)
        print ("grille ",g ," gagnante en colonne ",xT, " : ", score )
        grillesGagnantes[g] = "G"
        if grillesGagnantes.count("P") == 0:
          break
      
      
#grillePerdante = grillesGagnantes.index("P")

print (score)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
