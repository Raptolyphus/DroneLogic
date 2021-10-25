import drone


myDrone = drone.Drone


if __name__ =="__main__":

    myDrone.takeoff()
    myDrone.fly_forward_or_backwards(-5)
    myDrone.land()
    myDrone.printPosition()