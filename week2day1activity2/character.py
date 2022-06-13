from tkinter import E
from unicodedata import name


class Character():
    def __init__(self, real_name, superhero_name, power):
        #? inisialise the constructor moethod
        self.real_name = real_name
        self.superhero_name = superhero_name
        self.power = power



    def set_power(self, power):
        self.power =  power
        #? have a setter method for power
        
    def get_power(self):
        print(self.power)
        #? have a getter method for the power        

    def set_items(self, items):
        self.set_items =  items
        #? have a setter method for power
        
    def get_items(self):
        print(self.set_items)
        #? have a getter method for the power        


    def set_superhero_name(self, superhero_name):
        self.superhero_name = superhero_name
    def get_superhero_name(self):
        print(self.superhero_name) 

    def set_name(self, real_name):
        self.real_name = real_name
    def get_name(self):
        print(self.real_name)

    def set_items(self, items):
        self.items = items
    def get_items(self):
        print(self.real_name)

    pass







