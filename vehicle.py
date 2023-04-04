import heapq

class Vehicle:
    """
    Represents a vehicle
    """
    def __init__(self, id, speed, displacement, acceleration, commuR, safeR):
        self.id = id
        self.speed = speed
        self.displacement = displacement
        self.acceleration = acceleration
        self.commuR = commuR
        self.packets = []
        self.safeR = safeR
        self.maxSpeed = 2
        
    def addPacket(self, pkt):
        heapq.heappush(self.packets, pkt)

    def showInfo(self):
        print("id = ", self.id, ", speed = ", self.speed, ", displacement = ",self.displacement, ", acceleration = ", self.acceleration)



def updateLoc(aSim, car, dt):
    car.displacement = car.displacement + car.speed*dt


def broadcast(aSim, pkt, car):
    """
    the car broadcast and send the message to all its neighbors. The car generate the pkt with its own information and send it to neighbors
    """

    pkt.src = car
    pkt.dst = None
    pkt.data = [car.speed, car.displacement, car.acceleration]
    for neighbor in aSim.vehicles:
        if (neighbor.id == car.id)or(abs(neighbor.displacement - car.displacement) > car.commuR):
            continue
        else:
            neighbor.addPacket(pkt)
    

def makeDecision(aSim, packets,car):
    """
    The Car deceide what to do based on the received packets. We only consider the samelane case now. Check if there is a front car. If there is no front car, it try to turn up the speed or keep the maximum speed. If there is a front car, it should maintain the safe distance.
    """
    flag = 0
    for pkt in car.packets:
        if(pkt.data[1] > car.displacement):
            flag = 1
    if flag == 0:
        car.safeR = car.speed*car.speed/2/car.accerleration
    else:
        car.safeR 

