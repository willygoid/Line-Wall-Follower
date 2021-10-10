
from controller import Robot

def run_robot(robot):
    # Wall Followings

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
    t_kiri = 0
    t_henti = 0
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
        dindingdepan = sensor_dindingdepan.getValue() < 1000
        
     
        ada_garis = [batas_kiri, batas_kiri21, batas_kanan21, batas_kanan]
        
        # Read the sensors:
        print("IRL2 : {}, IRCL : {}, IRCR : {}, IRR2 : {}".format(batas_kiri2, batas_kiri, batas_kanan, batas_kanan2))
        print("DKiri {}: Dkanan : {}, Counter : {}, T-kiri : {}, T-henti : {}".format(dindingkiri, dindingkanan, counter, t_kiri, t_henti))
        
        left_speed = max_speed
        right_speed = max_speed
        
        if (ada_garis) and (t_henti != 25):
            if(counter == 86):
                left_speed = max_speed*2
                right_speed = max_speed*2
            elif(counter == 87):
                left_speed = max_speed*2
                right_speed = max_speed*2
            else:
                if (batas_kiri and batas_kanan):
                    print("Lurus")
                    left_speed = max_speed
                    right_speed = max_speed
                    
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
            if (dindingdepan == True):
                 print("Ada didepan, berhenti sebentar")
                 left_speed = 0
                 right_speed = 0  
            if (dindingkiri):
                 print("Lurus")
                 left_speed = max_speed*2
                 right_speed = max_speed*2
            if (dindingkanan):
                 print("Lurus")
                 left_speed = max_speed*2
                 right_speed = max_speed*2
                
        for i in range(2):
             if (i == 0 and (batas_kiri21 and batas_kanan21) and (batas_kiri1 and batas_kanan1) and t_kiri != 49): 
                print("T-1 belok kiri")
                left_speed = -max_speed      
                right_speed = max_speed*2
                t_kiri += 1
                break
             if (i == 1 and (batas_kiri21 and batas_kanan21) and (batas_kiri1 and batas_kanan1) and t_kiri != 49): 
                print("T-2 belok kiri")
                left_speed = -max_speed      
                right_speed = max_speed*2
                break
             if (batas_kiri21 and batas_kanan21) and (batas_kiri1 and batas_kanan1) and (t_kiri == 49):
                if(t_henti != 25):
                    print("T-3 lurus")
                    left_speed = max_speed*2      
                    right_speed = max_speed*2
                    t_henti += 1
                    break
                elif(t_henti > 25):
                    left_speed = 0
                    left_speed = 0
                    break
             if (batas_kiri21 and batas_kanan21) and (batas_kiri1 and batas_kanan1) and (t_henti == 25):
                 print("Berhenti")
                 left_speed = max_speed*0      
                 right_speed = max_speed*0

        # Enter here functions to send actuator commands, like:
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
    
    # Enter here exit cleanup code.
    
if __name__ == "__main__":

    # create the Robot instance.
    my_robot = Robot()
    run_robot(my_robot)