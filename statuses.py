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
    def __init__(self, time, tickev, result, death, unit, reps={}):
        self.time=time
        self.tk=time
        self.result=result
        self.tickev=tickev
        self.death=death
        self.reps=reps
        self.unit=unit
    
    def tick(self):
        if not self.usr.is_defeated():
            self.tk-=1
            self.tickev(self.unit)
            for i in self.reps.keys():
                if ((i*self.time)/100)==self.tk:
                    print self.reps[i].format(self.unit.name)
            
            if self.tk<=0:
                self.unit.del_event(self)
                return self.result(self.unit)
    def kill(self):
        self.unit.del_event(self)
        return self.death(self.unit)