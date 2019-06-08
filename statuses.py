#The event timer system. An abstract class
class status(object):
    def __init__(self):
        #create the event
        pass
        
    def tick(self):
        #one tick passes. Return strings of what happens
        pass
        
    def kill(self):
        #anything that happens when the event is stopped prematurely
        pass

class unit_status(status):
    def __init__(self, time, unit, tickev, result, death, reps={}):
        self.time=time
        self.tk=time
        self.result=result
        self.tickev=tickev
        self.death=death
        self.reps=reps
        self.unit=unit
    
    def tick(self):
        n=""
        self.tk-=1
        n+=self.tickev(self.unit)
        for i in self.reps.keys():
            if ((i*self.time)/100)==self.tk:
                n+=self.reps[i].format(self.unit.name)
            
        if self.tk<=0:
            self.unit.end_stat(self)
            return n+self.result(self.unit)
        return n
    def kill(self):
        self.unit.end_stat(self)
        return self.death(self.unit)
        
class attack_charge(status):
    def __init__(self, time, usr, tar, result, death, reps={}):
        self.time=time
        self.tk=time
        self.usr=usr
        self.tar=tar #If you mess around with the inputs of result, you could just make this any data for the end
        self.result=result
        self.death=death
        self.reps=reps
        
    def tick(self):
        n=""
        if self.usr.is_charging():
            self.tk-=1
            for i in self.reps.keys():
                if ((i*self.time)/100)==self.tk:
                    n+=self.reps[i].format(self.unit.name)
            if self.tk<=0:
                self.usr.end_stat(self)
                self.usr.end_charging()
                return n+self.result(self.usr, self.tar)
        return n
    
    def kill(self):
        self.unit.end_stat(self)
        self.unit.end_charging()
        return self.death(self.usr, self.tar)