class Vehicule:
    def __init__(self,marque,vitesse_max):
        self._marque=marque
        self.__vitess_max=vitesse_max

    @property
    def vitesse_max(self):
        return self.__vitesse_max

    @vitesse_max.setter
    def vitesse_max(self,value):
        self.__vitesse_max=value

    def __str__(self):
        return f"vehicle marque is {self._marque} and the max speed is {self.__vitesse_max} "

    def __eq__(self,auter):
        return self._marque == auter._marque
    
    def deplacer(self):
        return f"this is a vehicle class with marque ({self._marque}) "

class Voiture(Vehicule):
    def __init__(self, marque, vitesse_max,portes):
        super().__init__(marque, vitesse_max)
        self.portes=portes

    def deplacer(self):
        return f"the vehicle marque is {self._marque} with {self.portes} doors"
        

class Moto(Vehicule):
    def __init__(self, marque, vitesse_max):
        super().__init__(marque, vitesse_max)

    def deplacer(self):
        return f"the vehicle marque is {self._marque}"


v1=Vehicule("ferrari",2100)
v2=Voiture("ford",213,4)
v3=Moto("kawazaki","450")
Vehicules=[v1,v2,v3]
for v in Vehicules:
    print(v.deplacer())


print(v1==v2)
