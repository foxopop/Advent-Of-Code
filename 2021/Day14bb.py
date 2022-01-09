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
from collections import defaultdict, Counter

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




def cle( ch, nIter):
  return( ch + "-" + str(nIter))

milieuPaires = dict()
 


    
 
#-------------------------------------
def cle( pPaire, pNiv):
  ch = pPaire + "-" + str(pNiv)
  return ch
 

 

 
#=============================================
 

# TRAITEMENT PRINCIPAL
 
nbIterations = 40
chInit = lines[0]

nbPaires = Counter()
nbLettres = Counter()


#-----------------------------------
# initialisation des tranco de base
 
for i in range(2, len(lines) ):
  # NN -> NCN
  ligne = lines[i]
  valeur =  ligne[6] 
  
  clef = ligne[0:2]
  milieuPaires[clef] = valeur
  
 
#---------------------


#on compte les paires de depart
chDepart = lines[0]
for i in range(0, len(chDepart)-1) :
  ch = chDepart[i:i+2]
  nbPaires[ch] += 1
  nbLettres[ch[0]] +=1

nbLettres[chDepart[-1]] +=1


print ("chInit : ", chInit)



nbIter = 40



for i in range(0, nbIter):
  
  print ("Iteration ",i+1)
  
  nbNewPaires = Counter()
  
  # une boucle
  for pa in nbPaires:
    
    lettreAjoutee = milieuPaires[ pa ]
    nbLettres[lettreAjoutee] += nbPaires[pa]

    newGauche = pa[0] + lettreAjoutee
    nbNewPaires[newGauche] += nbPaires[pa]
      
    newDroite = lettreAjoutee + pa[1]
    nbNewPaires[newDroite] += nbPaires[pa]
    
  print(nbLettres)
  
  nbPaires = nbNewPaires.copy()
    





  

print(" ")
print ("FIN")

print (nbLettres)
 
#elements = list( chResult )

#print ("transfo finie : ", chInit, " -> ", chResult)

#elementsCounter = collections.Counter( elements )

nbMost = nbLettres.most_common(1)[0][1] 
nbLess = nbLettres.most_common()[:-2:-1][0][1]

print ("FIN : ",nbMost - nbLess)
 

 


 






   
   
   
   
  
    



