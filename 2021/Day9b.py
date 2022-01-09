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
#nomFichier = "test9a.txt" 
nomFichier = "input9a.txt" 



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

def afficherMatrice( m, long=int(2)):
  #print(" ")
  for y in range(len(m)):
    ligne = ""
    for x in range(len (m[y]) ):
      #contenu = str(m[y][x])
      contenu = m[y][x]
      #ligne += str(contenu)
      ligne += '{0:{width}}'.format( contenu, width=long)
      
    #print('{0:{width}}'.format( ligne, width=long) )
    print(ligne)

#####################################################    LECTURE LIGNES


  

debug ("================= DEBUT ================")


def tailleBassin(l, c):
  #print ( "calcul taille bassin ",l, ", ",c)
  if cases[l][c] >= 9:
    return 0
  else:
    cases[l][c] = 11 # marque pour ne plus le compter
    return 1 + tailleBassin(l-1, c) + tailleBassin(l, c-1) + tailleBassin(l+1, c) + tailleBassin(l, c+1) 
  

nbL = len(lines)
nbC = len(lines[0])

#☻print( nbL,nbC)

cases = [ [10 for c in range(nbC+2)] for l in range(nbL+2) ]

for l in range( 0, nbL) :
  for c in range( 0, nbC) :
    #print ( l, " ", c, " ", lines[l-1][c-1] )
    cases[l+1][c+1] = int(lines[l][c])
    #print (cases[l][c])
    
afficherMatrice( cases, 3)    
    

risk  = 0
total = 0

lps = []

for l in range( 1, nbL+1) :
  for c in range( 1, nbC+1) :
    case = cases[l][c]
    if (     case < cases[l-1][c] 
         and case < cases[l][c-1] 
         and case < cases[l+1][c] 
         and case < cases[l][c+1] 
         ) :
      #print ("low=",case)
      lps.append( (l,c) )
      risk = case + 1
      total += risk
  
print(" ")

bassins = []

for lp in lps:
  #print(lp[0], lp[1])
  # calcul taille bassin 
  tb = tailleBassin(lp[0], lp[1])
  
  #print ("taille bassin ", lp[0], lp[1], " = ",tb)
  
  # on ajoute aux bassins
  bassins.append(tb)
  
bassins.sort(reverse=True) 

print( bassins[0] * bassins[1] * bassins[2] )
  
  
  
























