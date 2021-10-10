
from controller import Robot

def run_robot(robot):
    # Wall Following

    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    max_speed = 7.5
    
    #Enable motors
    left_motor = robot.getMotor('motor_1')
    right_motor = robot.getMotor('motor_2')
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    #Enable Distance Sensor bawah
    sensor_warnaIRL1 = robot.getDistanceSensor('IRL2')
    sensor_warnaIRL1.enable(timestep)
    
    sensor_warnaIRL2 = robot.getDistanceSensor('IRL1')
    sensor_warnaIRL2.enable(timestep)
    
    sensor_warnaIRCL = robot.getDistanceSensor('IRCL')
    sensor_warnaIRCL.enable(timestep)
    
    sensor_warnaIRCR = robot.getDistanceSensor('IRCR')
    sensor_warnaIRCR.enable(timestep)
    
    sensor_warnaIRR1 = robot.getDistanceSensor('IRR1')
    sensor_warnaIRR1.enable(timestep)
        
    sensor_warnaIRR2 = robot.getDistanceSensor('IRR2')
    sensor_warnaIRR2.enable(timestep)
    
    #Enable Distance Sensor Dinding
    sensor_dindingkiri = robot.getDistanceSensor('ds_left')
    sensor_dindingkiri.enable(timestep)
    
    sensor_dindingkanan = robot.getDistanceSensor('ds_right')
    sensor_dindingkanan.enable(timestep)
    
    sensor_dindingdepan = robot.getDistanceSensor('ds_front')
    sensor_dindingdepan.enable(timestep)
        
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    counter = 0
    def lurus():
        left_speed = max_speed
        right_speed = max_speed
    
    def boost():
         left_speed = max_speed*2
         right_speed = max_speed*2
    
    def kiri():
         left_speed = -max_speed
         counter += 1
    
    while robot.step(timestep) != -1:
        # Process sensor data here.
        batas_kiri2 = sensor_warnaIRL2.getValue() 
        batas_kiri1 = sensor_warnaIRL1.getValue() < 200
        batas_kiri = sensor_warnaIRCL.getValue() < 200
        batas_kanan = sensor_warnaIRCR.getValue() < 200
        batas_kanan1 = sensor_warnaIRR1.getValue() < 200
        batas_kanan2 = sensor_warnaIRR2.getValue() 
        
        batas_kiri21 = sensor_warnaIRL2.getValue() < 200
        batas_kanan21 = sensor_warnaIRR2.getValue() < 300
        
        dindingkiri = sensor_dindingkiri.getValue() < 1000
        dindingkanan = sensor_dindingkanan.getValue() < 1000
        dindingdepan = sensor_dindingdepan.getValue() > 1500
     
        ada_garis = [batas_kiri, batas_kiri21, batas_kanan21, batas_kanan]
        
        # Read the sensors:
        print("IRL2 : {}, IRCL : {}, IRCR : {}, IRR2 : {}".format(batas_kiri2, batas_kiri, batas_kanan, batas_kanan2))
        print("DKiri {}: Dkanan : {}, Ddepan : {}, Counter : {}".format(dindingkiri, dindingkanan, dindingdepan, counter))
   
        if(counter == 0):   
            left_speed = max_speed
            right_speed = max_speed
            if(sensor_warnaIRR2.getValue() > 500):
                counter += 1
        else:
            if (ada_garis):
                if (batas_kiri and batas_kanan):
                    lurus()
                    
                elif (batas_kiri > batas_kanan):
                    print("Belok Kiri")
                    left_speed = -max_speed
                    counter += 1
                elif (batas_kanan > batas_kiri):
                    print("Belok Kanan")
                    right_speed = -max_speed
                if (batas_kiri21):
                    print("Belok Kiri cepat")
                    left_speed = -max_speed       
                    right_speed = max_speed*2
                if (batas_kanan21):
                    print("Belok Kanan cepat")
                    left_speed = max_speed*2       
                    right_speed = -max_speed                                       
                     
            else:     
                if (dindingkiri):
                     boost()
                if (dindingkanan):
                     boost()
                     
    
            for i in range(2):
                 if (i == 0 and (batas_kiri21 and batas_kanan21) and (batas_kiri1 and batas_kanan1)): 
                    print("Perempatan 1 belok kiri")
                    left_speed = -max_speed      
                    right_speed = max_speed*2
                    break
                 if (i == 1 and (batas_kiri21 and batas_kanan21) and (batas_kiri1 and batas_kanan1)): 
                    print("Perempatan 2 belok kiri")
                    left_speed = -max_speed      
                    right_speed = max_speed*2
                    break
            
                 if (batas_kiri21 and batas_kanan21) and (batas_kiri1 and batas_kanan1):
                     print("Perempatan 3 lurus")
                     left_speed = max_speed      
                     right_speed = max_speed

        # Enter here functions to send actuator commands, like:
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
    
    # Enter here exit cleanup code.
    
if __name__ == "__main__":

    # create the Robot instance.
    my_robot = Robot()
    run_robot(my_robot)