import djitellopy, time

dron = djitellopy.Tello()
dron.connect(False)

d = 25

dron.takeoff()
print('Poleteo sam')
time.sleep(3)

dron.move_down(20)
time.sleep(3)

dron.move_forward(d * 2 + d // 2)
time.sleep(3)

dron.rotate_clockwise(90)
time.sleep(3)

dron.move_forward(d * 2)
time.sleep(3)

dron.rotate_counter_clockwise(90)
time.sleep(3)

dron.move_forward(d * 2)
time.sleep(3)

dron.rotate_counter_clockwise(90)
time.sleep(3)

dron.move_forward(d * 4)
time.sleep(3)

dron.rotate_counter_clockwise(90)
time.sleep(3)

dron.move_forward(d * 3)
time.sleep(3)

dron.rotate_clockwise(90)
time.sleep(3)

dron.move_forward(d)
time.sleep(3)

dron.rotate_counter_clockwise(90)
time.sleep(3)

dron.move_forward(d)
time.sleep(3)

dron.rotate_counter_clockwise(90)
time.sleep(3)

dron.move_forward(d * 3)
time.sleep(3)

dron.rotate_clockwise(90)
time.sleep(3)

dron.move_forward(d // 2)
time.sleep(3)

dron.rotate_clockwise(180)
time.sleep(3)
print('sleteo sam')
dron.land()