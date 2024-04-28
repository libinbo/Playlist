
from sang import Sang

class Spilleliste:
    def __init__(self, listenavn): 
        self._sanger = [] #lager en instansvariabel sang som er en liste 
        self._navn = listenavn #ny i
    def les_fil(self,filnavn): # metdode for å lese en fil 
        fil = open(filnavn)
        for linje in fil: # lager en for løkke for å kunen iterere gjennom filen 
            all_data = linje.strip().split(';') # bruker tjeneste strip og splitt for å kunne fjerne tegn legge til en liste.

            tittel= all_data[0] 

            artist= all_data[1]

            sang= Sang(artist,tittel)
            self._sanger.append(sang) 
        fil.close() #lukker filen.

    def legg_til_sang(self,ny_sang): #metode for å legge til en sang til listen vår 

        self._sanger.append(ny_sang) # ved hjelp av append legges sang objektene til listen 
    def fjern_sang(self,sang): # metode for å fjerne en sang fra listen 
        self._sanger.remove(sang) #bruker remove for å fjerne en sang fra listen 
    def spill_sang(self,sang):#metode for å spill sanger 
        sang.spill() #kaller på metoden spill 

    def spill_alle(self): # metode som gjør det mulig å spille alle sanger
        for u in self._sanger:
            u.spill()
    def finn_sang(self,tittel): #metode for å finne sanger 

        for u in self._sanger:  #lager en for løkke
            if u.sjekk_tittel(tittel)==True: # lager en if setning for å kunen gå gjennom alle sangene i listen
               return u # returenen den første sangen 
        return None #hvis den ikke finnes i listen, retuners det none 
    def hent_artist_utvalg(self,artistnavn): #metode for å kunne hente artistutvalget 
        utvalgavartist=[] # lager en tom liste 
        for k in self._sanger:  
            if k.sjekk_artist(artistnavn):  
                utvalgavartist.append(k) 
        return utvalgavartist #returner artistutvalget 