from character import Character
#? need to import your class from the other file
batman = Character(
    "Bruce Banner",
    "Fatman",
    "Super Strenght")


spider_man = Character(
    "Peter Walker",
    "Spider-Van",
    "Rap Spider Verse",

)

#? instantiate your object from hero class

batman.set_name("Bruce Wayne")
batman.set_superhero_name("BATMAN")
batman.set_power("None")
spider_man.set_name("Peter Parker")
spider_man.set_superhero_name("SPIDER-MAN")
spider_man.set_power("Spider Sense")
#? HAVE A SETTER RUN


print()
batman.get_name()
batman.get_superhero_name()
batman.get_power()
print()
spider_man.get_name()
spider_man.get_superhero_name()
spider_man.get_power()
#? HAVE A GETTER RUN


