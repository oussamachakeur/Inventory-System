
class Product:

    def __init__(self, name , id , price , stockage):
        self.name= name
        self.id= id
        self.price= price
        self.stockage= stockage


    def __str__(self):
        return f"product name : {self.name} , id:{self.id} , price : $ {self.price} , quantity : {self.stockage}"