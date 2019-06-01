#The event timer system. An abstract class
class status(object):
    def __init__(self, time):
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
            #self.unit.del_event(self)
            return n+self.result(self.unit)
        return n
    def kill(self):
        #self.unit.del_event(self)
        return self.death(self.unit)
        