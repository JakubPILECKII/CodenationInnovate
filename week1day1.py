



greeting = "Hello World"

print (greeting)

print(len(greeting))

print (greeting[1])

print (greeting.upper())


def function_one(name):
   return f"Hello {name}!" 

print(function_one("John"))


print()
player_list = [
    "Stefan",
    "Jurek",
    "Krzysiek"
]
for player in player_list:
    print(player)

print()



class user():
    def __init__(self, name, age, email):
        self.name = name,
        self.age = age,
        self.email = email

print(user)



print()
print (int(5.4))
print (int("54"))


#######################?   R O U N D     N U M B ER    U P   #####################

print (int(round(5.8)))

print()


#########################?   P R I N T   F L O A T  N U M B E R   #####################

print (float(54))
print (float("54"))

print()


####################? T U R N    I T    I N   T O     S T R I N G   ########################

print (str(54))
print (str(54.0))

print()


##########################?     T R U E      A N D   F A L S E     #########################


v_1 = "Student"


if v_1 == "Student":
    print(f"Yes it is a {v_1}")
else:
    print("Its not a student")

print()

print("What is your name?")
name = input()
##############? IF THERE WILL BE ANYTHING INSIDE INPUT IT WILL BE TRUE STATMENT ##########
##############? IF INPUT ITS EMPTY IT WILL BE FLASE STATMENT #############################
if name:
    print(f"Hello {name} how are you?")
    print()
else:
    print("I didnt recive any name.")
    print()


    

##########################?   N  O  T     O  P  E  R  A  T  O  R   ###################

card_list = [
        "Jack", "Queen", "King", "Ace"
    ]

if "Ace" not in card_list:
    print("The Ace is missing")
elif "2" not in card_list and "3" not in card_list:
    print("List has possitive equality")


################### ? "!=" means  "not equal"   
###################?  "not in" checks is it in something else    ####################
if "ten" != card_list:
    print("Ten is missing")



###############################?  T R Y  /  E X C E P T  ###############################


def add_up():
    num1 = input("what is the first number you'd like to add up? \n")
    num2 = input("What is the second number you'd like to add up? \n")

    try: ########? THE PROGRAM WILL RUN IF THIS ACTION CAN BE EXECUTED. 
        #########? ITS GOOD WAY TO CHECK IS YOUR CODE WORK CORRECTLY. 
        print(f"{num1} + {num2} is {(int(num1) + int(num2))}!") 

    except: ######## IN CASE IF IT CANNOT RUN IT WILL EXECUTE THIS CODE>
        print("\n ERROR: please input only numerical values. \n") 
        print("********************************************** \n") 
        add_up()
add_up() 

