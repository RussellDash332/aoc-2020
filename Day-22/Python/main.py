input()
p1, p2 = [], []
import time
while True:
    try:
        p1.append(int(input()))
    except:
        break

input()
while True:
    try:
        p2.append(int(input()))
    except:
        break

q1, q2 = p1.copy(), p2.copy()

while p1 and p2:
    if p1[0] > p2[0]:
        p1.append(p1.pop(0))
        p1.append(p2.pop(0))
    else:
        p2.append(p2.pop(0))
        p2.append(p1.pop(0))
final = (p1 + p2)[::-1]

g = 0
def play(q1, q2, p):
    r = 0
    global g
    g, cg = g + 1, g + 1
    q1, q2 = q1.copy(), q2.copy()
    mem = set()
    while q1 and q2:
        if (tuple(q1), tuple(q2)) in mem:
            return (1, q1, q2)
        mem.add((tuple(q1), tuple(q2)))
        qq1, qq2 = q1[1:q1[0] + 1], q2[1:q2[0] + 1]
        if q1[0] <= len(qq1) and q2[0] <= len(qq2):
            sub = play(qq1, qq2, p)
            if sub[0] == 1:
                q1.append(q1.pop(0))
                q1.append(q2.pop(0))
            else:
                q2.append(q2.pop(0))
                q2.append(q1.pop(0))      
        elif q1[0] > q2[0]:
            q1.append(q1.pop(0))
            q1.append(q2.pop(0))
        else:
            q2.append(q2.pop(0))
            q2.append(q1.pop(0))
        
        if p:
            r += 1
            print("Round", r, "of Game", cg)
            print("Player 1:", q1)
            print("Player 2:", q2)
            print()
    if q1:
        return (1, q1, q2)
    else:
        return (2, q1, q2)

winner, f1, f2 = play(q1, q2, True) # last parameter to visualize game
final2 = eval(f"f{winner}")[::-1]
print("Part 1:", sum((i + 1) * final[i] for i in range(len(final))))
print("Part 2:", sum((i + 1) * final2[i] for i in range(len(final2))))