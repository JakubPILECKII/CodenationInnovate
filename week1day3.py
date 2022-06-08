
##############################? D I C T I O N A R Y S #####################################


##########################? DICTIONARY USES  " { "   " } " ################################
##########################? "NAME" = KEY , "BATMAN" = VALUE  ############################## 


cat1 = {"name" : "Batman",
        "colour" : "Grey",
        "mood" : "Playfull"}


##########################? DATA ON LEFT SIDE OF CODE ITS "KEY" ############################
#####################? DATA ON THE RIGHT SIDE OF CODE ITS "VALUE"###########################
dict_of_players = {
        1:"Will", 2:"Jay", 3:"Jakub", 
}

###########################? C H E C K   D A T A  ########################################## 
print()
print(cat1["name"])
print(cat1)
print(cat1["colour"])
print()
print(cat1["name"], ["Mood"])

name=cat1["name"]

print()
print(f"My cat is called {name}")
print()
print("My cat is " + cat1["mood"], "and it " + cat1["colour"] + " colour ")
print()

#################?   PRINT KEY WORDS 
for z in cat1.keys():
        print(z)
print()
#################? P R I N T   V A L U E S 
for y in cat1.values():
        print(y)
print()
#########################? P R I N T   A L L    I N F O  ################################# 
for x in cat1.items():
        print(x)
print()


#########################? U P D A T I N G   V A L U E S   O F    K E Y S  ###############

cat1["name"] = "Superman"
print(cat1["name"])


########################? M O R E   C O M P L E X   D I C T I O N A R Y

complex_dict = {

        "one": 
        {"nick": "Will",
        "age" : 33,
        "instrucor": True},

        "two" : 
        { "nick": "Jay",
        "age": 30,
        "instructor": True},

        "three": 
        { "nick": "Jakub",
        "age": 33,
        "instructor": False},
}

print(complex_dict)
print()
print(complex_dict["two"]["instructor"]) ########? PRINTING PRETICILUAR VALUE   
###########?"IN THIS CASE IT IS BULIANT VALUE - "INSTRCTOR" FOR KEY "TWO" 


print("""
############################ A C T I V I T Y  1 ###################################""")

###########? MAKE DICTIONARY FOR PETS ###########
pets_dict = {
        "one": 
        {"nick": "Billy",
        "colour" : "Black",
        "species": "Cat"},

        "two" : 
        {"nick": "Morphy",
        "colour": "Grey",
        "species": "Rabbit"},

        "three": 
        {"nick": "Lazer",
        "colour": "Green",
        "species": "Turtle"},

        "four":
        {"nick": "Smiler",
        "colour": "Brown",
        "species": "Dog"}
}

print()
print(pets_dict["one"]["colour"]) ####? - PRINTS WHAT COLOUR IS PET NR 1
print()
print("Updated colour")



################################? UPDATE INFORMATION INSIDE THE CODE
pets_dict["one"]["colour"] = "Black with white dots"
print()
print("Print info about Animal nr '4' - Colour and Species")
print(pets_dict["four"]["colour"], pets_dict["four"]["species"])
print()
print("Print all info about animal nr 1 and see if colour got updated")
print(pets_dict["one"])
print()
print(list(pets_dict))

print("Print all keys from pets_dict")
print(list(pets_dict.keys()))
print()
print("Print all values from pets_dict")
print(list(pets_dict.values()))
print()
print()


##############################?  LOOP THRUE YOUR DICTIONARY
print("LOOP THROUGH DICTIONARY: "
)
for x1 in pets_dict.keys():
    print(x1)

print()

for x1 in pets_dict.values():
    print(x1)

print()

for x1 in pets_dict.items():
    print(x1)

print()
print()


#######################? SET A DEFAULT VALUE FOR KEYS 
pets_dict["one"].setdefault("hungry", True) ####? SET ONE VALUE FOR PRETICILUAR KEY

for x in pets_dict:
    pets_dict[x].setdefault("mood", "sleepy")


print(x1)
print()


#######################?  DELETE A VALUE FOR KEYS
pets_dict["one"].pop("hungry") ######? delete value "hungry" from KEY "one" 
pets_dict["one"].pop("species")
popped_entry = pets_dict

print(pets_dict)

print()

for x in pets_dict:
    pets_dict[x].pop("mood") #########? delete all of the values "mood" from all keywords.

print(x1)



####################################? A C T I V I T Y      2 ###############################
print("############################# A C T I V I T Y      2 ################################")



countries ={
        "UK":{"Capital":"London", "Location":"Nort-West Europe"},
        "France":{"Capital":"Paris", "Location":"West Europe"},
        "Germany":{"Capital":"Berlin", "Location":"Central-West Europe"},
        "Spain":{"Capital":"Madrid", "Location":"South-West Europe"},
        "Italy":{"Capital":"Rome", "Location":"South Europe"}

}
print()
print(countries)
print()
for c1 in countries.items():
    print(c1)

print()
print("Add 2 more countries")
countries.setdefault("Poland",{"Capital":"Warsaw", "Location":"Central Europe"})
countries.setdefault("Brasil",{"Capital":"Brasilia", "Location":"South America"})
#("Capital","Warsaw", "Location","Central Europe")
print(countries)
print()
print("'Capital'-'KEY' check for new country")
print(countries["Brasil"]["Capital"])
print()



print("Capitals was deleted")
for no_capital in countries:
    countries[no_capital].pop("Capital")
print(countries)
print()




print("Language value was add to all keys.")
for add_lang in countries:
    countries[add_lang].setdefault("Language")
print(countries)
print()


print("Language values was filled with data.")
countries["UK"]["Language"] = "English"
countries["France"]["Language"] = "French"
countries["Germany"]["Language"] = "German"
countries["Spain"]["Language"] = "Spanish"
countries["Italy"]["Language"] = "Italian"
countries["Poland"]["Language"] = "Polish"
countries["Brasil"]["Language"] = "Portugese"
print(countries)
print()
for c1 in countries.items():
    print(c1)


print()
print()
print("######################## A C T I V I T Y   3  ########################")
print()
songs=[
    {"artist":"APOLLO 440", "song_name":"Aint Talkin' 'Bout Dub", "genre":"EDM", "release_year":"1997"}, 
    {"artist":"DJ INFINITY", "song_name":"Children of the 80's", "genre":"EDM", "release_year":"2001"}, 
    {"artist":"JACK BACK", "song_name":"FEELING", "genre":"HOUSE", "release_year":"2022"}, 
    {"artist":"DJ MIKE B", "song_name":"Feel My Energy", "genre":"FLORIDA BREAKS", "release_year":"1997"}, 
    {"artist":"BASS PATROL", "song_name":"Do The Alph", "genre":"ELECTRO", "release_year":"1988"}, 
]
print()
print(""" Playlist: """)
for song in songs:
        print(song)

print("""
""")
print(f"""Song that get replace: 
{songs[1]}
""")


songs[1]={"artist":"BOB SINCLAR", "song_name":"Love Generation", "gemre":"HOUSE", "release_year":"2005"}
print(f"""New song on playlist:
{songs[1]}
""")

print("Edited Playlist:")
for song in songs:
        print(song)

