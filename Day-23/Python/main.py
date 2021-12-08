cups = list(map(lambda x: int(x) - 1, input()))
cups2 = cups.copy() + [i for i in range(len(cups), 1_000_000)]

# Naive, works for part 1 only
curr_pos = 0
m = len(cups)
for i in range(100):
    curr = cups[curr_pos]
    pickup = [cups[(curr_pos + 1) % m], cups[(curr_pos + 2) % m], cups[(curr_pos + 3) % m]]
    cups = list(filter(lambda x: x not in pickup, cups))
    dest = (curr - 1) % m
    while dest in pickup:
        dest = (dest - 1) % m
    pos = cups.index(dest)
    for j in pickup[::-1]:
        cups.insert(pos + 1, j)
    curr_pos = (cups.index(curr) + 1) % m
while cups[0] != 0:
    cups.append(cups.pop(0))
print("Part 1:", str().join(list(map(lambda x: str(x + 1), cups[1:]))))

# Linked list, works for both parts
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

d = {}
n = len(cups2)
ll = LinkedList()
ll.head = Node(cups2[0])
d[cups2[0]] = ll.head
cur = ll.head
for i in cups2[1:]:
    cur.next = Node(i)
    d[i] = cur.next
    cur = cur.next
cur.next = ll.head

for i in range(10_000_000):
    pickup = [ll.head.next.val, ll.head.next.next.val, ll.head.next.next.next.val]
    dest = (ll.head.val - 1) % n
    while dest in pickup:
        dest = (dest - 1) % n
    temp = ll.head.next.next.next.next
    ll.head.next.next.next.next = d[dest].next
    d[dest].next = ll.head.next
    ll.head.next = temp
    ll.head = ll.head.next
cur = ll.head
while cur.val != 0:
    cur = cur.next
print("Part 2:", (cur.next.val + 1) * (cur.next.next.val + 1))