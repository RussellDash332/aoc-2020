import sys

def bin_to_dec(b): # '01001' -> 9
    res = 0
    for i in b:
        res *= 2
        res += int(i)
    return res

def dec_to_bin(d): # 10 -> ['1', '0', '1', '0']
    res = []
    while d:
        res.append(str(d % 2))
        d //= 2
    return res[::-1]

def mask(m, val):
    new_val = ['0'] * len(m)
    for i in range(len(val), 0, -1):
        new_val[-i] = val[-i]
    for i in range(len(m)):
        if m[i] != "X":
            new_val[i] = m[i]
    return new_val

def mask2(m, val):
    new_val = ['0'] * len(m)
    for i in range(len(val), 0, -1):
        new_val[-i] = val[-i]
    for i in range(len(m)):
        if m[i] != "0":
            new_val[i] = m[i]
    return new_val

def list_all(bin_list): # example, ['1', '0', 'X', '1']
    res = ['']
    for i in bin_list:
        if i != 'X':
            res = list(map(lambda x: x + i, res))
        else:
            res = list(map(lambda x: x + '0', res)) + list(map(lambda x: x + '1', res))
    return list(map(bin_to_dec, res))

mem = {}
mem2 = {}
for line in sys.stdin:
    cmd, val = line.strip().split(" = ")
    if cmd == "mask":
        msk = val
    else:
        add = int(cmd[4:-1])
        temp = int(val)
        val = dec_to_bin(int(val))
        val = mask(msk, val)
        val2 = mask2(msk, dec_to_bin(add))
        adds = list_all(val2)
        mem[add] = bin_to_dec(str().join(val))
        for a in adds:
            mem2[a] = temp
print("Part 1:", sum(mem.values()))
print("Part 2:", sum(mem2.values()))