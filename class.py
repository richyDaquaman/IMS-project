# Python class
# A Python class is a blueprint for creating objects
# Objects are instances of classes that encapsulate data (attributes) and behavior (methods).
# Classes allow for structuring data and functionality in an organized and reusable way.
# In this case, we can compare a cake recipe to a class, and a cake cooked following that recipe to an object (i.e., an instance of that class).
#  Using the same recipe (class), we can create many cakes (objects). 
# Classes are defined using the class keyword:



# Key points:
# Constructor (__init__): Method to initialize object attributes.
# Attributes: Variables that store the object’s state.
# Methods: Functions that define the object’s behavior.
# Inheritance: Reusing code by inheriting methods/attributes from a parent class.
# Parent Class: The class from which another class inherits (also called a superclass).
# Child Class: The class that inherits from another class (also called a subclass).
# super(): A method that allows the child class to call methods or attributes of the parent class.


# To define a Python class, use the class keyword followed by the name of the new class and the colon. Let's create a very simple empty class:
# e.g


# class className:
#     pass
# example
# class testClass:
#     firstname = "Adeyemi"
#     lastname = "Alao"
#     course = "python"
# #     # create an instance of the class
# test = testClass()
# test_2 = testClass()
# print(f'My name is {test.firstname} {test.lastname} with course code {test.course}')
# print(f'My name is {test_2.firstname} {test_2.lastname} with course code {test_2.course}')




# working with constructor
# class firstClass:

#     def __init__(self,  firstname, lastname, level, x, y):
#         # attribute or data
#         self.firstname = firstname
#         self.lastname = lastname
#         self.level = level
#         self.location = "Challenge"
#         self.x = x
#         self.y = y
#         # self.display()



#     # METHOD
#     def calc(self):
#         return self.x + self.y
    
#     def display(self):
#         print(f'My name is {self.firstname} {self.lastname}, i"m from {self.location} and my total score is {self.calc()}')
              
# # # # # Creating instances of the test class
# std_one  = firstClass('lola', 'ojo', 100, 30, 40)
# std_2  = firstClass('john', 'doe', 200, 50, 40)
# std_3 = firstClass('jide', 'ola', 'PD', 20, 10)

# # std_one.display()
# # std_2.display()
# # std_3.display()

# print(std_2.calc())

# # print(std_one.calc())
# std_one.display()
# std_two.display()
# std_3.display()

# firstClass("Yemi", "Ojo", "500", 10, 6)


# class cbt:

#     def __init__(self):
#         self.username = input('Enter username: ')
#         self.password = input('Enter password: ')
#         self.score = 0
#         self.login()




#     # 1 
#     def login(self):
#         if self.username == "admin" and self.password == "1234":
#             print('Welcome')
#             self.test()
#             if self.test:
#                 print(self.cong())
#         else:
#             print('Incorrect username or password')

#     # test

#     def test(self):

#         ans = ['a', 'c', 'b']
#         q1 = input("""
#                         1. who is the pres of Nig
#                         a. Tinubu
#                         b. Buhari
#                         c. Jona""")
        
#         if q1 == ans[0]:
#             self.score += 10
#             print(self.score)
#             self.tryagain()
#         else:
#             self.score
#             print(self.score)
#             self.tryagain()

#     def cong(self):
#         if self.score >= 10:
#             return "Congrats"
#         else:
#             return "Try again"
            
        
#     def tryagain(self):
#         tryy = input('Enter yes to try again: ')

#         if tryy == 'yes':
#             self.test()
#         else:
#             quit()
        

# # run = cbt()
# # run.login()

# cbt()


# class calculator:

#     def __init__(self):
#         self.username = input('Enter username: ')
#         self.passw = input('Enter password: ')
#         self.login()



#     def login(self):
#         if self.username == 'admin' and self.passw == '1234':
#             print('welcome')
#             self.calc()
#         else:
#             print('Wrong username or password')
#             self.new()
    
#     def calc(self):
#         self.x = int(input('Enter val1: '))
#         self.y = int(input('Enter val2: '))
#         self.oper = input('enter operation: ')

