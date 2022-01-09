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

nomFichier = "test12.txt" 

nomFichier = "input12.txt" 



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

def calculeCle(ch, l):
    l2 = list(l)
    l2.sort()
    cle = ch + "-" + ''.join(l2)  
    return cle


def nbChemins( debut, interdits, chaine, secondeVisiteFaite ):

  #print ("Recherche nb chemins à partir de ", debut, " ",interdits)  
  
  cle = calculeCle(debut,interdits)
 # if nbCheminsCalcules[ cle ] != 0:
 #   return nbCheminsCalcules[ cle ] 

  #  return nbCheminsCalcules[debut]
      
  if debut == "end":
    #interdits.clear()
    #print("RESET interdits")
    print(chaine)
    print(" ")
    return 1
  else:
    if not debut.isupper():
      interdits.add(debut)   

    # on somme tous les chemins possibles
    nbSuiv = 0
    for suiv in suivants[debut]:
      if suiv not in interdits:
        #print(debut," -> ", suiv)
        chaine = chaine + "," + suiv
        nbSuiv += nbChemins(suiv, interdits.copy(), chaine, secondeVisiteFaite)
      elif not secondeVisiteFaite and suiv != "end" and suiv != "start" :
        chaine = chaine + "," + suiv
        nbSuiv += nbChemins(suiv, interdits.copy(), chaine, True)
      
    
    #nbCheminsCalcules[debut] = nbSuiv
    
    cle = calculeCle(debut,interdits)
    nbCheminsCalcules[cle] = nbSuiv
    
    return nbSuiv

#####################################################    LECTURE LIGNES
debug ("================= DEBUT ================")

nbL = len(lines)

suivants = defaultdict(set)

nbCheminsCalcules = defaultdict(int)

for l in lines:
  deb,fin = l.split('-')
  suivants[deb].add(fin)
  suivants[fin].add(deb)
  #print ( suivants )

interditsDebut = set()

secondeVisiteFaiteDebut = False

print ( nbChemins("start", interditsDebut, "start", secondeVisiteFaiteDebut ) )
print(" ")





 






   
   
   
   
  
    



