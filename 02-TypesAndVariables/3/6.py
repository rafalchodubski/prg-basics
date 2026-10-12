import math
#Write a program that calculates the distance to the horizon from a height given in meters from the keyboard

# I. You are standing on a beach, by the sea, on the water line (calculate the distance for your height in m)
h = 1.7
d = 3.57 * math.sqrt(h)
print(f'The horizon is {d} kilometers away in situation I.')

# II. You are looking out of a hotel window located by the sea, the window is at a height of 20 meters
h = 20
d = 3.57 * math.sqrt(h)
print(f'The horizon is {d} kilometers away in situation II.')