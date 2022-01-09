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
from collections import defaultdict

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""   Initialisation en dur des entrées : ne pas copier  """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lines = "3"



# Attention : volontairement écrasé par ci-dessous :

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""   Initialisation des entrées à partir de input1.txt : ne pas copier    """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nomFichier = ""

nomFichier = "test15.txt" 

#nomFichier = "input15.txt" 



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

def afficherMatrice( m, long=int(2), avecBords=True) :
  
  if avecBords == False:
    delta=1
  else:
    delta=0
  
  for y in range(delta, len(m) - delta):
    ligne = ""
    for x in range(delta, len (m[y]) - delta):
      #contenu = str(m[y][x])
      contenu = m[y][x]
      #ligne += str(contenu)
      ligne += '{0:{width}}'.format( contenu, width=long)
      
    #print('{0:{width}}'.format( ligne, width=long) )
    print(ligne)
  print(" ")




#####################################################    LECTURE LIGNES
debug ("================= DEBUT ================")

nbL = len(lines)
nbC = len(lines[0])
maxC = nbC-1
maxL = nbL-1


cases = [ [0 for c in range(nbC)] for l in range(nbL) ]


RP = [ [0 for c in range(nbC)] for l in range(nbL) ]

for l in range( 0, nbL) :
  for c in range( 0, nbC) :
    cases[l][c] = int(lines[l][c])

afficherMatrice( cases, 2 , True)


cCour = maxC-1
lCour = maxL-1

RP[maxL][maxC] = cases[maxL][maxC]



while cCour >=0 and lCour >=0:
  


  dxB=0
  dyB=-1
  dxD=-1
  dyD=0

  xB,yB = cCour,maxL  # 1
  xD,yD = maxC,lCour  # 2

  # case à gauche
  RP[yB][xB] = RP[yB][xB+1] + cases[yB][xB]  

  #case au dessus  
  RP[yD][xD] = RP[yD+1][xD] + cases[yD][xD]

  while abs(xB-xD) + abs(yB-yD) > 1:
  
 
    afficherMatrice( RP, 3, True)



    if RP[yB][xB] <= RP[yD][xD]:

      old = RP[yB][xB]      

      # Bas < Droite
      if yB>yD:
        dyB = -1
      else:
        dxB = +1
        dyB = 0
      xB += dxB
      yB += dyB
        
      RP[yB][xB] = old + cases[yB][xB]
      afficherMatrice( RP, 3, True)  

    else:
      
      # Droite < Bas
      if xD>xB:
        dxD = -1
        if xD+dxD != xB:
          old = min( RP[yD][xD], RP[yD+1][xD-1])
        else:
          old = RP[yD][xD]

      else:
        dyD = +1 # on descend
        dxD = 0  # on arrete le deplacement  a gauche
        if yD+dyD != yB:
          old = min( RP[yD][xD], RP[yD+1][xD+1])
        else:
          old = RP[yD][xD]
          
      
      yD += dyD
      xD += dxD
        
      RP[yD][xD] = old + cases[yD][xD]
      afficherMatrice( RP, 3, True) 

  if cCour >= 0:
    cCour -= 1
  if lCour >= 0:
    lCour -= 1
    
RP[0][0] = min(RP[1][0],RP[0][1] )   

print (RP[0][0]) 
    

 






   
   
   
   
  
    



