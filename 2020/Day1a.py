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
#nomFichier = "test1a.txt" 
nomFichier = "input1a.txt" 



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


def couplePour( somme ):
  for i in nbs:
    if (somme - i) != i :
      if (somme - i) in nbs:
        #print(somme - i)
        return (i, somme-i)
    else :
      if nbs.count(i) == 2:
        #print(somme - i)
        return (i, somme-i)
  return(-1,-1)
    
  
  
  

debug ("================= DEBUT ================")

nbs = list(map( int,lines))
print (nbs)
      

print(" ")


for a in nbs:

  somme = 2020 -a
  (b,c) = couplePour(somme)
  
  if (b,c) != (-1,-1):
      print(a,b,c)
      break;


print ( a, " + ",b, " + ", c," = ",a + b + c)
print ( a, " x ",b, " x ", c," = ",a * b * c)

      















