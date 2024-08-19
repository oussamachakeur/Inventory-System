

from client import Client

class Work : 
    
    
    def __init__(self):
        self.products=[]
        self.clients = []
        
        
    def register_product(self , product):
        self.products.append(product)
        
        
    def register_client(self , client):
        self.clients.append(client)
        
    
    def view_product(self):
        for i , product in enumerate(self.products):
            print(f"{i}. {product}")

    def view_clients(self):
        for i, client in enumerate(self.clients):
            print(f"{i}. {client}")

    def remove_product(self,index ):
        if 0<=index<len(self.products):
            del self.products[index]

    def remove_client(self,index ):
        if 0<=index<len(self.clients):
            del self.clients[index]

    def add_cart(self , client_index , product_index):
        if 0<=product_index<(len(self.products)) and 0<=client_index<(len(self.clients)):
            product=self.products[product_index]
            client = self.clients[client_index]
            client.add_cart(product)




