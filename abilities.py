#Skills list, separated so that I can keep this all organized

class abil(object):
    #Does Python have abstract classes? This is an abstract class, pretty much
    def __init__(self, lvl=0):
        self.name="Confetti"
        #Stuff that won't matter until much later in development:
        self.lvl=lvl
        self.sp=0 #mana/stamina cost
        self.tm=0 #time cost
    def use(self, usr, tar):
        #tar is the fighter that is the target of the ability
        #usr is the fighter that activated the ability
        return "%s is showered in confetti by %s! It has litterally no effect!"%(tar.name, usr.name)
    def __str__(self):
        return "%10s (lvl.%2d)"%(self.name, self.lvl)
        
class punch(abil):
    def __init__(self, lvl=0):
        self.name="Punch"
        self.lvl=lvl
        self.sp=0
        self.tm=5
    def use(self, usr, tar):
        #usr.wait(5) #user needs to wait 5 time units to use the ability
        tar.defend(5) #the target is hit for 5 damage
        
