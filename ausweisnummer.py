#!/Applications/Anaconda3/anaconda/bin/python

erlaubte_zeichen='1 2 3 4 5 6 7 8 9 0 C F G H J K L M N P R T V W X Y Z'.split()
def zeichen_erlaubt(x): return x in erlaubte_zeichen
gewichtung=[7, 3, 1, 7, 3, 1, 7, 3, 1]
def char_to_number(x): return ord(x)-ord('A')+10
def anything_to_number(x): return int(x) if x.isnumeric() else char_to_number(x) 

# https://de.wikipedia.org/wiki/Ausweisnummer#Berechnung_der_Prüfziffern
def check_ausweisnummer_nov2010_old(ausweisnummer):
   if False in [zeichen_erlaubt(x) for x in ausweisnummer]:
       raise Exception("Enthält ungültige Zeichen:", [x for x in ausweisnummer if zeichen_erlaubt(x)==False])
    
   if len(ausweisnummer)!=10:
      raise Exception("Es werden genau 10 Zeichen verlangt, wir haben aber:", len(ausweisnummer) )

   checksumme_gegeben=anything_to_number( ausweisnummer[-1] )
   ausweisnummer_without_check=ausweisnummer[:-1]
 
   ausweisnummer_as_list_simple_without_check=[x for x in ausweisnummer_without_check] # e.g. ['T', '2', '2', '0', '0', '0', '1', '2', '9',]
   ausweisnummer_as_list_number_without_check=[ anything_to_number(x) for x in ausweisnummer_as_list_simple_without_check  ] # e.g. [29, 2, 2, 0, 0, 0, 1, 2, 9,]

   pairs=zip(ausweisnummer_as_list_number_without_check,gewichtung) # [(29, 7), (2, 3), (2, 1), (0, 7), (0, 3), (0, 1), (1, 7), (2, 3), (9, 1)]

   
   # Die Endziffern (Einerstelle) der Produkte werden addiert
   produkte_alle_stellen=[(x*y) for x,y in pairs]   # [203, 6, 2, 0, 0, 0, 7, 6, 9]
   produkte_letzte_stellen=[x%10 for x in produkte_alle_stellen] # [3, 6, 2, 0, 0, 0, 7, 6, 9]   
   checksumme_berechnet=sum(produkte_letzte_stellen)%10

   if checksumme_gegeben != checksumme_berechnet:
     raise Exception("Checksumme falsch", checksumme_gegeben , checksumme_berechnet )

   return True


# type: string -> (bool,reason)
def check_ausweisnummer_nov2010(ausweisnummer):
    return
    

# Alternativer Ansatz ohne Exceptions

"""

okay,reason=check_ausweisnummer_nov2010("T220001292") # Erika Mustermann (stimmt)
# erwartete Antwort True,"ok"


okay,reason=check_ausweisnummer_nov2010("T22000129A") # Erika Mustermann (falsch)
# erwartete Antwort False,"Enthält ungültige Zeichen: [A]"

"""
