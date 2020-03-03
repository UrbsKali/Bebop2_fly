#C:/Users/urbai/AppData/Local/Microsoft/WindowsApps/python.exe c:/Users/urbai/Documents/bebop.py

from pyparrot.Bebop import Bebop

bebop = Bebop()


def connect():
    print("connecting")
    success = bebop.connect(10)
    print(success)



def disconnect():
    print("Disconnecting")
    success = bebop.disconnect()
    print(success)



def take(x=5):
    bebop.safe_takeoff(x)


def land(x=5):
    bebop.safe_land(x)


def fow(inclinaison=20,time=1):
    bebop.fly_direct(0,inclinaison,0,0,time)


def up(power=5,time=1):
    bebop.fly_direct(0,0,0,power,time)


def down(power=5, time=1):
    bebop.fly_direct(0,0,0,-power,time)


def back(inclinaison=20,time=1):
    bebop.fly_direct(0,inclinaison,0,0,time)


def r_left(inclinaison=10,time=1):
    bebop.fly_direct(0,0,inclinaison,0,time)



def r_right(inclinaison=10,time=1):
    bebop.fly_direct(0,0,inclinaison,0,time)



def right(degre=10, time=1):
    bebop.fly_direct(degre,0,0,0,time)



def left(degre=10,time=1):
    bebop.fly_direct(-degre,0,0,0,time)


