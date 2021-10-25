import random
import time


class Drone:
    x=0 #nach hinten -> 1LE entspricht 1cm
    y=0 #nach link/rechts -> 1LE entspricht 1cm
    z=0 #nach oben -> 1LE entspricht 1cm
    flying = False #specifies whether the drone is flying
    forward_velocity = 0
    backward_velocity = 0
    properies = [
        "cool",
        "made by rapto"
        ]
    def takeoff():
        if Drone.flying:
            print("you cannot take off when you've already taken off")
        else:
            print("starting taking-off-process")
            time.sleep(2)
            Drone.flying=True
            Drone.z = 1
            print("took off")
    def land():
        if Drone.flying:
            print("starting landing process")
            time.sleep(3)
            Drone.flying = False
            Drone.z = 0
            print("successfully landed!")
        else:
            print("you cannot start landing if you're already on the ground")
    def fly_up_or_down(value:int):
        if Drone.flying:
            if value>0:
                print("flying upwards")
                Drone.z+=value
                print(f"the drone now is at z={Drone.z}")
            elif value<0:
                print("flying downwards")
                Drone.z+=value
                print(f"the drone now is at z={Drone.z}")
            elif value==0:
                print("not doing anything")
                print(f"the drone is at z={Drone.z}")
        else: 
            if value>0:
                print("taking off")
                time.sleep(2.0)
                print("took off")
                Drone.flying=True
                Drone.z=1
                if value>1:
                    print("flying up")
                    Drone.z+=value
                    print(f"the drone is at z={Drone.z}")
                else:
                    Drone.z+=value
                    print(f"the drone is at z={Drone.z}")
            elif value<0:
                print("you cannot fly down if you already landed")  
            else:
                print("not doing anything")
                print(f"the drone is at z={Drone.z}")
    def fly_forward(velocity_kmh, timespan_secs):
        if Drone.flying:
            if int(velocity_kmh)>0:
                
                Drone.forward_velocity += int(velocity_kmh)
                timespan_hours = int(timespan_secs) / 60 / 60
                delta_s_km = Drone.forward_velocity*timespan_hours
                delta_s_m = delta_s_km * 1000
                delta_s_cm = delta_s_m * 100
                Drone.x += delta_s_cm
                print(f"""
                flying forward with 
                vel={velocity_kmh}km/h 
                for {timespan_secs}s or {timespan_hours}h. 
                That means, you fly for {delta_s_m}m or {delta_s_cm}cm.
                """)
            elif int(velocity_kmh)<0:
                print("you cannot fly forward with a negative velocity")
        else:
            print("you cannot fly forward when you're not flying")
    def fly_backwards(velocity_kmh, timespan_secs):
        if Drone.flying:
            if int(velocity_kmh)<0:
                Drone.backward_velocity += int(velocity_kmh)
                timespan_hours = int(timespan_secs) / 60 / 60
                delta_s_km = Drone.backward_velocity * timespan_hours
                delta_s_m = delta_s_km * 1000
                delta_s_cm = delta_s_m * 100
                Drone.x += delta_s_cm
                print(f"""
                flying backwards with 
                vel={velocity_kmh}km/h 
                for {timespan_secs}s or {timespan_hours}h. 
                That means, you fly for {delta_s_m}m or {delta_s_cm}cm.
                """)
            elif int(velocity_kmh)>0:
                print("you cannot fly backwards with a positive velocity")
        else:
            print("you cannot fly backwards when you're not in the air")
    def printPosition():
        print(f"The Drone is at x={Drone.x}, y={Drone.y}, z={Drone.z}")
    def fly_forward_or_backwards(distance_in_centimeters:int):
        if Drone.flying:
            if distance_in_centimeters>0:
                print(f"flying forwards for {distance_in_centimeters}cm")
                timespan = random.randint(1,4)
                time.sleep(timespan)
                Drone.x += distance_in_centimeters
                distance_in_meters = distance_in_centimeters / 100
                velocity_meterPerSecond = distance_in_meters / timespan
                velocity_kiloMeterPerHour = velocity_meterPerSecond * 3.6
                print(f"""
                the drone flew forward 
                in a timespan of {timespan}s with 
                a velocity of {velocity_kiloMeterPerHour}km/h
                and moved {distance_in_centimeters}m in total
                """)
            elif distance_in_centimeters<0:
                print(f"flying backwards for {distance_in_centimeters*-1}cm")
                anotherTimespan = random.randint(1,4)
                time.sleep(anotherTimespan)
                Drone.x += distance_in_centimeters
                distance_in_meters = distance_in_centimeters / 100
                velocity_meterPerSecond = distance_in_meters / anotherTimespan
                velocity_kiloMeterPerHour = velocity_meterPerSecond * 3.6
                print(f"""
                the drone flew forward 
                in a timespan of {anotherTimespan}s with 
                a velocity of {velocity_kiloMeterPerHour*-1}km/h
                or {velocity_meterPerSecond*-1}m/s
                and moved {distance_in_centimeters*-1}cm in total
                """)
            else: 
                print("not doing anything")
        else:
            print("you must takeoff before flying forward of backward")
    def fly_left(distance_in_centimeters):
        distance_in_meters = distance_in_centimeters / 100
        distance_in_kilometres = distance_in_meters / 1000
        timespan = random.randint(1,4)
        timespan_hours = timespan / 60 / 60
        velocity_metersPerSecond = distance_in_centimeters / timespan
        velocity_kilometresPerHour = distance_in_kilometres / timespan_hours 
        if Drone.flying:
            if distance_in_centimeters>0:
                print(f"flying left for {distance_in_centimeters}cm")
                time.sleep(timespan)
                Drone.y-=distance_in_centimeters
                print(f"""
                the drone flew forward 
                in a timespan of {timespan}s with 
                a velocity of {velocity_kilometresPerHour}km/h or {velocity_metersPerSecond}m/s
                and moved {distance_in_centimeters}cm or {distance_in_meters}m in total
                """)
            elif distance_in_centimeters<0:
                print("error: input must be positive")
        else:
            print("you cannot fly left if you're not on the ground")

