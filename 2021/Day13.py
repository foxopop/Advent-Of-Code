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

nomFichier = "test13.txt" 

nomFichier = "input13.txt" 



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

  #if all( cases[l][c] == 0 for l,c in zip(range(1,nbL+1), range(1,nbC+1))  ):
  #  print( "step NUL = ", step)     
  #  break


def plierMatrice( m, pSens, pNiv ):
  print ("Je plie en ",pSens, " au niveau ", pNiv)

  maxCount = pNiv-1

  nbCC = len(m[0])
  nbLL = len(m)

  m2=[]  

  nb = 0
  if sens == "y":
    for l in range(0, maxCount+1):
      ligne =[]
      for c in range( 0, nbCC):
        case = cases[l][c] | cases[nbLL-1-l][c]
        ligne.append( case )
        if case == 1:
          nb += 1
      m2.append(ligne.copy())   

    
  
  elif sens == "x":
    for l in range( 0, nbLL):
      ligne = []
      for c in range(0, maxCount+1):
        case = cases[l][c] | cases[l][nbCC-1-c]
        ligne.append (case)
        if case == 1:
          nb += 1
      m2.append(ligne.copy())       

  
  return(m2, nb)
  
  


#####################################################    LECTURE LIGNES
debug ("================= DEBUT ================")



maxX = 0
maxY = 0

for l in lines:
  if l[:4] == "":
    break

    
  elif l != "":  
    (x,y) = l.split(',')
    maxX = max( int(x) , maxX)
    maxY = max( int(y) , maxY)

nbL = maxY+1
nbC = maxX+1

cases = [ [0 for c in range(maxX+1)] for l in range(maxY+1) ]

for l in lines :
  if l == "":
    break
  (x,y) = map( int, l.split(','))
  cases[y][x] = 1

afficherMatrice( cases, 2) 



for l in lines:
  if l[:4] == "fold":
    # plis
    (sens, nivCH) = l[11:].split("=")
    niv = int(nivCH)
    print ("Je plie en ",sens, " au niveau ", niv)

    (mPliee, nb) = plierMatrice( cases, sens, niv )
    cases = mPliee.copy()
      
    afficherMatrice( cases, 2) 
  
print(nb)







 






   
   
   
   
  
    



