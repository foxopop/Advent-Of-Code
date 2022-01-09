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

#nomFichier = "input14.txt" 



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


transfos = dict()

def cle( ch, nIter):
  return( ch + "-" + str(nIter))

for i in range(2, len(lines)):
  ch = lines[i]
  triplet = (ch[0],ch[1],ch[6] )
  modifs.append( triplet)
  print(triplet)


chCourant = chDepart

def appliquerInsert( pCh, pTriplet, pCh2 ):

  # pCh  = NNCB
  # pCh2 = N.N.C.B
  
  for i in range(1, len(pCh2)-1, 2):
    if pCh2[i-1] == pTriplet[0] and pCh2[i+1] == pTriplet[1]:
      pCh2 = pCh2[:i]+ pTriplet[2] + pCh2[i+1:]
      
  return pCh2   


def transfo( ch, nITer):
  
  print (nITer)
  
  try:
    chT = transfos[ cle(ch,nITer)]
    return chT
      
  except:
  
    if len(ch) == 1:
      return ch
      
    else:  
      chRes = ""
      
    # ch = NCN
    #for i in range(len(ch)-1):
      ch2Car = ch[0:2]
      chReste = ch[1:]
      if nITer>0:
        
        chGaucheAvant = transfo( ch2Car, nITer - 1)
        if len(chGaucheAvant)>1:
          clef = cle(ch2Car,nITer-1)
          transfos[clef ] = chGaucheAvant
        chGauche = unStep( chGaucheAvant )
        if len(chGauche)>1:     
          clef = cle(chGaucheAvant,0)          
          transfos[ clef ] = chGauche
          clef2 = cle(ch2Car,1)          
          transfos[ clef2 ] = chGauche
        
        chDroiteApres = transfo( chReste, nITer)
        if len(chDroiteApres)>1:
          transfos[ cle(chReste,nITer)] = chDroiteApres
        #chDroite = unStep( chDroiteApres )
        #if len(chDroite)>1:
        #  clef = cle(chDroiteApres,0)
        #  transfos[clef ] = chDroite
        
        
        ##chRes += chGauche + chDroite[1:]
        chRes += chGauche + chDroiteApres[1:]
      else:
        chGauche = unStep( ch2Car)
        chDroite = transfo( chReste, nITer)
        chRes += chGauche + chDroite[1:]
    
    if len(chRes)>1:
      clef = cle(ch,nITer)
      transfos[ clef ] = chRes
    return chRes
  

def unStep(chDepart):

  
  try:
    dejaCalcule = transfos[ chDepart, 0 ]     
    return dejaCalcule
  except:
  
    Ch2 = dedouble(chDepart)
  
    chDepartOrigin = chDepart
  
    # step 1  
    for mod in modifs:
      #print ( " Appliquer", mod, " sur ", chDepart )
      Ch2 = appliquerInsert( chDepart, mod, Ch2)
        
      chDepartNext = Ch2.replace('.','')  
  
      chDepart = chDepartNext
      
    if len(chDepart)>1:
      clef = cle(chDepartOrigin,0)
      transfos[clef ] = chDepart

    for i in range(1, len(chDepart)-1, 2):
      clef = cle(  chDepart[i-1]+chDepart[i+1]  ,0)
      triplet = chDepart[i-1:i+2]
      transfos[ clef ] = triplet
      
    return chDepart  
    

def dedouble (pCh ):
  ch2 = pCh[0]
  for c in pCh[1:]:
    ch2 = ch2 + "." + c
  return ch2

nbIterations = 3
chInit = "NN"  # lines[0]

#chResult = transfo( lines[0] , nbIterations-1 ) 

chResult = transfo( chInit , nbIterations-1 ) 

elements = list( chResult )

print ("transfo finie : ", chInit, " -> ", chResult)

elementsCounter = collections.Counter( elements )

nbMost = elementsCounter.most_common(1)[0][1] 
nbLess = elementsCounter.most_common()[:-2:-1][0][1]
    

  
print(nbMost - nbLess)

  
  
  
    




 






   
   
   
   
  
    