#         if self.oper == "+" or self.oper == 'add':
#             print(self.x + self.y)

#     def new(self):
#         print('Forgot password')

# calculator()











# class testClass:
    
# #     # constructor
#     def __init__(self, firstname, lastname, level, x, y):
#         self.firstname = firstname  #Attribute to store the firstname name
#         self.lastname = lastname  #Attribute to store the lastname
#         self.level = level   #Attribute to store the level
#         self.x = x
#         self.y = y

# # method to display the studentinfo
#     def display_func(self):
#         print(f'My name is {self.firstname}  {self.lastname}, my level is {self.level} and my score is {self.score()}')

#     def score(self):
#         z = self.x + self.y
#         return z
# # # # Creating instances of the test class
# test = testClass("Adeyemi", "Oluwaseyi", "4", 10, 6)
# # test1 = testClass("bUKOLA", "SHARAKI", "67", 50, 90)
# # test1  = testClass("king", "victor", "5", 10, 10)
# # test2 = testClass("Grace", "Odogwu", "14", 50, 50)
# # test.display_func()
# # test1.display_func()
# # test2.display_func()

# # test.score()

# print(test.score())



# class secondClass:

#     def __init__(self, age, gender, course, score, name):

#         # attribute
#         self.age = age
#         self.gender = gender
#         self.course = course
#         self.score = score
#         self.name = name

    
#     # method
#     def average(self):
#         return self.score / 2
    
        
#     def final(self):
#         # self.name = "Kola"
#         print(f'My name is {self.name}, i"m {self.age} yrs old. I"m {self.gender} and my best subject is {self.course} and average score is {self.average()}')

# # std_one = secondClass(30, "male", "data science", 50)
# # std_one.final()
# n = secondClass(30, "male", "data science", 50, 'jide')
# v = secondClass(20, "female", "ai", 10, 'john')

# n.final()
# v.final()















# class student_name():
#   name = "Timi"
#   location = "ibadan"
#   def walk(self):
#     name = "Ade"
#     print(name + " is walking")
#   def talk(self):
#     print("i am talking")
# rn = student_name()

# rn.talk()
# rn.walk()

# impo







# # Features:

# # Add product (name, quantity, price)

# # View all products

# # Update product quantity

# # Delete product


# class productmanagt:

#     def __init__(self):
#         self.prod1 = {"name":"food", "quantity":4, "price":3000}
#         self.prod2 = {"name":"drinks", "quantity":10, "price":1200}
#         self.prod3 = {}
#         self.prod = {
#             "food":self.prod1,
#             "drinks":self.prod2
#         }

#         self.mainpage()



#     # main
#     def mainpage(self):
#         self.f = input('Enter 1 to add product\nEnter 2 to view\nEnter 3 to update\nEnter 4 to delete\nEnter 5 to quit: ')
#         if self.f == "1":
#             self.addprod()
#         elif self.f == "2":
#             self.viewp()
#         elif self.f == "3":
#             self.updateprod()
#         elif self.f == "4":
#             self.delprod()
#         elif self.f == "5":
#             quit()
#         else:
#             print('invalid Input')

#     # add
#     def addprod(self):
#         self.name = input('Enter product name: ')
#         self.quant = int(input('Enter prod quant: '))
#         self.price = int(input('Enter prod price: '))
#         self.prod3[self.name] = {"name":self.name, "quantity":self.quant, "price":self.price}
#         self.prod.update(self.prod3)
#         for i, j in self.prod.items():
#             print(f'{i} : {j}')
    
#     # view
#     def viewp(self):
#         for i, j in self.prod.items():
#             print(f'{i} : {j}')
    
