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
        usr.wait(self.tm, self.activate, [usr, tar]) #user needs to wait 5 time units to use the ability
        return "%s starts building up for a punch!"%(usr.name)
        #tar.defend(5) #the target is hit for 5 damage
    def activate(self, data):
        #data[0] is the user object
        #data[1] is the targtet object
        usr=data[0]
        tar=data[1]
        n="%s punches %s!"%(usr.name, tar.name)
        n+="\n"
        n+=tar.defend(5)
        return n
