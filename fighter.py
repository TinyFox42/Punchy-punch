#Ok, complete restart of this. First off, lets make a base fighter
#2 actions:
#punch- deals 2 damage to the enemy
#block- cuts recieved damage until next turn in half

class fighter(object):
    def __init__(self, name, mhp):
        self.name=name
        self.mhp=mhp
        self.hp=mhp
        self.stati=[] #I don't feel like typing out statuses
    
    def report(self):
        print "{0}. {1}/{2}".format(self.name,self.hp,self.mhp)
        
    def get_hit(self, hit):
        if "block" in self.stati:
            hit.dmg /=2
        self.hp-=hit.dmg
        print "{0} was hit for {1} damage!".format(self.name, hit.dmg)
        
    def punch(self, tar):
        if "block" in self.stati:
            self.stati.remove("block")
        h=dumby_hit(2)
        tar.get_hit(h)
    def block(self):
        self.stati.append("block")
        
    def act(self, opp):
        #opp being a shorthand for "opponent" here. For now this is dueling
        print "Hit or Block? (H/b)"
        x=raw_input(">")
        if x=="b":
            self.block()
        else:
            self.punch(opp)
        
class dumby_hit(object):
    #a very simple hit object, just to fill in for now
    def __init__(self, dmg):
        self.dmg=dmg