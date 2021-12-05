import sys
from math import *

x, y, angle = 0, 0, 0
x2, y2, xwp, ywp = 0, 0, 10, 1
for line in sys.stdin:
    cmd, dis = line[0], int(line[1:])
    if cmd == "N":
        y += dis
        ywp += dis
    elif cmd == "S":
        y -= dis
        ywp -= dis
    elif cmd == "E":
        x += dis
        xwp += dis
    elif cmd == "W":
        x -= dis
        xwp -= dis
    elif cmd == "R":
        xwp, ywp = xwp * cos(dis * pi / 180) + ywp * sin(dis * pi / 180), - xwp * sin(dis * pi / 180) + ywp * cos(dis * pi / 180)
        angle = (angle - dis) % 360
    elif cmd == "L":
        xwp, ywp = xwp * cos(dis * pi / 180) - ywp * sin(dis * pi / 180), xwp * sin(dis * pi / 180) + ywp * cos(dis * pi / 180)
        angle = (angle + dis) % 360
    else: # F
        x += dis * cos(angle * pi / 180)
        y += dis * sin(angle * pi / 180)
        x2 += xwp * dis
        y2 += ywp * dis
print("Part 1:", abs(round(x)) + abs(round(y)))
print("Part 2:", abs(round(x2)) + abs(round(y2)))