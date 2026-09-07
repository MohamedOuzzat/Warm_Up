class Voiture:
    def __init__(self,marque:str,modele:str,prix:float,kilometrage:int =0):
        self.marque=marque
        self.modele=modele
        self.prix=prix
        self.kilometrage=kilometrage

    def afficher_info(self):
        return f"Marque: {self.marque} | Modèle: {self.modele} | Prix: {self.prix} | Kilométrage: {self.kilometrage}"


class VoitureElectrique(Voiture):
    def __init__(self, marque, modele, prix, kilometrage,autonomie):
        super().__init__(marque, modele, prix, kilometrage)
        self.autonomie=autonomie

    def afficher_info(self):
        return f"Marque: {self.marque} | Modèle: {self.modele} | Prix: {self.prix} | Kilométrage: {self} | Autonomie: {self.autonomie} km"


class Concession:
    def __init__(self,nom:str,inventaire:list =[]):
        self.nom=nom
        self.inventaire=inventaire

    def ajouter_voiture(self,voiture):
        
        self.inventaire.append(voiture)

    def afficher_inventaire(self):
        for v in self.inventaire:
            print(v.afficher_info())

    def vendre_voiture(self,marque, modele):
        for v in self.inventaire:
            if v.marque == marque and v.modele == modele:
                return f"La voiture {marque} {modele} a été vendue"

            
        print("la voiture n’a pas été trouvée")


    def total_prix(self):
        total=0
        for i in self.inventaire:
            total+=i.prix
        return total

    def moyenne_prix(self):
        moyenne_prix=self.total_prix()/len(self.inventaire)

        return moyenne_prix

    def __str__(self):
        return f"nom : {self.nom} | vehciles number : {len(self.inventaire)}"


c=Concession("Concession du Centre")

v1=VoitureElectrique("cybertrack","Tesla",20000,987896,"auto")
v2=Voiture("dacia","logan",2000,32442)
v3=Voiture("mercides","G-class",9203,99282)
v4=Voiture("hello","idksdk",989,908)

Voitures=[v1,v2,v3]
for v in Voitures:
    c.ajouter_voiture(v)

c.afficher_inventaire()


c.vendre_voiture("hello","hello")


# print(c)

        

    


        