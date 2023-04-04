import heapq
import math

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
        self.safeR = safeR   # 单车安全距离
        self.maxSpeed = 2

        self.packets = []
        self.traceLoc = []
        self.traceCommR = []
        self.traceSpeed = []
        self.traceSafeR = []
        
        
    def addPacket(self, pkt):
        heapq.heappush(self.packets, pkt)

    def showInfo(self):
        print("id = ", self.id, ", speed = ", self.speed, ", displacement = ",self.displacement, ", acceleration = ", self.acceleration)



def updateLoc(aSim, car, dt):
    print(" Update Location-id=", car.id, "displacement=", car.displacement )
    car.displacement = car.displacement + car.speed*dt
    car.safeR = car.speed * car.speed/2/car.acceleration + car.speed*dt
    car.traceLoc.append(car.displacement)
    car.traceCommR.append(car.commuR)
    car.traceSpeed.append(car.speed)
    car.traceSafeR.append(car.safeR)



def broadcast(aSim, pkt, car):
    """
    the car broadcast and send the message to all its neighbors. The car generate the pkt with its own information and send it to neighbors
    """
    pkt.src = car
    pkt.dst = None
    pkt.data = [car.speed, car.displacement, car.acceleration]
    for neighbor in aSim.vehicles:
        if (neighbor.id == car.id)or(abs(neighbor.displacement - car.displacement) > car.commuR):
            print(" Broadcast-id=", car.id, ", dst= None",", pkt=", pkt.data)
        else:
            neighbor.addPacket(pkt)
            print(" Broadcast-id=", car.id, ", dst=", neighbor.id, ", pkt=", pkt.data)

    

def makeDecision(aSim, packets,car):
    """
    The Car deceide what to do based on the received packets. We only consider the samelane case now. Check if there is a front car. If there is no front car, it try to turn up the speed or keep the maximum speed. If there is a front car, it should maintain the safe distance.
    """
    
    if car.id == 'v_l': # 前车根据后车的通信情况调整自己的广播半径
        if(len(car.packets)):
            car.commuR = abs(car.packets[-1].data[1] - car.displacement)+0.1
            print( " UpCommuR-id=", car.id, ", commuR=", car.commuR)
            print(car.packets[-1].data)
            print(car.displacement)
        else:
            car.commuR = car.safeR+0.1
            print(" UpCommuR-id=", car.id, ", commuR=", car.commuR)



    if car.id == 'v_f': # 如果听到了前车
        if(len(car.packets)):
            
            g = car.packets[-1].data[1] - car.displacement  # prtotype Lidar
            speed_l = car.packets[-1].data[0]
            car.commuR = abs(g)+0.1
            print( " UpCommuR-id=", car.id, ", commuR=", car.commuR)
            print(car.packets[-1].data)
            print(car.displacement)
            car.speed = min(car.maxSpeed, car.speed+car.acceleration*aSim.slotSize,-car.acceleration + math.sqrt((car.acceleration*aSim.slotSize)**2 + speed_l**2 + 2*car.acceleration*g) )
        else:
            car.commuR = car.safeR+0.1
            print( " UpCommuR-id=", car.id, ", commuR=", car.commuR)
           