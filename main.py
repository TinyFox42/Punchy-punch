#A simple little game, at least for now

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
    def __str__(self):
        #When you try to print it normally, 
        return "%10s (%3ld%)"%(self.name, ((100*self.hp)/self.mhp))
    def defend(self, hit):
        #for now, "hit" is just a number of damage points. Later on it will be an object, for special defense logic
        d=hit-self.ac
        if d>0:
            self.hp-=d
            return "%s was hit for %d damage!"%(self.name, d)
        else:
            return "%s blocked the attack!"%(self.name)
    