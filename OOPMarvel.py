# Marvel characters, object oriented programming.
# Class and Inheritance application
# Marvel characters - Features application
# written by Spyder IDE.
""" @author: saaydmr """
#%% Base class
class Marvel():
    characters = []
    age_avg = 0
    
    def __init__(self, gender, age, power, name, surname, experience, herotag):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age 
        self.experience = experience
        self.power = power
        self.herotag = herotag
        
    def add_character(self):
        Marvel.characters.append(self)
        print("\n", self.name, self.surname, self.herotag, " saved to list..")
        
    def character_listing(self):
        print("\n\nName\t Surname\t Gender\t Age\t Exp\t Power\t Herotag")
        for m in Marvel.characters:
            if(type(m) == Marvel):
                print("""{}\t {}\t {}\t {}\t {}\t {}\t {}\t""".format(m.name, m.surname, m.gender, m.age, m.experience, m.power, m.herotag))
                
    def all_character_listing(self):
        print("\n\nName\t Surname\t Gender\t Age\t Exp\t Power\t Herotag")
        for c in Marvel.characters:
               print("""{}\t {}\t {}\t {}\t {}\t {}\t {}\t""".format(c.name, c.surname, c.gender, c.age, c.experience, c.power, c.herotag))
               
    def age_average(self):
        avg = 0
        counter = 0
        for m in Marvel.characters:
            if(type(m) == Marvel):
                counter += 1
                avg += m.age
        Marvel.ageavg =  avg/counter
        print("Marvel's age average is  : ", Marvel.ageavg )
        
    def all_age_average(self):
        avg = 0
        for m in Marvel.characters:
            avg += m.age
        Marvel.age_avg = avg/len(Marvel.characters)
        print("All marvel characters age average:", Marvel.age_avg)
            
                
                
#%% Inheritance class
                
class Avengers(Marvel):
    def __init__(self, gender, age, power, name, surname, experience, herotag):
        super().__init__(gender, age, power, name, surname, experience, herotag)
        
        
        
        
    def character_listing(self):
        print("\n\nName\t Surname\t Gender\t Age\t Exp\t Power\t Herotag\t")
        for m in Marvel.characters:
            if(type(m) == Avengers):
                print("""{}\t {}\t {}\t {}\t {}\t {}\t {}\t""".format(m.name, m.surname, m.gender, m.age, m.experience, m.power, m.herotag))
    

        
    def age_average(self):
        avg = 0
        counter = 0
        for m in Marvel.characters:
            if(type(m) == Avengers):
                counter += 1
                avg += m.age
        Marvel.ageavg =  avg/counter
        print("Avenger's age average is  : ", Marvel.ageavg )
        
#%% character insertion section
character0 = Marvel("Woman", 29, 95, "Carol", "Danvers", 88, "CAPTAIN MARVEL")
character0.add_character()
character1 = Marvel("\t Man", 70, 86, "Nick", "Fury", 100, "S.H.I.E.L.D LEADER")
character1.add_character()
character2 = Avengers("\t Man", 101, 100, "Steve", "Rogers", 100, "CAPTAIN AMERICA")
character2.add_character()
character3 = Avengers("Woman", 35, 100, "Natasha", "Romanov", 100, "BLACK WIDOW")
character3.add_character()
character4 = Avengers("\t Man", 49, 100, "Tony", "Stark", 100, "IRON MAN")
character4.add_character()
#%% Trial area
character0.all_character_listing() #Marvel class member all character listing.
character2.all_character_listing() #Avengers inheritance class member all character listing.
character0.all_age_average() #Marvel class member all character age listing.
character2.all_age_average() #Avengers inheritance class member all character age listing.
character0.character_listing() #Marvel class character  listing.
character2.character_listing() #Avengers inheritance class character listing.
character0.age_average() #Marvel class character age listing.
character2.age_average() #Avengers inheritance class character age listing.

