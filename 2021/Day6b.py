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
nomFichier = "input6.txt" 
#nomFichier = "test6.txt" 



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
    print(" ")
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


   
def getNbFils( age, j ):
  
  # print('age=',age," jour=",j)
  
  if j == 0:
    return 1
  elif (age,j) == (0,1) :
    return 2
  elif age==0:
    cle = str(age)+"_"+str(j)
    if nbFils[cle] != "":
      return nbFils[cle]
    else:
      res = getNbFils(6, j-1) + getNbFils(8, j-1)
      nbFils[cle] = res
      return res
  else:
    cle = str(age)+"_"+str(j)
    if nbFils[cle] != "":
      return nbFils[cle]
    else:
      res = getNbFils(age-1, j-1)
      nbFils[cle] = res
      return res
    
  
  
  

debug ("================= DEBUT ================")

lanterns = list( map (int, lines[0].split(',')) )

#print (lanterns)

#nbj = 256
nbj= 256

nbFils = defaultdict(str)

nbFils["0_1"] = 2

print ("<",nbFils["0_1"],">")

#print (lanterns)

nbTotal = 0
for l in lanterns:
  print ("lantern ",l)
  nb = getNbFils(l,nbj)
  #print( "nb fils = ", nb)
  nbTotal += nb
  
print (nbTotal)  

      















