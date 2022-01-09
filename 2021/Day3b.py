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

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""   Initialisation en dur des entrées : ne pas copier  """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lines = []




lines.append("forward 9")
lines.append("down 9")
lines.append("up 4")
lines.append("down 5")
lines.append("down 6")
lines.append("up 6")
lines.append("down 7")



# Attention : volontairement écrasé par ci-dessous :

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""   Initialisation des entrées à partir de input1.txt : ne pas copier    """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nomFichier = ""
nomFichier = "input3.txt" 
#nomFichier = "test3.txt" 



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


x = 0
y = 0
aim=0

long = len(lines[0]) 

nbBit1 = [0] * long
nbBit0 = [0] * long

oxyMax = ''
coMin = ''


newLinesMax = lines
newLinesMin = lines

finMin = False
finMax = False

  
for i in range(0, long):
  
  linesMaxUn = []
  linesMaxZero = []

  linesMinUn = []
  linesMinZero = []

  for l in newLinesMax:
 
    if l[i] == '1':
      nbBit1[i] += 1
      linesMaxUn.append(l) 
    else:
      nbBit0[i] += 1
      linesMaxZero.append(l) 
      

  for l in newLinesMin:
 
    if l[i] == '1':
      nbBit1[i] += 1
      linesMinUn.append(l) 
    else:
      nbBit0[i] += 1
      linesMinZero.append(l) 

    
  if len(linesMaxUn) >= len (linesMaxZero):

    if not finMax:
      newLinesMax = linesMaxUn

  else :    
    if not finMax:
      newLinesMax = linesMaxZero


  if len(linesMinUn) >= len (linesMinZero):

    if not finMin:
      newLinesMin = linesMinZero
      print (newLinesMin)
    
  else :    
      
    if not finMin:
      newLinesMin = linesMinUn
      print (newLinesMin)    
    
  if len(newLinesMax) == 1:
    oxyMax = int(newLinesMax[0],2)
    print ( "oxy=",oxyMax )
    finMax = True

  if len(newLinesMin) == 1:
    coMin = int(newLinesMin[0],2)
    print ( "Co=",coMin )
    finMin = True

print ( coMin * oxyMax)











