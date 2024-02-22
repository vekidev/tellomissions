import djitellopy, time 

dron = djitellopy.Tello() 
dron.connect(False) 

distance = 50
angle = 90
sec = 3

dron.takeoff() # Dron polece //
time.sleep(sec) 

dron.move_forward(distance + distance)
time.sleep(sec)

dron.rotate_clockwise(angle)
time.sleep(sec)

dron.move_forward(distance)
time.sleep(sec)

dron.rotate_clockwise(angle - 45)
time.sleep(sec)

dron.move_forward(distance - 15)
time.sleep(sec)

dron.rotate_clockwise(angle - 45)
time.sleep(sec)

dron.move_forward(distance)
time.sleep(sec)

dron.rotate_counter_clockwise(angle)
time.sleep(sec)

dron.move_forward(distance + distance)
time.sleep(sec)

dron.rotate_clockwise(angle)
time.sleep(sec)

dron.move_forward(distance + distance)
time.sleep(sec)

dron.rotate_clockwise(angle)
time.sleep(sec)

dron.move_forward(distance)
time.sleep(sec)

dron.rotate_clockwise(angle)
time.sleep(sec)

dron.move_forward(distance)
time.sleep(sec)

dron.rotate_counter_clockwise(angle)
time.sleep(sec)

dron.move_forward(distance)
time.sleep(sec)

dron.rotate_counter_clockwise(angle)
time.sleep(sec)

dron.move_forward(distance)
time.sleep(sec)

dron.rotate_clockwise(angle)
time.sleep(sec)

dron.move_forward(distance)
time.sleep(sec)

dron.rotate_counter_clockwise(angle)
time.sleep(sec)

dron.move_forward(distance)
time.sleep(sec)

dron.rotate_counter_clockwise(angle)
time.sleep(sec)

dron.move_forward(distance + distance)
time.sleep(sec)

dron.rotate_clockwise(angle)
time.sleep(sec)

dron.move_forward(distance)
time.sleep(sec)

dron.rotate_clockwise(angle)
time.sleep(sec)

dron.move_forward(distance + distance)
time.sleep(sec)

dron.rotate_counter_clockwise(angle)
time.sleep(sec)

dron.move_forward(distance)
time.sleep(sec)

dron.rotate_clockwise(angle)
time.sleep(sec)

dron.move_forward(distance - 25)
time.sleep(sec)

dron.rotate_clockwise(angle)
time.sleep(sec)

dron.move_forward(distance)
time.sleep(1.5)

dron.move_forward(distance)
time.sleep(1.5)

dron.move_forward(distance)
time.sleep(1.5)

dron.land()
