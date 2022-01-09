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
#nomFichier = "test8b.txt" 
nomFichier = "input8.txt" 



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

codage=defaultdict(set)
decode=defaultdict(set)


nb =0

total = 0

for l in lines:
  #print( l )
  
  droite = l.split('|')[1]   
  reps = droite.split(' ')
  reps.pop(0)
  #print (reps)

  gauche = l.split('|')[0]   
  gauche = gauche.split(' ')
  gauche.pop(10)

  # premiere passe : on trouve 1, 4 7 et 8

  for ch in gauche :
    
    if len(ch) == 2 :
      # chiffre '1'
      un = set(ch)
      codage["1"] = un
      
    if len(ch) == 4 :
      # chiffre '4'
      quatre = set(ch)
      codage["4"] = quatre
      
    if len(ch) == 3 :
      # chiffre '7'
      sept = set(ch)
      codage["7"] = sept
      
    if len(ch) == 7 :
      # chiffre '8'
      huit = set(ch)
      codage["8"] = huit
      

    

      
  # seconde passe : on trouve 1, 4 7 et 8

  for ch in gauche :
    
    sch = set(ch)    

    # si 5 segments
    if len(ch) == 5 :
      
      
      if len( (huit.difference(quatre)) - sch ) ==  0:
      
        # chiffre '2'
        codage["2"] = sch
      elif len(un - sch) == 0:
        # chiffre ''
        codage["3"] = sch
      else:
        codage["5"] = sch
        
    # si 6 segments
    if len(ch) == 6 :
      if len(un - sch) > 0:
        # chiffre '6'
        codage["6"] = sch
      elif len( (huit.difference(quatre)) - sch ) ==  0:
        # chiffre '0'
        codage["0"] = sch
      else:
        codage["9"] = sch
  
  print(" ")        


  if len(codage) < 10:
    print("Codage incomplet : ligne ", )
        
  for s in codage:
    try:
      print(s, codage[s]) 
      cht = ''.join(sorted(codage[s]))
      decode[cht] = s
    except:
      print("erreur")    

  
  print(" ")  

  
  droite = l.split('|')[1]  
  reps = droite.split(' ')
  reps.pop(0)

  sstotal = ""
  nch=""
 
  for code in reps:
    
    # un chiffre

    cht = ''.join(sorted(code))
    nch += decode[ cht ]

  sstotal += ''.join(nch)
  
  print(sstotal)
  print(int(sstotal))
  total += int(sstotal)
  
print (total)  
    
    

      
      
    

  

debug ("================= DEBUT ================")

