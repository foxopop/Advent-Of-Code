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

cases = [ [0 for c in range(nbC)] for l in range(nbL) ]

memoRisk = [ [0 for c in range(nbC)] for l in range(nbL) ]




interdit = 10 * nbL * nbC

for l in range( 0, nbL) :
  for c in range( 0, nbC) :
    cases[l][c] = int(lines[l][c])

#afficherMatrice( cases, 2, True)


def risk( c,l) :
  
  print ("calcul risk ",c, ",",l)
  
  dejaPasse = [ [False for c in range(nbC)] for l in range(nbL) ]
  
  dejaPasse[c][l] = True
  
  if c == nbC-1 and l == nbL-1:
    return cases[nbL-1][nbC-1]
  
  elif memoRisk[c][l] != 0:
    return memoRisk[c][l]
    
  else : 
    
    if c< nbC-1 and not dejaPasse[c+1][l]:
      riskDroite = risk( c+1, l)
    else:
      riskDroite = interdit
      
    if l< nbL-1 and not dejaPasse[c][l+1]:
      riskBas = risk( c, l+1)
    else:
      riskBas = interdit

    if l>0 and not dejaPasse[c][l-1]:
      riskHaut = risk( c, l-1)
    else:
      riskHaut = interdit

    if c>0 and not dejaPasse[c-1][l]:
      riskGauche = risk( c-1, l)
    else:
      riskGauche = interdit

    res = cases[l][c] + min( riskDroite, riskBas, riskGauche, riskHaut)

    memoRisk[c][l] = res
    return res


#print ( risk(0,0) - cases[0][0])

print ( risk(8,8))

 






   
   
   
   
  
    



