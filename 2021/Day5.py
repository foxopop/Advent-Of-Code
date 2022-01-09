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







# Attention : volontairement écrasé par ci-dessous :

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""   Initialisation des entrées à partir de input1.txt : ne pas copier    """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nomFichier = ""
#nomFichier = "input5.txt" 
nomFichier = "test5.txt" 



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


   
def afficherMatrice( m, long=int(2)):
  print(" ")
  for y in range(len(m)):
    ligne = ""
    for x in range(len (m[y]) ):
      #contenu = str(m[y][x])
      contenu = m[y][x]
      #ligne += str(contenu)
      ligne += '{0:{width}}'.format( contenu, width=long)
      
    #print('{0:{width}}'.format( ligne, width=long) )
    print(ligne)
  
  
  

debug ("================= DEBUT ================")


def decode( s):

  s = s.replace(" -> ", ",")
  l = s.split(',')
  #print(l)
  return int(l[0]),int(l[1]), int(l[2]),int(l[3]) 
  



#on cherche le max x
maxX = 0
maxY = 0
for l in lines:
   xd,yd,xf,yf = decode(l)
   if xd > maxX :
     maxX = xd
   if xf > maxX :
     maxX = xf
   if yd > maxY :
     maxY = yd
   if yf > maxY :
     maxY = yf



print('maxX = ',maxX)     
print('maxY = ',maxY)     


# on construit le grille


# grilleVide = [0] * (maxX+1)
# grille = []
# for i in range(maxY+1):
#   grille.append(grilleVide.copy())


grille = [ [0 for c in range(maxY+1)] for l in range(maxX+1) ]


#print (grille)

for l in lines:
   xd,yd,xf,yf = decode(l)
   
   if (xd==xf or yd==yf)  :
     for x in range(min(xd,xf),max(xd,xf)+1)   :
       for y in range(min(yd,yf),max(yd,yf)+1)   :
         grille[y][x] = grille[y][x] + 1

   # diagonales
   if (abs(xd-xf) == abs(yd-yf)) :
     
       i=0
       if xf<xd: 
         rangex = -1
       else:
         rangex = +1
       if yf<yd: 
         rangey = -1
       else:
         rangey = +1
       
       for x in range(xd,xf+rangex, rangex)   :
         y = yd + i
         grille[y][x] = grille[y][x] + 1
         i = i + rangey
     

afficherMatrice(grille,2)

rep = 0
for x in range(0,maxX+1):
  for y in range(0,maxY+1):
    if (grille[y][x] >=2) :
      rep +=1
      
print(" ")
print(rep)      















