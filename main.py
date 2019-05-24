#A simple little game, at least for now
import abilities

class fighter(object):
    def __init__(self, name, mhp=10, ac=0):
        #Basic constructor. 
        #Name is what it will be reffered to, you may want to add numbers when you swarm them
        #mhp is "max hp", the highest the health can get to, and also the starting health
        #ac is armor class, the amount of damage that will be removed from each hit
        self.name=name
        self.mhp=mhp
        self.ac=ac
        self.hp=mhp
        self.skills=[]
    def __str__(self):
        #When you try to print it normally, 
        return "%10s (%3ld%s)"%(self.name, ((100*self.hp)/self.mhp),'%')
        #I'll work on making this a nicer print later on.
        #Like by finding out how to put a % symbol in there without messing up the format string
    def defend(self, hit):
        #for now, "hit" is just a number of damage points. Later on it will be an object, for special defense logic
        d=hit-self.ac
        if self.hp<=0:
            return "%s has already been defeated!"%(self.name)
        if d>0:
            self.hp-=d
            if self.hp>0:
                return "%s was hit for %d damage!"%(self.name, d)
            else:
                return "%s was hit for %d damage! %s has been defeated!"%(self.name, d, self.name)
        else:
            return "%s blocked the attack!"%(self.name)
    def learn(self, abil):
        self.skills.append(abil)
    def forget(self, abil):
        #Removes an ability
        #Note- you give this function the specific ability OBJECT, not just an object of the same ability type
        self.skills.remove(abil)
    def skill_list(self):
        n=""
        for i in range(len(self.skills)):
            n+=str(i)+". "
            n+=str(self.skills[i])
            n+="\n"
    def use_skill(self, pos, tar):
        #pos is the index of the skill in the skill list
        #tar is the target of the skill
        self.skills[pos].use(self, tar)
    def wait(self, time, event, evtData):
        #time is the number of time units to wait before the thing happens
        #event is the function that is called after that
        #evtData is the other information the event function needs
        self.timer=time
        self.event=event
        self.evtData=evtData
    def tick(self):
        if self.hp<=0:
            #anything that happens when unconcious
            return
        if type(self.timer)==int:
            if self.timer<=0:
                self.event(self.evtData)#not sure if this will actually work or not...
                self.timer=None
            else:
                self.timer-=1
                return
        #decision function! AI writing! Whoo!

'''class abil(object):
    #Does Python have abstract classes? This is an abstract class, pretty much
    def __init__(self, lvl=0):
        self.name="Confetti"
        #Stuff that won't matter until much later in development:
        self.lvl=lvl
        self.sp=0 #mana/stamina cost
        self.tm=0 #time cost
    def use(self, tar):
        #tar is the fighter that is the target of the ability
        return "%s is showered in confetti! It has litterally no effect!"%(tar.name)
    def __str__(self):
        return "%10s (lvl.%2d)"%(self.name, self.lvl)'''

