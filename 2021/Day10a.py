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

nomFichier = "test10.txt" 

nomFichier = "input10.txt" 



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

def afficherMatrice( m, long=int(2)):
  #print(" ")
  for y in range(len(m)):
    ligne = ""
    for x in range(len (m[y]) ):
      #contenu = str(m[y][x])
      contenu = m[y][x]
      #ligne += str(contenu)
      ligne += '{0:{width}}'.format( contenu, width=long)
      
    #print('{0:{width}}'.format( ligne, width=long) )
    print(ligne)

#####################################################    LECTURE LIGNES

err = dict()
err[')']=3
err[']']=57
err['}']=1197
err['>']=25137

rev = dict()
rev[')']='('
rev[']']='['
rev['}']='{'
rev['>']='<'

valeur = dict()
valeur['(']=1
valeur['[']=2
valeur['{']=3
valeur['<']=4


def valeurErreur( l ):
  pile = []
  for c in l:
    if c in ('<','[','(','{'):
      pile.append(c)
    if c in ('>',']',')','}'):  
      indexDernier = len(pile)-1
      
      if (pile[ len(pile)-1 ] == rev[str(c)] ):
        
        pile.pop( indexDernier )
      else:
        return err[c]
  return 0

def valeurComplement( l ):
  pile = []
  val = 0

  # on enleve tout ce qui se ferme bien  
  for c in l:
    if c in ('<','[','(','{'):
      pile.append(c)
    if c in ('>',']',')','}'):  
      indexDernier = len(pile)-1
      
      if (pile[ len(pile)-1 ] == rev[str(c)] ):
        
        pile.pop( indexDernier )
      else:
        return err[c]
      
  # si la pile est vide, il faut completer
  while len(pile)>0:
    val = val * 5
    indexDernier = len(pile)-1
    val += valeur[pile[indexDernier]]
    print ("val= ", val)
    pile.pop( indexDernier )
    
  return val
    




debug ("================= DEBUT ================")

liste = []


for l in lines:
  
  total = 0
  e = valeurErreur(l)
  
  if e == 0:

      # ligne a completer
      v = valeurComplement(l)
      print ("v=",v)
      total += v
      
      print(total)  
      liste.append(total)
  
  
liste.sort()

print(liste)
 
while ( len(liste) >1):
 indexDernier = len(liste)-1
 liste.pop( indexDernier )
 liste.pop(0)
 print (liste)
 
   
   
   
   
  
    



