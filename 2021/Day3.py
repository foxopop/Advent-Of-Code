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

gamma = ''
epsilon = ''

for l in lines:
  
  print(l)
  
  for i in range(0, long):
    if l[i] == '1':
      nbBit1[i] += 1
    
print ( nbBit1 )    

for n in nbBit1:
  if n > len(lines)/2 :
    gamma = gamma + '1'
    epsilon = epsilon + '0'
  else:
    gamma = gamma + '0'
    epsilon = epsilon + '1'

g = int(gamma,2)
e = int(epsilon,2)

print (gamma,  g)    
print (epsilon,  e) 
print ( g * e )   









