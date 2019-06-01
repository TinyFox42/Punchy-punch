import statuses
def poison_tick(unit):
    #Take a small amount of damage every turn
    n="The poison takes its effect on {0}!\n".format(unit.name)
    n+=unit.defend(1)
    return n
def poison_die(unit):
    #The poison ends
    n="The poison has ended its effects on {0}.".format(unit.name)
    return n
def poison_end(unit):
    #The poison gets even more annoying before being done
    n="The poison takes one last hit on {0}!\n".format(unit.name)
    n+=unit.defend(10)
    return n

poison_reps={50:"The poison is half done with its effect on {0}."}
class ex_poison(statuses.unit_status):
    #An example status, of being poisoned, in a really simple way (example, not feature)
    def __init__(self, time, unit):
        self.time=time
        self.tk=time
        self.unit=unit
        self.tickev=poison_tick
        self.death=poison_die
        self.result=poison_end
        self.reps=poison_reps