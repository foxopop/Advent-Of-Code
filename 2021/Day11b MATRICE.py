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

nomFichier = "test11b.txt" 

nomFichier = "input11.txt" 



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

nbL = len(lines)
nbC = len(lines[0])

cases = [ [0 for c in range(nbC+2)] for l in range(nbL+2) ]
newZero = [ [False for c in range(nbC+2)] for l in range(nbL+2) ]

nbFlash = 0

for l in range( 0, nbL) :
  for c in range( 0, nbC) :
    cases[l+1][c+1] = int(lines[l][c])

afficherMatrice( cases, 2) 

auMoinsUnNew = False

nbSteps = 1000

for step in range(1,nbSteps+1):
  
  # on augmente de 1 ttes les cases, sauf bords
  for l in range( 1, nbL+1) :
    for c in range( 1, nbC+1) :
      new_val = (cases[l][c] + 1) % 10
      cases[l][c] =  new_val
      if new_val == 0:
        # on indique nouveau zero
        newZero[l][c] = True
        auMoinsUnNew = True
        nbFlash += 1

  print("CASES:")            
  afficherMatrice( cases, 2, False)   
  
 # print("NEWZERO:")  
  #afficherMatrice( newZero , 2)   


  # on augmente les voisins des nouveaux zeros modulo 10
  # tant qu'il reste des nouveaux zeros
  while auMoinsUnNew:
    auMoinsUnNew = False    
    for l in range( 1, nbL+1) :
      for c in range( 1, nbC+1) :
        if newZero[l][c] == True :
          newZero[l][c]  = False
          # on incremente ses voisins
          for dl in range(-1,+2):
            for dc in range(-1,+2):
                nl = l + dl
                nc = c + dc
                if not ( dl == 0  and dc == 0)  and cases[nl][nc] != 0:
                  new_val = (cases[nl][nc] + 1) % 10
                  cases[nl][nc] =  new_val
                  if new_val == 0:
                    # on indique nouveau zero
                    newZero[nl][nc] = True
                    auMoinsUnNew = True
                    nbFlash += 1
                  
  print("CASES:")            
  afficherMatrice( cases, 2, False)   


  if step==195:
    print( "step 195 = ", step)    
  
#  tousNuls = True
#  for l in range(1, nbL+1):
#    if not all( cases[l][c] == 0 for c in range(1,nbC+1)):

  if all( cases[l][c] == 0 for l,c in zip(range(1,nbL+1), range(1,nbC+1))  ):
    print( "step NUL = ", step)     
    break

    
#print (nbFlash )






 






   
   
   
   
  
    



