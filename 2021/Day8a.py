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
#nomFichier = "test8.txt" 
nomFichier = "input8.txt" 



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


nb =0

for l in lines:
  #print( l )
  
  droite = l.split('|')[1] 
  
  reps = droite.split(' ')
  reps.pop(0)
  print (reps)
  for ch in reps :
    print (len(ch))
    if len(ch) in (2,4,3,7):
      nb +=1
  
print(nb)  
  

debug ("================= DEBUT ================")

