class Event:
    """
    Represents a event
    """
    def __init__(self,aSim, type, clock, datap, bywho, handle_func) -> None:
        self.aSim = aSim
        self.type = type
        self.timestamp = clock
        self.datap = datap
        self.bywho = bywho
        self.handle_func = handle_func
    
    def __lt__(self,other):
        return self.timestamp < other.timestamp

    def consume(self):
        self.handle_func(self.aSim, self.datap, self.bywho)

    def showInfo(self):
        if(self.type == 'upLoc'):
            print('type=', self.type, ", timestamp=%.1f"%(self.timestamp), ", vehicle=", self.datap.id,", Location=%.3f"%(self.datap.displacement))
        if(self.type == 'broad'):
            print('type=', self.type, ", timestamp=%.1f"%(self.timestamp), ", vehicle=", self.datap.src.id)
        # print('type=',self.type, ", timestamp=", self.timestamp, ", datap=", self.datap, ", bywho=",self.bywho, "handl_func=", self.handle_func)