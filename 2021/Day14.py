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

nomFichier = "test14.txt" 

nomFichier = "input14.txt" 



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


 
  


#####################################################    LECTURE LIGNES
debug ("================= DEBUT ================")


chDepart = lines[0]
modifs=[]

for i in range(2, len(lines)):
  ch = lines[i]
  triplet = (ch[0],ch[1],ch[6] )
  modifs.append( triplet)
  print(triplet)


chCourant = chDepart

def appliquerInsert( pCh, pTriplet, pCh2 ):

  # pCh2="x"

  # for c in pCh:
  #   pCh2 = pCh2 + c + '.'
  # pCh2 = pCh2.replace('x','')
    
  for i in range(1, len(pCh2)-1, 2):
    if pCh2[i-1] == pTriplet[0] and pCh2[i+1] == pTriplet[1]:
      pCh2 = pCh2[:i]+ pTriplet[2] + pCh2[i+1:]
      #pCh2[i] = pTriplet[2]
      
  #on enleve tous les points

  return pCh2  #.replace('.','')  
      






for s in range(0,10):
  
  
  print ("STEP ", s)
  
  Ch2="x"
  for c in chDepart:
    Ch2 = Ch2 + c + '.'
  Ch2 = Ch2.replace('x','')
  Ch2 = Ch2[:-1]  
  
  print (".")
  
  # step 1  
  for mod in modifs:
    print ( " Appliquer", mod, " sur ", chDepart )
    Ch2 = appliquerInsert( chDepart, mod, Ch2)
    
  chDepart = Ch2.replace('.','')  
  print( "chDepart=",chDepart)
  
  elements = list(chDepart)
 
  elementsCounter = collections.Counter( elements )

  nbMost = elementsCounter.most_common(1)[0][1] 
  nbLess = elementsCounter.most_common()[:-2:-1][0][1]
    
  
  print(nbMost - nbLess)
  
  
    




 






   
   
   
   
  
    



