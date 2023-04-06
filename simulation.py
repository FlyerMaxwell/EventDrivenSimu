import heapq


class Simulation:
    """
    Represents a simulation
    """
    def __init__(self) -> None:
        self.exprStart = 0
        self.exprEnd = 20
        self.slotSize = 0.0005
        self.clock = self.exprStart
        self.events = []
        self.vehicles = []

        self.slotPerFrame = 200
    
    def run(self):
        """
        Runs the queue system until there are no more events in the event queue.
        """
        while self.events:
            event = heapq.heappop(self.events)
            # event.showInfo()
            print(event.timestamp)
            event.consume()
    
    def add_vehicles(self, car):
        """
        Adds an event to the event queue.

        :param event: The event to add to the queue.
        """
        self.vehicles.append(car)
        

    def add_event(self, event):
        """
        Adds an event to the event queue.

        :param event: The event to add to the queue.
        """
        heapq.heappush(self.events, event)
            
    
    def setTime(self, clock):
        self.clock = clock
            
    
    def showTime(self):
        print('clock = ', self.clock)