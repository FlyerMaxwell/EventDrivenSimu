# Author: Maxwell
# Date: 2023/4/4
# Function: 本文件快速实现仿真场景及其可视化

import numpy as np
import heapq
import vehicle
from vehicle import Vehicle
from simulation import Simulation
from event import Event
from packet import Packet


aSim = Simulation()

# Add vehicles to aSim
aSim.add_vehicles(Vehicle(id = 'v_l', speed = 1, displacement = 5, acceleration = 0.5))
aSim.add_vehicles(Vehicle(id = 'v_f', speed = 2, displacement = 0, acceleration = 0.5))

for car in aSim.vehicles:
    car.showInfo()

# add event to aSim
for i in np.arange(aSim.exprStart, aSim.exprEnd, aSim.slotSize):
    
    # Communication
    # Transmission
    for car in aSim.vehicles:
        aSim.add_event(Event(type = "broad", aSim = aSim, clock= i, datap=Packet(clock=i), bywho=car, handle_func=vehicle.broadcast))
    
    # Receive and decode
    for car in aSim.vehicles:
        aSim.add_event(Event(type = "decode",aSim = aSim, clock= i, datap=car.packets, bywho=car, handle_func= vehicle.decodePkt))
    
    # Update Location
    for car in aSim.vehicles:
        aSim.add_event(Event(type = "upLoc",aSim = aSim, clock=i, datap= car, bywho= aSim.slotSize, handle_func=vehicle.updateLoc))


print(aSim.events)

# run simulator
aSim.run()
