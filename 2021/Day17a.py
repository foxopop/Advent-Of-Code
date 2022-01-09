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
from  math import ceil

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""   Initialisation en dur des entrées : ne pas copier  """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lines = []


lines.append("150")
lines.append("160")
lines.append("140")
lines.append("170")
lines.append("180")



# Attention : volontairement écrasé par ci-dessous :

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""   Initialisation des entrées à partir de input1.txt : ne pas copier    """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nomFichier = "test17a.txt" 
#nomFichier = "input17.txt"




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

  

#####################################################    LECTURE LIGNES


debug ("================= DEBUT ================")


print ( lines[0])
print("")

ch = lines[0].split('=')
plageX= ch[1]
plageY=ch[2]

xMin = int( plageX.split('..')[0] )
xMax = int( plageX.split('..')[1].split(',')[0] )
yMin = int( plageY.split('..')[0] )
yMax = int( plageY.split('..')[1].split(',')[0] )


# calcul de xMin   et nXMin
vXMin = 0
x = 0
nXMin = 0
while x < xMin:
  vXMin += 1
  x = x + vXMin
  nXMin += 1
print ("vXmin =", vXMin)
print ("nXmin =", vXMin)


vXMax = vXMin
while x < xMax:
  vXMax += 1
  x = x + vXMin
vXMax -=1
print ("vXMax =", vXMax)


# calcul du vYmin
# vYMin = 0
# y = 0
# nYMIn=0
# while y < yMin:
#   vYMin += 1
#   nYMin += 1
#   y = y + vXMin
# print ("vXmin =", vXMin)

svY = 0
vYMax = 0
step = 0
yFinal = 0

yPlusHaut= 0

# pb ci-dessous : condition de fin à trouver !

while  svY < 1000 :
  
  y = 0  
  
  # on teste la solution vY avec n entre nXmin et nXmax
  n = nXMin
  while n < 100 :
    
    vY = svY
    
    # on teste la solution vY avec n steps
    print ("Essai avec vY=",vY," en ",n, " coups")
    print(" ")
    for st in range(0,n):
      y += vY
      if y>yPlusHaut:
        yPlusHaut = y
      vY -= 1
      
    # après n steps : test si y dans la fourchette 
    if y>= yMin and y <= yMax:
      vYMax = svY
      print ("ok avec vY=",vYMax," en ",n," coups. Hauteur max = ", yPlusHaut )
     
    n += 1  
     
    # on memorise le yFinal
  yFinal = y
      
      
  svY +=1    
  
  
  


print("")
    
print('REP=',"")    
  
  









