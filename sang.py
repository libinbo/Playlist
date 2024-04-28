class Sang: # lager klassen sang 

    def __init__(self,artist, tittel): #danner en kosntruktår, med paramenters artist og titel 

        self._tittel=tittel  # danner instansvariablen tittel og artist
        self._artist=artist 


    def spill(self): # en metode for å kunne spille sanger 
        print("Nå spilles:" , self._tittel , "av", self._artist) # lager en print setning med info om sangen arist og tittel 
    
    def sjekk_artist(self,navn): # en metode fom sjekker artisten 
       
        for l in navn.split(" "):  # lager en for løkke som gjør det mulig å kunne fjerne tegn og legger til en liste

            if l in self._artist.split(" "): # her gjøres det samme samtidg som den returner true så lenge et ord i aristit navnet er likt feks så skal det være mulig å finne lord gaga, siden den består av ordet gaga.
       
                return True 
        
        
        return False  # hvis ikke returners false 
    def sjekk_tittel(self,tittel): # en metode som sjekker titellen 
        return tittel.lower() == self._tittel.lower() 
    
    def sjekk_artist_og_tittel(self,artist,tittel): # en metode som sjekker både artist og tittelen

        return self.sjekk_tittel(tittel) and self.sjekk_artist(artist) # skal kunen returner både titelen og artisten.
