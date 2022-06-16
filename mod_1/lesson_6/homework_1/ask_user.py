import speed

distance = input("Jaką odległość pokonałeś? ")
time = input(f"W jakim czsie przebiegłeś {distance}? ")

avg_velocity = speed.avg_velocity(time=time, distance=distance)

print(f"Twoj średnia prędkość to {speed.avg_velocity(time, distance)}")