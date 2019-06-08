#Skills list, separated so that I can keep this all organized
import statuses
class abil(object):
    #Does Python have abstract classes? This is an abstract class, pretty much
    def __init__(self, lvl=0):
        self.name="Confetti"
        #Stuff that won't matter until much later in development:
        self.lvl=lvl
        self.des="Showers the target with confetti. This looks cool, but doesn't really do anything."
    def use(self, usr, tar):
        #tar is the fighter that is the target of the ability
        #usr is the fighter that activated the ability
        return "{0} is showered in confetti by {1}! It has litterally no effect!".format(tar.name, usr.name)
    def __str__(self):
        return "{0:10} (lvl.{1:>2})".format(self.name, self.lvl)
    def update_flavor(self):
        #an optional function, for when the ability may change based off of level
        pass
    def desc(self):
        self.update_flavor()
        n=str(self)+":\n"
        n+="\t"+self.des 
        return n       
class charged_abil(abil):
    def __init__(self, lvl=0):
        self.name="Charged_abil"
        self.lvl=lvl
        self.des="An ability that charges before it is activated. (Sample deals 1 damage after 2 turns)"
    def use(self, usr, tar):
        if usr.is_ready():
            st=self.get_charger(usr, tar)
            usr.start_charging()
            usr.start_stat(st)
            return self.use_desc(usr, tar)
        #The next part is just in case something goes wrong, even though this should never happen
        return "{0} tries to use {1}, but is currently unable to.".format(usr.name, self.name)
    def use_desc(self, usr, tar):
        return "{0} starts charging an attack against {1}.".format(self.usr, self.tar)
    #charger parts:
    def charger_result(self, usr, tar):
        n="{0} attacks {1}!\n".format(usr.name, tar.name)
        n+=tar.defend(1)
        return n
    def charger_death(self, usr, tar):
        n="{0} stops charging their attack!".format(usr.name)
        return n
    def get_charger(self, usr, tar):
        st=statuses.attack_charge(2, usr, tar, self.charger_result, self.charger_death)
        return st
        
#Old punch ability. Used the old events system, instead of the new statuses ability
'''class punch(abil):
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
        return n'''
