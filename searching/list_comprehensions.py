a1 = [x for x in range(101)]
print(a1)
a2 = [y for y in range(101) if y % 2 == 0]
print(a2)
a3 = [z for z in range (101) if z > 30]
print(a3)
a4 = [q * q for q in range(101)]
print(a4)
a5 = ["even" if s % 2 == 0 else "uneven" for s in range(101)]
print(a5)
a6 = [[i for i in range(n)] for n in range(101)]
print(a6)
#a7 = [[[[[i for i in range(h)] for h in range(g)] for g in range(f)] for f in range(e)] for e in range(101)]
#print(a7)