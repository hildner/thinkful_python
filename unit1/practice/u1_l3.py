import sys

class Musician(object):
    instances = []  
    def __init__(self, sounds):
        self.sounds = sounds
        self.instances.append(self) 

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bang","Wham", "Crash"])
    
    def beat_count(self):
        print("One!, Two!, Three!, Four!")
    
    def spont_combust(self):
        print("Poof")

class Band(object):
    def __init__(self,members):
        self.members = members
    def play_music(self):
        print("\nWe are {}!".format(band_name))
        print(Drummer().beat_count())
        for x in band.members:
            x.solo(6)
    def hire_member(self,person):
        self.members.append(person)
        print("\nYou're Hired! Now the band has {} members. Let's hear how you sound.".format(len(self.members)))
    def fire_member(self,person):
        self.members.remove(person)
        print("\nYou're Fired! The band only needs {} members!".format(len(self.members)))


if __name__ == "__main__":
    
    John = Guitarist()
    Paul = Guitarist()
    George = Bassist()
    Ringo = Drummer()
    band = Band([John, Paul, George, Ringo])
    
    if len(sys.argv) == 2:
        band_name = str(sys.argv[1])
    else:
        band_name = "The Beatles"
    band.play_music()
    band.fire_member(Paul)
    band.play_music()
    band.hire_member(Paul)
    band.play_music()