def mult(p, q):
    return tuple(q[p[i] - 1] for i in range(len(p)))


def composition(s, f):
    new = set([])
    for i in s:
        for j in s:
            temp = mult(i, j)
            if temp not in s:
                new.add(temp)
                # s.append(temp)
    s.update(new)
    if f in s:
        return True

    while new:
        last = new
        new = set([])
        for i in last:
            for j in s:
                temp = mult(i, j)
                if temp not in s and temp not in new:
                    new.add(temp)
        s.update(new)
    return f in s

f11 = tuple([3, 1, 3, 4]) # 1->3 2->1 3->3 4->4
f12 = tuple([3, 4, 2, 1]) # tuples car une liste ne peut pas
s1 = set([f11,f12])       # servir d'élément d'un ensemble
f1 = tuple([1, 1, 1, 2])

f21 = tuple([3, 5, 4, 2, 6, 8, 1, 7])
f22 = tuple([1, 4, 3, 2, 5, 6, 7, 8])
s2 = set([f21,f22])
f2 = tuple([8, 7, 6, 5, 4, 3, 2, 1])

f31 = tuple([3, 3, 4, 4, 5, 5])
f32 = tuple([3, 4, 2, 1, 6, 6])
f33 = tuple([4, 4, 4, 4, 5, 5])
s3 = set([f31,f32,f33])
f3 = tuple([2, 1, 4, 3, 5, 5])

f41 = tuple([1, 2, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12])
f42 = tuple([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1])
f43 = tuple([2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
s4 = set([f41,f42,f43])
f4 = tuple([2, 1, 4, 3, 5, 7, 7, 7, 7, 7, 7, 7])

f51 = tuple([3, 3, 5, 5, 7, 7, 1, 1, 11, 12, 12, 1])
f52 = tuple([3, 3, 1, 1, 5, 5, 7, 7, 7, 4, 12, 11])
f53 = tuple([1, 1, 3, 3, 5, 5, 9, 7, 9, 9, 10, 12])
s5 = set([f51,f52,f53])
f5 = tuple([7, 7, 3, 3, 1, 1, 5, 5, 12, 11, 10, 4])

f61 = tuple([3, 4, 4, 2, 6, 8, 1, 7, 3])
f62 = tuple([4, 4, 4, 4, 4, 5, 5, 8, 1])
s6 = set([f61,f62])
f6 = tuple([2, 1, 4, 4, 5, 6, 8, 7, 3])

print(composition(s1, f1))
print(composition(s2, f2))
print(composition(s3, f3))
print(composition(s4, f4))
print(composition(s5, f5))
print(composition(s6, f6))