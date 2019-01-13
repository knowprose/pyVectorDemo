# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:42:57 2019

@author: Taran

This synchronous code is a quick hack that gives basic status.

For the battery state, the following from the SDK noted:
    
    Low = 1: 3.6V or less. If on charger, 4V or less.
    Nominal = 2
    Full = 3: This state can only be achieved when Vector is on the charger.

This code also does an image capture (image is not saved) and reports gyro status.

robot.disconnect is commented out because it raises the exception:
    "Attempted to access the connection loop before it was ready";
hints at SDK threading issue that is unresolved (the SDK is in Alpha, after all)
"""

import anki_vector
with anki_vector.Robot(enable_camera_feed=True) as robot:
#robot = anki_vector.Robot()
    print ("Getting Vector's diagnostics")
    print ("...Network State")
    network_state = robot.get_network_state()
    print ("Vector network state: {0}".format(network_state))
    print ("...Image capture")
    image = robot.camera.latest_image
    image.show()
    print(f"latest_image_id: {robot.camera.latest_image_id}")
    print("...Vector Gyro")
    current_gyro = robot.gyro
    
    print ("gyro: {0}".format(current_gyro))
    
    print ("Battery State")
    battery_state = robot.get_battery_state()
    if battery_state:
        print("Battery voltage: {0}".format(battery_state.battery_volts))
        print("Battery Level: {0}".format(battery_state.battery_level))
        print("Battery is charging?: {0}".format(battery_state.is_charging))
        print("On charger platform: {0}".format(battery_state.is_on_charger_platform))
        print("Suggested charger time: {0}".format(battery_state.suggested_charger_sec))
    else:
            print ("Cannot get battery_state!")
            
#robot.disconnect()        
        
