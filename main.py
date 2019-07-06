#A simple little game, at least for now
import abilities
#Statuses.
stsD=-1 #dead/defeated
stsR=0  #ready for new action
stsW=1  #waiting for event

class fighter(object):
    def __init__(self, name, mhp=10):
        #Basic constructor. 
        #Name is what it will be reffered to, you may want to add numbers when you swarm them
        #mhp is "max hp", the highest the health can get to, and also the starting health
        #ac is armor class, the amount of damage that will be removed from each hit
        self.name=name
        self.mhp=mhp
        self.reacts=[]
        self.hp=mhp
        self.skills=[]
        self.ded=False
        self.red=True#"ready"
        self.stats=[]
        self.items=[]
        
    def __str__(self):
        #When you try to print it normally, 
        #return "%10s (%3ld%s)"%(self.name, ((100*self.hp)/self.mhp),'%')
        return "{0:10} ({1:3}%)".format(self.name, ((100*self.hp)/self.mhp))
        #I'll work on making this a nicer print later on.
        #Like by finding out how to put a % symbol in there without messing up the format string
    def defend(self, hit):
        #"hit" is an object that "reacts" will possibly block. It can be anything from a hex to a sword swing to a panacea
        for react in self.reacts:
            react.respond(hit)
        if hit.dispelled():
            return hit.dis_ex()
        return hit.resolve()
    def damage(self, dmg):
        if self.ded:
            return "{0} is already defeated, so therefore cannot take more damage.".format(self.name)
        elif dmg<=0:
            return "{0} takes no damage!".format(self.name)
        else:
            self.hp-=dmg
            n="{0} has taken {1} point(s) of damage!".format(self.name, dmg)
            if self.hp<=0:
                self.hp=0
                self.ded=True
                return n+"{0} has been defeated!".format(self.name)
            return n
    def heal(self, health):
        if self.ded:
            return "{0} is defeated, so cannot be healed that easily.".format(self.name)
        elif health<=0:
            return "{0} heals no health...".format(self.name)
        else:
            self.hp+=health
            if self.hp>self.mhp:
                self.hp=self.mhp
                return "{0} has been healed to full health!".format(self.name)
            return "{0} has been healed for {1} point(s) of health.".format(self.name, health)
    def revive(self, health, points=False):
        #if points=True, health is hp points healed. if False, health is % of max hp healed
        #health=25 points=false => revived with 25% max health
        #health=25 points=true => revived with 25 health points
        if not self.ded:
            return "{0} is not defeated, so cannot be revived...".format(self.name)
        else:
            self.ded=False
            n="{0} has been revived.".format(self.name)
            if points:
                return n+self.heal(health)
            else:
                x=(self.mhp*health)/100
                return n+self.heal(x)
    def learn_skill(self, abil):
        self.skills.append(abil)
    def forget_skill(self, abil):
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
    def tick(self):
        n=""
        for stat in self.stats:
            n+=stat.tick()
            n+="\n"
        return
    def start_stat(self, stat):
        self.stats.append(stat)
    def end_stat(self, stat):
        self.stats.remove(stat)
    #Yeah, I'm going to rework this whole system later:
    def is_defeated(self):
        return self.ded
    def is_ready(self):
        return self.sts==stsR
    
    '''def decide(self, allies, enimies):
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
                continue'''
        
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
            if ft.is_ready():
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
            if self.members[i].is_defeated():
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

