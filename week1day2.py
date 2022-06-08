
from bdb import Breakpoint
from doctest import script_from_examples
from tracemalloc import start

############################? W E E K  1   D A Y  2   ####################################
print()
welcome = "Welcome to Codenation"

lenght_w = (len(welcome))


if (lenght_w % 2) == 0:
    print(f'"{welcome}" is {lenght_w} characters long, and {lenght_w} is an even number.')

else:
    print(f'"{welcome}" is {lenght_w} characters long, and {lenght_w} its an odd numeber')

print()



##############################?   A  C  T  I  V  T  Y     1    D A Y 2  #################################
print("Activity 1 - ALphabet / LIST LOOP")
alphabet = [
    "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j", 
    "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y",
    "z"
]

def list_loop(l1):
    for number in l1:
        print(number)

def chosen(l1):
    user_choice = int(input("Type number 0-26 to check what letter that corespond to in Alphabet :  "))
    print(f'"{l1[user_choice -1]}" is under possition {user_choice} in aplhabet')

list_loop(alphabet)
chosen(alphabet)
print("""
""")


###################################################?


def show_num():
    num=13
    print(num)

num = 10

show_num()


########################################################? 


light = False

def light_switch():
    global light ########? GLOBAL - IMPORTS FUNCTION(line13) VALUE TO THE FUNCTION AND ALOWS IT TO CHANGE IT.
    ######? GENERALY YOU SHOULDNT DECLARE VIAREBLE IN 'GLOBAl" CODE 
    ######?  YOU SHOULD ALWAYS TRY TO DECLARE IT INSIDE FUNCTION/
    if light:
        print("Whoa! Its Bright in here!")
        light = False
    else:
        print("Who turned out the light ?!")
        light = True

light_switch()


########################################################? 


print()
print()
my_list = [
    1,2,3,4,5,6,7,8,9
]


print (f"My list: {my_list}")
print()
print ("print (my_list [0:5])")
print (my_list[0:5])
print ("print (my_list[2:-2])")
print (my_list[2:-2])
print ("print (my_list[3:6])")
print (my_list[3:6])

print()
print()


########################################################?

loop_runs = True

while loop_runs:
    print("Hi")
    print(loop_runs)
    break

def function_for_loop():
    loop_runs2 = True
    while loop_runs2 == True:
        print(loop_runs2)
        break ##########? "BREAK"  STOPS FUCTION FROM RUNNING.



def admin_check():
    name = "Admin"
    while admin_check:
        if name != "Admin":     #####? IF NAME DOESNT EQUAL "ADMIN"
            print(f"Hello {name} you dont have permission to be here")
            break
        else:
            print(f"Hello {name}")
            break


admin_check()
print()
print()

############################? A C T I V I T Y - 2   D A Y  2  #########################


def day2_prog():
    print("Prog - 1")
    some_number = 0
    some_number = input("Please put some number... ")
    try:
        some_number = int(some_number)
        if some_number % 1 == 0:
            print (some_number)
    except:
        print("Please try again, you need to put a number in numeric value.")
        day2_prog()

day2_prog()




############################? A C T I V I T Y - 3   D A Y  2  #########################



def day2_prog2():
    print()
    
    print("Prog 2")
    def members():
        cast_members = ["Bill Murray", "Dan Aykroyd", "Harold Ramis", "Sigourney Weaver",
                        "Ernie Hudson", "Annie Potts", "Rick Moranis"
        ]
        print(f"""                     Ghost Busters(1984)   CAST MEMBERS : 
{cast_members}""")

    def game():
        answer=input("Whats the name of friendly green ghost from Ghost Busters Movie? ").upper()
        while answer !="SLIMER":
            print("You didnt get that right this time, Please try again!")
            game()
        else:
            print("Your are right! Con gratulation!")
            


    def start():
        start1 =input("Please chose betwen (1)Quiz Game, (2)Check cast members, (3)Exit (Type numeric velue.) ")
        if start1=="1":
            print("Ok Lets start the game!")
            print()
            game()
        elif start1=="2":
            print()
            members()
            print()
            
            
            start()
        elif start1=="3":
            exit
        else:
            print("Please try again, Try to put numeric value : 1, 2 or 3.")
            start1=""
            start()
            

    start()

day2_prog2()

