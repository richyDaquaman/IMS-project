# 1. 🛒 Simple Inventory Management System
# Features:

# Add product (name, quantity, price)

# View all products

# Update product quantity

# Delete product


class sims:

    def __init__(self):

        # self.productname = input('Enter product name: ')
        # self.quantity = int(input('Enter product quantity: '))
        # self.price = int(input('Enter price: '))
        self.food_prod = {"Name":"Rice", "Quantity":50, "Price": 50000}
        self.drinks_prod = {"Name":"Pepsi", "Quantity":100, "Price": 500000}
        self.bev_prod = {"Name":"Milk", "Quantity":10, "Price": 10000}
        self.prod = {
            "Food": self.food_prod,
            "Drinks": self.drinks_prod,
            "Beverage": self.bev_prod
        }

        self.alls()

# method

    # all
    def alls(self):
        self.ori = input(""" Enter 1 to add product
                        Enter 2 to view all
                        Enter 3 to update product
                        Enter 4 to delete product
                        Enter 5 to quit: """)
        
        if self.ori == "1":
            self.productname = input('Enter product name: ')
            self.quantity = int(input('Enter product quantity: '))
            self.price = int(input('Enter price: '))
            self.add_product()
        elif self.ori == "2":
            self.view_pro()
        elif self.ori == "3":
            self.update_prod()
        elif self.ori == "4":
            self.delete_prod()
        elif self.ori == "5":
            quit()
        else:
            print('Invalid Input')


    # add product
    def add_product(self):
        self.new = {"Name":self.productname, "Quantity":self.quantity, "Price":self.price}
        print(self.new)
        self.tryagain()

#   view all product

    def view_pro(self):
        print(self.prod)
        self.tryagain()

    
    # update
    def update_prod(self):
        self.first_int = input('Enter the product you want to update: ').capitalize()
        if self.first_int == "Food":
            self.inner_inp = input("""Enter name to update name
                                    Enter quantity to update quantity
                                    Enter price to update price: """).capitalize() 
            if self.inner_inp == "Name":
                self.new_inp = input('Enter the new name: ')
                self.prod[self.first_int][self.inner_inp] = self.new_inp
                print(self.prod)
            elif self.inner_inp == "Quantity":
                self.new_inp = int(input('Enter the new quantity: '))
                self.prod[self.first_int][self.inner_inp] = self.new_inp
                print(self.prod)
            elif self.inner_inp == "Price":
                self.new_inp = int(input('Enter the new price: '))
                self.prod[self.first_int][self.inner_inp] = self.new_inp
                print(self.prod)
            else:
                print('Invalid Input')
        
        elif self.first_int == "Drinks":
            self.inner_inp = input("""Enter name to update name
                                      Enter quantity to update quantity
                                      Enter price to update price: """).capitalize() 
            if self.inner_inp == "Name":
                self.new_inp = input('Enter the new name: ')
                self.prod[self.first_int][self.inner_inp] = self.new_inp
                print(self.prod)
            elif self.inner_inp == "Quantity":
                self.new_inp = int(input('Enter the new quantity: '))
                self.prod[self.first_int][self.inner_inp] = self.new_inp
                print(self.prod)
            elif self.inner_inp == "Price":
                self.new_inp = int(input('Enter the new price: '))
                self.prod[self.first_int][self.inner_inp] = self.new_inp
                print(self.prod)
            else:
                print('Invalid Input')

        elif self.first_int == "Beverage":
            self.inner_inp = input("""Enter name to update name
                                    Enter quantity to update quantity
                                    Enter price to update price: """).capitalize() 
            if self.inner_inp == "Name":
                self.new_inp = input('Enter the new name: ')
                self.prod[self.first_int][self.inner_inp] = self.new_inp
                print(self.prod)
            elif self.inner_inp == "Quantity":
                self.new_inp = int(input('Enter the new quantity: '))
                self.prod[self.first_int][self.inner_inp] = self.new_inp
                print(self.prod)
            elif self.inner_inp == "Price":
                self.new_inp = int(input('Enter the new price: '))
                self.prod[self.first_int][self.inner_inp] = self.new_inp
                print(self.prod)
            else:
                print('Invalid Input')

        else:
            print('Invalid Input')
        self.tryagain()


    # delete
    def delete_prod(self):
        self.anot_in = input('Enter the product you want to delete: ').capitalize()
        if self.anot_in == "Food":
            print(self.drinks_prod, self.bev_prod)
        elif self.anot_in == "Drinks":
            print(self.food_prod, self.bev_prod)
        elif self.anot_in == "Beverage":
            print(self.food_prod, self.drinks_prod)
        else:
            print('Invalid Input')
        self.tryagain()



    # tryagain
    def tryagain(self):
        self.inputss = input("Enter Yes to try again or No to stop: ").capitalize()
        if self.inputss == "Yes":
            self.alls()
        elif self.inputss == "No":
            quit()
        else:
            print('Invalid Input')
        

sims()










