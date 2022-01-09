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

#nomFichier = "test15.txt" 
nomFichier = "input15.txt" 



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
maxC = nbC-1
maxL = nbL-1

maxRisk = nbC * nbL * 10


bigNbL = len(lines)*5
bigNbC = len(lines[0])*5
bigMaxC = bigNbC-1
bigMaxL = bigNbL-1
bigMaxRisk = bigNbC * bigNbL * 10

arrivee = (bigMaxC,bigMaxL)


cases = [ [0 for c in range(bigNbC)] for l in range(bigNbL) ]
parcourus = [ [False for c in range(bigNbC)] for l in range(bigNbL) ]
riskMini = [ [ maxRisk for c in range(bigNbC)] for l in range(bigNbL) ]

for dupC in range (0,5):
  for dupL in range (0,5):
    
    decalC = dupC * nbC
    decalL = dupL * nbL
    
    
    #sous grille
    for l in range( 0, nbL) :
      for c in range( 0, nbC) :
        cases[l+decalL][c+decalC] = 1 + ( (int(lines[l][c]) -1 + dupC+dupL)% 9 )

afficherMatrice( cases, 2 , True)


coordFils = []
riskFils = []
peres = defaultdict(list)
riskPeres = defaultdict(lambda: bigMaxRisk)


coordFils.append( (0,0) )
riskFils.append(0)
parcourus[0][0] = True
riskMini[0][0] = 0
riskPeres['0-0'] = 0

def coder( c, l):
  return str(c) + '-' + str(l)

def ajouterFils( pCoord, pDc, pDl):
  
  (oldC,oldL) = pCoord
  c = oldC + pDc
  l = oldL + pDl
  
  if c <0 or c> bigMaxC:
    return False
  if l <0 or l> bigMaxL:
    return False
  
  newCoord = (c,l)
  
  #☻print (c,l)
  
#  if not parcourus[c][l]:
  newFils = coder(c,l)
  oldFils = coder(oldC,oldL)
  
  if (newFils not in peres[oldFils]) and (riskPeres[newFils] == bigMaxRisk ):
    coordFils.append(newCoord)   
    riskMini[c][l] = min( riskMini[c][l], riskPeres[oldFils]+ cases[c][l])
    riskFils.append( riskMini[c][l] )
    
    # parcourus[c][l] = True
    peres[newFils].append(oldFils)
    riskPeres[newFils] = riskMini[c][l] 

  if c == bigMaxC and l == bigMaxL:
    return True


arriveeTrouvee = False
while not arriveeTrouvee :

  
  # for i in range(len(coordFils)):

  # on cherche l'index du fils de moindre risque
  iMin = riskFils.index( min(riskFils) )
  
  # on avance sur son chemin
  #   1. on l'enleve de la liste des fils
  #   2. on ajoute ses fils
  
  # on l'enleve 
  filsCour = coordFils[iMin]
  coordFils.pop(iMin)
  riskFils.pop(iMin)
  
  # on ajoute ses voisins non parcourus
  for dc in range(-1,+2):
    for dl in range(-1,+2):
      if (dc ==0 or dl == 0) and ( dc != dl ):
        if ajouterFils( filsCour, dc, dl):
          arriveeTrouvee = True
        
#  afficherMatrice( riskMini, 5 , True)
    
    
          
      
print(riskMini[bigMaxC][bigMaxL]  )








   
   
   
   
  
    



