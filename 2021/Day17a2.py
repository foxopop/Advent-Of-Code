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
nomFichier = "input17.txt"




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


# Y au plus haut quand x = xMax lorsque Vx = 0
vXMax = 0
x=0
while x <= xMax:
  vXMax += 1
  x = x + vXMax
xCible = x-vXMax
vXMax -=1

print ("vXMax =", vXMax)
print ("xCible =", xCible)


vYMAx = -yMin -1




vX = vXMax
vY = vYMAx

# on teste la solution avec vY

x=0
y=0
yHaut = 0

while y > yMax:
  x = x+vX
  y = y+vY
  
  #print ("y=",y)
  
  vX = max(0,vX-1)
  vY = vY-1
  if y > yHaut :
    yHaut = y
  
print("A la fin : x=",x, 'y=',y)
    
print('Y MAX =', yHaut)    
  
  