#     # update
#     def updateprod(self):
#         self.oper = input('Enter 1 to update prod name\nEnter 2 to update quant\nEnter 3 to update price')
#         self.old_n = input('Enter old name: ')
#         if self.oper == "1":
#             if self.old_n in self.prod:
#                 self.new_n = input('Enter new name: ')
#                 self.prod[self.old_n].update({"name":self.new_n})
#                 for i in self.prod.values():
#                     print(i['name'], i)
#             else:
#                 print('product not found')
#         elif self.oper == "2":
#             if self.old_n in self.prod:
#                 self.new_n = int(input('Enter new quant: '))
#                 self.prod[self.old_n].update({"quantity":self.new_n})
#                 for i in self.prod.values():
#                     print(i['name'], i)
#             else:
#                 print('product not found')
#         elif self.oper == "3":
#             if self.old_n in self.prod:
#                 self.new_n = int(input('Enter new price: '))
#                 self.prod[self.old_n].update({"price":self.new_n})
#                 for i in self.prod.values():
#                     print(i['name'], i)
#             else:
#                 print('product` not found')

#     # delete
#     def delprod(self):
#         self.rem = input('Enter the product to remove: ')
#         if self.rem in self.prod:
#             del self.prod[self.rem]
#             for i,  j in self.prod.items():
#                     print(f'{i} : {j}')
#         else:
#             print('product` not found')   
        

# productmanagt()
























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
























# Python Inheritance - means acquiring properties
# There are two classes - the base class(parent class) and derived class(child class)
# Through the object of the derived class we can access the properties of both parent and child class
# Types of inheritance
# 1. single inheritance and 
# 2. multi-level inheritance
# single inheritance - one base class and one derived class

# class dad_mom:

#     name = 'yemi'
#     level = 200
#     score = 70.89
#     surname = 'jide'

#     # method 1
#     def prop(self):
#         self.name = 'lola'
#         self.school = 'EBHS'
#         return self.name, self.school
 
# class one_child(dad_mom):


#     location = 'Ojoo'

#     def new(self):
#         final = f'My name is {self.surname} {self.name}, i"m in {self.level} and my total score is {self.score}'
#         return final
    
#     def last(self):
#         print(f'{self.new()}, my location is {self.location}')

# one_c = one_child()
# one_p = dad_mom()

# # one_c.last()

# # print(one_c.name)

# print(one_c.prop())








# class yes:
#     name = "ade"
#     def display(self):
#         print("parent")
      

#     def score(self, x, y):
#         self.x = x
#         self.y = y
#         return self.x + self.y


# class no(yes):
#     def show(self):
#         # print("child")
#         print(f'My name is {c2.name} from department of {c2.final()} and total score is {c2.score(50, 10)}')

#     def final(self):
#         department  = "Data Science"
#         return department
# c2 = no()
# c1 = yes()
# c2.show()
# c1.display()
# print(c2.name)
# print(c2.score(5, 5))
# c2.display()
# print(c2.name)
# print(c2.score(10, 5))
# print(f'My name is {c1.name} from department of {c2.final()} and total score is {c1.score(50, 10)}')
# print(f'My name is {c2.name} from department of {c2.final()} and total score is {c2.score(90, 10)}')

# c2.show()
# print(c2.name)

# grade = int(input('enter grade: '))

# class grad:
#     def __init__(self, level_1, level_2, level_3):

#         self.level_1 = level_1
#         self.level_2 = level_2
#         self.level_3 = level_3
#         self.math = int(input('Enter value for math: '))
#         self.eng = int(input('Enter value for eng: '))
#         self.phy = int(input('Enter value for phy: '))

#         # self.new = self.cumu(self.aver)

#     def cumu(self):

#         self.original = self.phy + self.math + self.eng
#         # print(self.original)
#         return self.original
   

# class gradchild(grad):

#     def result(self):

#         self.aver = (self.cumu()) / 3
#         if  self.aver <= 44:
#             print('Fail')
#             print('Now in level', self.level_1)
#         elif self.aver <= 64:
#             print('Average')
#             print('Now in level', self.level_2)
#         else:
#             print('Excellent')
#             print('Now in level', self.level_3)
# ts = gradchild(1, 2, 3)
# ts.cumu()
# ts.result()
# print(ts.cumu())




# class car:

#     def __init__(self, color):
#         self.model = 'Benz'
#         self.color = color
#         self.interior = input('Enter interior: ')
#         self.engine_type = 'v6_engine'

#     # mehod 1
#     def carprop(self):
#         new = f'The car model is {self.model}, color is {self.color} and the interior is {self.interior} and finally the engine type is {self.engine_type}'
#         return new
    
