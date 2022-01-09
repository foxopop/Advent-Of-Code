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


lines.append("150")
lines.append("160")
lines.append("140")
lines.append("170")
lines.append("180")



# Attention : volontairement écrasé par ci-dessous :

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""   Initialisation des entrées à partir de input1.txt : ne pas copier    """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#nomFichier = "input16.txt" 
#nomFichier = "test16Lit.txt"
#nomFichier = "test16OperLg.txt"
nomFichier = "test16Autres1.txt"
nomFichier = "test16_1200.txt"
nomFichier = "test16a_F478.txt"
nomFichier = "test16a_8E34.txt"
nomFichier = "test16a_2340.txt"
nomFichier = "test16a_4780.txt"
nomFichier = "input16a.txt"

#nomFichier = "test16b_0A82.txt"




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


def getLongEtdecodePaquet( pPaq, pDebut ):
  global totalVersions  
  
  print("")
  
  p = pDebut
  
  version = pPaq[p:p+3:] 
  print ("version = ",version)
  p+=3
  totalVersions += int(version,2)
  print ("totalVersions = ", totalVersions)

  
  typePaq = pPaq[p:p+3:] 
  print ("type = ",typePaq)
  p+=3
  
  ## paquet Litteral
  
  if typePaq == '100':
   
    literral = ""
    # tq pas le dernier octet
    while pPaq[p] == '1' :
      literral += pPaq[p+1:p+5]
      p += 5
    literral += pPaq[p+1:p+5]
    p += 5 
      
    print ("Literral = ",literral," = ",int(literral,2))
    print("")
    #print ("Long Paquet = ", p - pDebut)
    return ( (p - pDebut), int(literral,2) )
    
  ## paquet Operateur
  
  elif typePaq != '100':
    
    typeLgPaq = pPaq[pDebut+6]
    
    ### type longueur 0 = longueur 
    
    if typeLgPaq == '0':
      longPaq = int(pPaq[pDebut+7:pDebut+18],2)
      print ("paquets à suivre de longueur ", longPaq)
      
      p = pDebut + 7
      lgSousPaquets = int(pPaq[p:p+15],2)

      pDebOper = pDebut +7 +15

      sousPaquets = pPaq[pDebOper:pDebOper+lgSousPaquets]
      print("Operateur (type Lg) = ", sousPaquets)      
      #print ("Long Paquet = ", lgSousPaquets)      
      
      #### on decode les sous paquets
      
      pCour = 0
            
      pCour = 0
      lCour, res  = getLongEtdecodePaquet( sousPaquets, pCour )
      pCour += lCour
      while pCour < lgSousPaquets:
        lCour, res2  = getLongEtdecodePaquet( sousPaquets, pCour )
        
        if typePaq == '000' : # somme
          res += res2
        elif typePaq == '001' : # somme
          res *= res2
        elif typePaq == '010' : # somme
          res = min ( res, res2)
        elif typePaq == '011' : # somme
          res = max ( res, res2)
        elif typePaq == '101' : # somme
          res = ( res > res2)
        elif typePaq == '110' : # somme
          res = ( res < res2)
        elif typePaq == '111' : # somme
          res = ( res == res2)
        
        pCour += lCour
      
      return lgSousPaquets +7 +15, res
    

    ### type longueur 1 = nb paquets
    
    if typeLgPaq == '1':
      nbPaq = int(pPaq[pDebut+7:pDebut+18],2)
      print (nbPaq," paquets à suivre :")
      
      pCour = pDebut+7+11
      
      sousPaquets = pPaq[pCour:]
      
      pCour = 0
      
      lCour, res = getLongEtdecodePaquet( sousPaquets, pCour )
      pCour += lCour
      
      for p in range(1,nbPaq):
        print("")
        print ( 'paquet ', p, ' :')
        lCour, res2 = getLongEtdecodePaquet( sousPaquets, pCour )
        
        if typePaq == '000' : # somme
          res += res2
        elif typePaq == '001' : # somme
          res *= res2
        elif typePaq == '010' : # somme
          res = min ( res, res2)
        elif typePaq == '011' : # somme
          res = max ( res, res2)
        elif typePaq == '101' : # somme
          res = ( res > res2)
        elif typePaq == '110' : # somme
          res = ( res < res2)
        elif typePaq == '111' : # somme
          res = ( res == res2)        
        
        pCour += lCour
        
      return pCour +7 +11, res
        

rep = 0

debug ("================= DEBUT ================")


entree = lines[0]

print (entree)

entreeBin = bin( int(entree, 16) )[2:]

print ("")

while len(entreeBin ) % 4 != 0: 
  entreeBin = '0'+entreeBin

print( entreeBin ) 

totalVersions = 0

l, res = getLongEtdecodePaquet( entreeBin, 0 )


    
print('REP=', res)    
  
  









