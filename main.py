#A simple little game, at least for now
import abilities
#Statuses.
stsD=-1 #dead/defeated
stsR=0  #ready for new action
stsW=1  #waiting for event

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
        self.sts=stsR
        
    def __str__(self):
        #When you try to print it normally, 
        #return "%10s (%3ld%s)"%(self.name, ((100*self.hp)/self.mhp),'%')
        return "{0:10} ({1:3}%)".format(self.name, ((100*self.hp)/self.mhp))
        #I'll work on making this a nicer print later on.
        #Like by finding out how to put a % symbol in there without messing up the format string
    def defend(self, hit):
        #for now, "hit" is just a number of damage points. Later on it will be an object, for special defense logic
        d=hit-self.ac
        if self.hp<=0:
            return "{0} has already been defeated!".format(self.name)
        if d>0:
            self.hp-=d
            if self.hp>0:
                return "{0} was hit for {1} damage!".format(self.name, d)
            else:
                self.sts=stsD
                return "{0} was hit for {1} damage! {0} has been defeated!".format(self.name, d)
        else:
            return "{0} blocked the attack!".format(self.name)
    def learn(self, abil):
        self.skills.append(abil)
    def forget(self, abil):
        #Removes an ability
        #Note- you give this function the specific ability OBJECT, not just an object of the same ability type
        self.skills.remove(abil)
    def skill_list(self,t=0):
        n=""
        for i in range(len(self.skills)):
            n+="\t"*t
            n+=str(i)+". "
            n+=str(self.skills[i])
            n+="\n"
        return n
    def use_skill(self, pos, tar):
        #pos is the index of the skill in the skill list
        #tar is the target of the skill
        return self.skills[pos].use(self, tar)
    def wait(self, time, event, evtData):
        #time is the number of time units to wait before the thing happens
        #event is the function that is called after that
        #evtData is the other information the event function needs
        self.timer=time
        self.event=event
        self.evtData=evtData
        if self.sts==stsR:
            self.sts=stsW
        else:
            raise TypeError ("{0} was told to wait, while in invalid status {1}".format(self.name, self.sts))
        
    def tick(self):
        if self.sts==stsD:
            #anything that happens when unconcious, with some other return statement in there
            return ""
        if self.sts==stsW:
            if self.timer<=0:
                n=self.event(self.evtData)#not sure if this will actually work or not...
                self.timer=None
                self.sts=stsR
                return n
            else:
                self.timer-=1
                return ""
        #decision function! AI writing! Whoo!
            
    def decide(self, allies, enimies):
        #for the base fighter class, this will just be asking for user input
        print "You are playing as:"
        print "\t"+str(self)
        print allies
        print enimies
        print "Available actions:"
        print "\tL-List all skills"
        print "\tD-Ask for description of a skill"
        print "\tU-Use skill"
        cont=True
        while cont:
            x=raw_input(">")
            x=x.lower().strip()
            if x=="l":
                print self.skill_list()
            if x=="d":
                n=raw_input("Skill number: ")
                if n.isdigit():
                    n=int(n)
                    if n<0 or n>=len(self.skills):
                        print "Invalid skill number!"
                        continue
                    print self.skills[int(n)].desc()
                else:
                    print "That is not a number..."
            if x=="u":
                n=raw_input("Skill number: ")
                if not n.isdigit():
                    print "That is not a number..."
                    continue
                n=int(n)
                if n<0 or n>=len(self.skills):
                    print "Invalid skill number!"
                    continue
                sk=self.skills[n]
                sn=n
                #I need to finish this later. Get the target team, get the target number, and then use the skill
                #...
                print "You have selected the following skill:"
                print sk.desc()
                print "Would you like to target an Ally, Enemy, or Cancel? (a/e/C)"
                x=raw_input(">")
                x=x.strip().lower()
                if x=="e":
                    print str(enimies)
                    n=raw_input("Enemy number: ")
                    if not n.isdigit():
                        print "That is not a number..."
                        continue
                    n=int(n)
                    if n<0 or n>=enimies.get_member_count():
                        print "Invalid enemy number."
                        continue
                    tar=enimies.get_member(n)
                    print "You have selected the enemy: "+str(tar)
                    print("Are you sure you want to do this? y/N")
                    x=raw_input(">")
                    x=x.strip().lower()
                    if x=="y":
                        return self.use_skill(sn, tar)
                    continue
                if x=="a":
                    print str(allies)
                    n=raw_input("Ally number: ")
                    if not n.isdigit():
                        print "That is not a number..."
                        continue
                    n=int(n)
                    if n<0 or n>=allies.get_member_count():
                        print "Invalid ally number."
                        continue
                    tar=allies.get_member(n)
                    print "You have selected the ally: "+str(tar)
                    print "Are you sure you want to do this? y/N"
                    x=raw_input(">")
                    x=x.strip().lower()
                    if x=="y":
                        return self.use_skill(sn, tar)
                    continue
                continue
        
class team(object):
    def __init__(self, name):
        self.members=[]
        self.name=name
    def __str__(self):
        n=""
        n+="{0}:".format(self.name)
        n+="\n"
        for i in range(len(self.members)):
            n+="\t"+str(i)+". "
            n+=str(self.members[i])
            n+="\n"
        return n
    def tick(self):
        n=""
        for i in range(len(self.members)):
            x=self.members[i].tick()
            if x!="":
                n+=x
        return n
    def decide(self, enimies):
        n=""
        for i in range(len(self.members)):
            ft=self.members[i]
            if ft.sts==stsR:
                n+=ft.decide(self, enimies)
        return n
        
    def defend(self, hit):
        for i in range(len(self.members)):
            self.members[i].defend(hit)
    def add_member(self, member):
        self.members.append(member)
    def get_member_count(self):
        #For overloading later on
        return len(self.members)
    def get_member(self, pos):
        #assumes that the caller wasn't stupid
        return self.members[pos]
    def is_defeated(self):
        for i in range(len(self.members)):
            if self.members[i].sts==stsD:
                return False
        return True

class fight(object):
    #the main runner class. Finally getting to this!
    def __init__(self,team1,team2):
        self.t1=team1
        self.t2=team2
    def tick(self):
        print self.t1.decide(self.t2)
        print self.t1.tick()
        print self.t2.decide(self.t1)
        print self.t2.tick()
    def __str__(self):
        n=""
        n+=str(self.t1)
        n+=str(self.t2)
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