#     def move(self):
#         print(self.carprop())
#         oper = input('Enter start to start the car: ')
#         if oper == 'start':
#             print('Car engine is on')
#         else:
#             print('Car engine is off')
    
#     def direction(self):
#         self.move()
#         oper = input('Enter d to move forward or r to reverse:  ')
#         if oper == 'd':
#             print('Car is moving forward')
#         elif oper == 'r':
#             print('Car is in reverse mode')
#         else:
#             print('Unknown, engine off')
    

# class nextoption(car):
#     def __init__(self, color, driver):
#         super().__init__(color)
#         self.driver = driver


#     def owner(self):
#         print(f'The owner of the car is {self.driver}')

#     def last(self):
#         self.owner()
#         self.direction()
#         oper = input('Enter b to apply break and park: ')
#         if oper == 'b':
#             print('Car parked')
#         else:
#             print('Low fuel')


# # cc = car('Yellow')
# no = nextoption('Blue', 'Lola')

# # no.last()
# # no.move()
# print(no.color)

    






# 2. Multi-level inheritance - 
# base class === derived class === base class === derived class
# Grandparent == parent == child == grandchild
# grandparent == parent == child

 
# class grandparent:
#   def gdisplay(self):
#     print("grandparent")
# class parent(grandparent):
#   def pdisplay(self):
#     print("parent")
# class child(parent):
#   def cdisplay(self):
#     print("child")
# class grandchild(child):
#   def grdisplay(self):
#     print("grandchild")

# c4 = grandchild()
# c3 = child()
# c2 = parent()
# c1 = grandparent()

# c4.gdisplay()
# c4.cdisplay()
# c2.gdisplay()




# class Father:
#   def __init__(self):
#       self.surname = "Adeowo"
#       self.name = "Owolabi"
#       self.skin_color = "dark skin"
#       self.height = "tall"
#       self.language = "Yoruba"
#       self.wlk = "slowly"
#       self.tlk = "loud"
#       self.slp = "snores"
    


#   def walk(self):
#       print(self.name + " " + self.surname+" is walking "  + self.wlk)
  
#   def talk(self):
#       print(self.name +' from '+self.surname+' talks ' + self.tlk)
  
#   def sleep(self):
#       print(self.name + " " + self.slp +' while sleeping')
    
# class Child(Father):
#     def __init__(self, gender):
#         # Father.__init__(self)
#         super().__init__()
#         self.birth = "2003"
#         self.location = "Ibadan"
#         self.name = "Johnson"
#         self.wlk = "anyhow"
#         self.gender = gender


#     def run(self):
#         print(self.name+ " is running up and down")

#     def gend(self):
#         print(f'my gender is ', self.gender)

 

# class GrandChild(Child):
#     def __init__(self):
#         super().__init__(gender="male")
#         self.name = "Micheal"
#         self.wlk = "fast"
#         self.slp = "talk"

# ft = Father()
# ch = Child("male")
# gd = GrandChild()

# # gd.gend()
# gd.walk()

# # class myClass:

# #   def __init__(self,name,age,color):
# #       self.name = name
# #       self.age = age
# #       self.color = color

# # details = myClass('ade',24,'light')
# # print(f'my name is {details.name}, am {details.age} years old and am {details.color} in complexion')


# # # Base class (Parent class)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def shows_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")

# # Derived class (Child class)
# class Student(Person):
#     def __init__(self, name, age, school, post_utme_score):
#         # Call the parent class's constructor
#         super().__init__(name, age)
#         self.school = school
#         self.post_utme_score = post_utme_score
    
#     # Method to check if the student passed the Post-UTME
#     def check_post_utme_result(self):
#         passing_score = 50  # Let's assume the passing score is 50
#         if self.post_utme_score >= passing_score:
#             print(f"Congratulations {self.name}, you passed the Post-UTME with a score of {self.post_utme_score}!")
#         else:
#             print(f"Sorry {self.name}, you did not pass the Post-UTME. Your score is {self.post_utme_score}.")
    
