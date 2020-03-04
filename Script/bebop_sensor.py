from pyparrot.Bebop import Bebop
from pyparrot.Bebop import BebopSensors
from bebop_cmd import *



bebop = Bebop(drone_type="Bebop2")

connect()
bebop.ask_for_state_update()
x = bebop.set_user_sensor_callback(batterie(), battery)
print(x)
disconnect()