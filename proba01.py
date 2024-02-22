import djitellopy, time 

dron = djitellopy.Tello() 
dron.connect(False) 

distance = 50

dron.takeoff() # Dron polece //
time.sleep(3) 

dron.move_forward(distance + 25) #ide napred 75 //
time.sleep(3)

dron.rotate_clockwise(90) #skrece desno //
time.sleep(3)

dron.move_forward(distance) #ide pravo 50 //
time.sleep(3)

dron.rotate_clockwise(90) #skrece desno //
time.sleep(3)

dron.move_forward(distance + 25) #ide pravo 75 //
time.sleep(3)

dron.rotate_counter_clockwise(90) #skrece levo //
time.sleep(3)

dron.move_forward(distance) #ide prvao 50 //
time.sleep(3)

dron.rotate_clockwise(90) #skrece desno //
time.sleep(3)

dron.move_forward(distance) #ide pravo 50 //
time.sleep(3)

dron.rotate_clockwise(90) #skerece desno //
time.sleep(3)

dron.move_forward(distance) #ide pravo 50 //
time.sleep(3)

dron.rotate_counter_clockwise(90) #skrece levo //
time.sleep(3)

dron.move_forward(distance) #ide pravo 50 //
time.sleep(3)

dron.rotate_clockwise(90) #skrece desno //
time.sleep(3)

dron.move_forward(distance) #ide pravo 50 //
time.sleep(3)

dron.rotate_counter_clockwise(90) #skrece levo //
time.sleep(3)

dron.move_forward(distance) #ide pravo 50 //
time.sleep(3)

dron.rotate_counter_clockwise(90) #skrece levo //
time.sleep(3)

dron.move_forward(2 * distance) #ide pravo 100 //
time.sleep(3)

dron.rotate_counter_clockwise(90) #skrece levo //
time.sleep(3)

dron.move_forward(distance) #ide pravo 50 //
time.sleep(3)

dron.rotate_counter_clockwise(90) #skrece levo //
time.sleep(3)

dron.move_forward(2 * distance) #ide pravo 100 //
time.sleep(3)

dron.rotate_clockwise(90) #skrece deno //
time.sleep(3)

dron.move_forward(2 * distance) #ide pravo 100 //
time.sleep(3) 

dron.land() #Dron slece //

