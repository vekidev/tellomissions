import djitellopy, time, threading

from testtello import TestTello

dron = djitellopy.Tello()
# dron = TestTello() 
dron.connect() 

distance = 50

dron.takeoff()
# threading.Thread(target=dron.update).start()
time.sleep(3)

dron.update()

dron.move_forward(distance) # ide pravo 50
time.sleep(3)

dron.rotate_counter_clockwise(45) #skrece levo 45
time.sleep(3)

dron.move_forward(distance - distance + 36) # ide prabo 36
time.sleep(3)

dron.rotate_clockwise(45) # skrece desno 45
time.sleep(3)

dron.move_forward(distance) # ide pravo 50
time.sleep(3)

dron.rotate_counter_clockwise(90) # skrece levo 90
time.sleep(3)

dron.move_forward(distance) # ide pravo 50
time.sleep(3)

dron.rotate_counter_clockwise(90) #skrece levo 90
time.sleep(3)

dron.move_forward(distance) # ide pravo 50 
time.sleep(3)

dron.rotate_clockwise(90) # skerece desno 90
time.sleep(3)

dron.move_forward(distance) # ide prvo 50
time.sleep(3)

dron.rotate_counter_clockwise(90) # skrece levo 90
time.sleep(3)

dron.move_forward(distance * 2) # ide pravo 100
time.sleep(3)

dron.rotate_counter_clockwise(90) # skrece lev0 90
time.sleep(3)

dron.move_forward(distance) # ide pravo 50
time.sleep(3)

dron.rotate_counter_clockwise(90) # srece levo 90
time.sleep(3)

dron.move_forward(distance) # ide pravo 50
time.sleep(3)

dron.rotate_clockwise(90) # slrece desno 90
time.sleep(3)

dron.move_forward(distance) # ide pravo 50
time.sleep(3)

dron.rotate_clockwise(45) # skrece desno 45
time.sleep(3)

dron.move_forward(distance - distance + 36) # ide pravo 36
time.sleep(3)

dron.land()