#     # Overriding the parent class method to show additional information
#     def show_info(self):
#         super().shows_info()  # Call parent method to show name and age
#         print(f"School: {self.school}")
#         print(f"Post-UTME Score: {self.post_utme_score}")

# # # Taking user input to create a Student object
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# school = input("Enter your school name: ")
# post_utme_score = int(input("Enter your Post-UTME score: "))

# # Creating an object of the Student class using the input data
# student = Student(name, age, school, post_utme_score)

# # Display the student's information
# student.show_info()

# # # Check if the student passed the Post-UTME
# student.check_post_utme_result()

# from cbt import CBT 



# user = input('enter username: ')
# passw = int(input('enter password: '))
# class studentExam:

#     def __init__(self, name):

#         self.name = name
#         self.login()



#     def login(self):
#         self.username = ["seyi", "bola", "bunmi"]
#         self.password = [1234, 5678, 9012]
        

        


#         self.found = False

#         for i in range(len(self.username)):
#             if self.username[i] == user and self.password[i] == passw:
#                 print('login')
#                 self.found = True
#                 self.result()
#                 break

#             else:
#                 CBT.wrong_pass()
#                 self.found = False
#                 break


#     def result(self):
#         # print('welcome')
#         CBT.first_input()


# studentExam(user)



# class Bus:
#     def __init__(self, bus_number, total_seats):
#         self.bus_number = bus_number
#         self.total_seats = total_seats
#         self.booked_seats = 0

#     def book_seat(self, seats):
#         if self.booked_seats + seats <= self.total_seats:
#             self.booked_seats += seats
#             print(f"{seats} seat(s) booked successfully!")
#         else:
#             print("Not enough seats available.")

#     def available_seats(self):
#         return self.total_seats - self.booked_seats

#     def status(self):
#         print(f"Bus {self.bus_number}: {self.booked_seats} booked, {self.available_seats()} available.")
# # Create a bus with 40 seats
# my_bus = Bus("B123", 40)

# # Book seats
# my_bus.book_seat(5)
# my_bus.book_seat(10)

# # Show status
# my_bus.status()

# Try booking too many seats
# my_bus.book_seat(30)

# Final status
# my_bus.status()


# class Bus:
#     def __init__(self, bus_number):
#         self.bus_number = bus_number
#         self.total_seats = 30
#         self.booked_seats = 0

#     def book_seat(self, seats):
#         if self.booked_seats + seats <= self.total_seats:
#             self.booked_seats += seats
#             print(f"{seats} seat(s) booked successfully!")
#         else:
#             print("Not enough seats available.")

#     def available_seats(self):
#         return self.total_seats - self.booked_seats

#     def status(self):
#         print(f"Bus {self.bus_number}: {self.booked_seats} booked, {self.available_seats()} available.")
# # Create a bus with 40 seats

# seat_s = int(input('Enter seat: '))
# # tseat_s = int(input('Enter total seat: '))
# my_bus = Bus("B123")

# # Book seats
# my_bus.book_seat(seat_s)
# my_bus.book_seat(seat_s)
# my_bus.book_seat(seat_s)


# # Show status
# my_bus.status()


# class Animal:
#     def __init__(self):
#         self.name = 'Jack'
#         self.breed = 'German'
    
#     def eat(self):
#         return "Eating..."

# class Dog(Animal):
#     def __init__(self):
#         super().__init__()
#         # self.breed = breed
    
#     def bark(self):
#         return "Woof!"
    

# class smallDog(Dog):
#     def __init__(self):
#         super().__init__()
#         self.color = "blue"
#         self.name = 'chukky'
#         # self.breed = "German Shep"


#     def prop(self):
#         print(f'The name of the dogg is {self.name} and it has {self.color} and is {self.breed}, {self.bark()}')


# sm = smallDog()
# print(sm.bark())
# print(sm.eat())
# sm.prop()
# sm.Animal()
# print(sm.eat())
# print(sm.bark())



# class USD:
#     def __init__(self, ussd):
#         self.ussd = ussd
#         self.check()
    
