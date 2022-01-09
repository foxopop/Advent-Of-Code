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
#nomFichier = "input6.txt" 
nomFichier = "test6.txt" 



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

#####################################################    LECTURE LIGNES


   

  
  
  

debug ("================= DEBUT ================")

lanterns = list( map (int, lines[0].split(',')) )

#print (lanterns)

nbj = 256

for j in range(1, nbj +1):

  print ('====> jour ',j)  

  newLanterns = lanterns.copy()
  
  for i in range(len(lanterns)):
   

    # naissances
    if newLanterns[i] == 0 :
      newLanterns.append(8)

    #murissement
    if lanterns[i] <= 6:
      newLanterns[i] = (lanterns[i] - 1) % 7
    else:
      #• jeune lanterne
      newLanterns[i] = lanterns[i] - 1

      
  #  print( lanterns[i],"->", newLanterns[i]  )

      
  #☻print(newLanterns)      
      
  lanterns = newLanterns   

print (len(lanterns))   
      
      















