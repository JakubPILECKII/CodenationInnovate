

from random import random


class Person():
    def __init__(self):
        #? THE CONSTRUCTOR METHOD 
        self.name = None
        self.age = None
        self.profession = None
        self.hobbies = []

    def set_hair(self, person_hair):
        self.hair =  person_hair
    
 



new_person = Person()
new_person.age = 31
new_person.name ="Stefan"

new_person2 = Person(

)
new_person2.age =28
new_person2.name ="Will"

#? print(new_person.age)
#? print(new_person.name)

#? print(new_person2.name)


#? New() - #?  THIS IS CLASS - STARTS WITH CAPITAL LETTER




class MPerson():
    def __init__(self, mperson_name, mperson_age, mperson_profession):
        #? THE CONSTRUCTOR METHOD 
        self.name = mperson_name
        self.age = mperson_age
        self.profession = mperson_profession
        self.hobbies = []
        #? WE SET 

    def set_hair(self, person_hair):
        self.hair =  person_hair
    def get_hair(self):
        print(self.hair) 
    def set_hobby(self, person_hobby):
        self.hobbies.append(person_hobby)
    def get_hobby(self):
        for hobby in self.hobbies:
            print(hobby)       



#? print("=========================================")
#? print("Person")
#? random_person = MPerson("Micheal", 30, "Musician", "Skydiving")
#?print(random_person.name)
#? print(random_person.age)
#? print()
#? print("Person2")
#? random_person2 = MPerson ("Rysiek", 25, "instructor", "Movies")
#? print(random_person2.name)
#? print(random_person2.age)
#? print()




#? print(random_person)