#     def check(self):
#         self.user_inp = input('Enter ussd: ')
#         if self.user_inp == self.ussd:
#             self.firststage()
#         else:
#             self.check()
        

#     def firststage(self):
#         print("""
#                 1. Buy Data Plan
#                 2. Buy Airtime
#                 3. Borrow Airtime
#                 4. Check Balance
#                 5. Exit""")

#         self.user_inp = input('Enter operation: ')
#         if self.user_inp == "1":
#             self.secondstage_1()
#         elif self.user_inp == "2":
#             self.secondstage_2()
#         elif self.user_inp == "3":
#             self.secondstage_3()
#         elif self.user_inp == "4":
#             self.secondstage_4()
#         elif self.user_inp == "5":
#             quit()
#         else:
#             print('Unknown Input')
        
#     def secondstage_1(self):
#         print("""
#                     1. #500 for 1GB
#                     2. #1000 for 70GB
#                     3. Go to Menu""")
#     def secondstage_2(self):
#         print("""
#                     1. #500
#                     2. #1000
#                     3. Go to Menu""")
#     def secondstage_3(self):
#         print("""
#                     1. #500
#                     2. #1000
#                     3. Go to Menu""")
#     def secondstage_4(self):
#         print(""" #50000""")

# USD('*312#')


# acces to exam(promotion)
# check score
# view detail
# delete

# from cbt import firstexam
# import time


# class examproj:

#     def __init__(self):
#         self.score  = 0
        
#         self.mainpage()
   

 
 



# class subexam(examproj):

#     def __init__(self):
#         super().__init__()

#     def login(self):
#         self.username = input("Enter username: ")
#         self.password = input('Enter password: ')

#         if self.username == self.student_1["username"] and self.password == self.student_1["password"]:
#             time.sleep(2)
#         else:
#             print('Invalid Details')
#             self.login()
    




# class ext_sub_exam(subexam):

#     def __init__(self):
#         super().__init__()

#     def check_score(self):
#         self.new = input('Enter the username to check score: ')

#         if self.new == self.student_1["username"]:
#             print("Score: ", self.student_1["score"])
#         else:
#             print('Invalid Details')


#     def details(self):
#         self.new = input('Enter the username to view your detail: ')

#         if self.new == self.student_1["username"]:
#             print("Score: ", self.student_1)
#         else:
#             print('Invalid Details')

#     def delete(self):
#         self.new = input('Enter the username to delete: ')

#         if self.new == self.student_1["username"]:
#             print("Score: ", self.student_1)
#         else:
#             print('Invalid Details')


#     # def new(self):
#         # self.name = input('Enter student name: ')
#         # self.level = int(input('Enter student level: '))
#         # self.department = input('Enter student dept: ')
#         # # score = int(input('Enter student score: '))
#         # self.username = input('Enter student username: ')
#         # self.password = input('Enter student password: ')

#     def register(self):
#         self.login()
#         if self.login:
#             firstexam.first_input(self)
#             if firstexam.first_input:
#                 self.student_1 = {"fullname": self.name, "level":self.level, "department":self.department, "score":firstexam.show_score(self), 
#                     "username":self.username, "password": self.password}
#                 print(self.student_1)
                
#         else:
#             print('No')
        

#     def mainpage(self):
        
#         oper = input('Enter 1 to Register/login\nEnter 2 to View\nEnter 3 to check score\nEnter 4 to delete\nEnter 5 to quit: ')
        
#         if oper == "1":
#             self.name = input('Enter student name: ')
#             self.level = int(input('Enter student level: '))
#             self.department = input('Enter student dept: ')
#             # score = int(input('Enter student score: '))
#             self.username = input('Enter student username: ')
#             self.password = input('Enter student password: ')
#             self.student_1 = {"fullname":self.name, "level":self.level, "department":self.department, "score":self.score, 
#             "username":self.username, "password": self.password}
#             self.register()
#         elif oper == "2":
#             self.details()
#         elif oper == "3":
#             self.check_score()
#         elif oper == "4":
#             self.delete()
#         elif oper == "5":
#             quit()
#         else:
#             print('Invalid Input')



    

# ext_sub_exam()