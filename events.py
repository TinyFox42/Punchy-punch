#The event timer system. An abstract class
class event(object):
    def __init__(self, time):
        #create the event
        pass
        
    def tick(self):
        #one tick passes. Return strings of what happens
        pass
        
    def kill(self):
        #anything that happens when the event is stopped prematurely
        pass

class physical(event):
    def __init__(self, time, result, usr, tar):
        #result function, attack user, attack target
        self.time=time
        self.tk=time
        self.result=result
        self.usr=usr
        self.tar=tar
    
    def tick(self):
        if not self.usr.is_defeated():
            self.tk-=1
            #if (self.tk)==(self.time/2)
            #Possibly put charging noticies here
            
            #if self.tk<=0:
                #Oh goodness, this will be difficult
        
    