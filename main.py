from  product import Product
from client import Client
from work import Work
from register import save_data , load_data


def main() :

    filename = "inventory.pkl"
    work = load_data(filename) or Work()

    while True :

        print("welcome to inventory system ")
        print("do u wanna go to products or clients settings ?")
        choice1=int(input("1/for product , 2/for clients: "))
        if choice1 == 1 :
            print("press 1 to view the list of products available ")
            print("press 2 to add a product to the list ")
            print('press 3 if u wanna remove a product from the list ')
            choice2= int(input("(1/2/3): "))
            if choice2 ==1 :
                work.view_product()
            elif choice2 ==2 :
                name= input("please enter the name of the product: ")
                id = int(input("please enter the id of the product : "))
                price =float(input("please enter the price of he product: "))
                stockage= int(input("please enter the stockage of the product : "))
                product = Product(name, id , price ,stockage)
                work.register_product(product)
                print("product is registered succesfully")
                save_data(filename , work)
            elif choice2 == 3 :
                work.view_product()
                index = int(input("please enter the index of product u wanna remove : "))
                work.remove_product(index)
                print("product is removed succesfully")
                save_data(filename ,work)

        elif choice1 ==2 :
            print("press 1 to view the list of clients ")
            print("press 2 to add a client to the list ")
            print('press 3 if u wanna remove a client from the list ')
            print('press 4 if u wanna add a product to a specific client ')
            choice3 = int(input('(1/2/3/4): '))

            if choice3 == 1:
                work.view_clients()

            elif choice3 == 2:
                name =input("please enter the name of the client to register : ")
                id = int(input("please enter the id number:  "))
                client = Client(name ,id)
                work.register_client(client)
                print("client is registered succesfully")
                save_data(filename , work)

            elif choice3==3 :
                work.view_clients()
                index = int(input("please enter the index of client u wanna remove : "))
                work.remove_client(index)
                print("client is removed succesfully")
                save_data(filename , work)
            elif choice3 ==4 :
                work.view_clients()
                client_index = int(input('please enter index of client u wanna add product to his cart: '))
                work.view_product()
                product_index= int(input("please enter the product index: "))
                work.add_cart(client_index , product_index)



if __name__ == "__main__":
    main()




















