

class Client :


    def __init__(self , name , id ):
        self.name = name
        self.id = id
        self.cart=[]


    def __str__(self):
        return f"client name : {self.name} , ID : {self.id} , product in cart : {self.cart}"


    def add_cart(self , product ):
        self.cart.append(product)
