#Skills list, separated so that I can keep this all organized

class abil(object):
    #Does Python have abstract classes? This is an abstract class, pretty much
    def __init__(self, lvl=0):
        self.name="Confetti"
        #Stuff that won't matter until much later in development:
        self.lvl=lvl
        self.sp=0 #mana/stamina cost
        self.tm=0 #time cost
        self.des="Showers the target with confetti. This looks cool, but doesn't really do anything."
    def use(self, usr, tar):
        #tar is the fighter that is the target of the ability
        #usr is the fighter that activated the ability
        return "{0} is showered in confetti by {1}! It has litterally no effect!".format(tar.name, usr.name)
    def __str__(self):
        return "{0:10} (lvl.{1:>2})".format(self.name, self.lvl)
    def update_flavor(self):
        #an optional function, for when the ability may change based off of level
        return
    def desc(self):
        self.update_flavor()
        n=str(self)+":\n"
        n+="\tCharge Time:{0:>2}".format(self.tm)
        n+="\t"+self.des        
class punch(abil):
    def __init__(self, lvl=0):
        self.name="Punch"
        self.lvl=lvl
        self.sp=0
        self.tm=5
        self.des="Punches the target, dealing 5 damage."
    def use(self, usr, tar):
        usr.wait(self.tm, self.activate, [usr, tar]) #user needs to wait 5 time units to use the ability
        return "{0} starts building up for a punch!".format(usr.name)
        #tar.defend(5) #the target is hit for 5 damage
    def activate(self, data):
        #data[0] is the user object
        #data[1] is the targtet object
        usr=data[0]
        tar=data[1]
        n="{0} punches {1}!".format(usr.name, tar.name)
        n+="\n"
        n+=tar.defend(5)
        return n
