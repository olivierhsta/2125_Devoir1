def product(p, q):
    r = []
    for i in range(len(q)):
        r.append(p[q[i]-1])
    return r
    #return tuple(q[p[i] - 1] for i in range(len(p)))


def inverse(p):
    q = [0] * len(p)

    for i in range(len(p)):
        q[p[i]-1] = i + 1
    return q


def sift(tableau, p):
    IDENTITY = tuple(range(1, len(p)+1))
    q = p

    while q != IDENTITY:
        i = min(x for x in range(len(q)) if q[x] != x+1)
        j = q[i] - 1
        if tableau[i][j] == IDENTITY:
            tableau[i][j] = q
            return q
        else:
            q = product(q, inverse(tableau[i][j]))
        return None


def composition(permutations, r):
    IDENTITY = tuple(range(1, len(r)+1))
    tableau = [[IDENTITY] * len(r) for _ in range(len(r))]
    
    # Tamisage initial / Initial sift
    for p in permutations:
        sift(tableau, p)
        
        # Remplir tableau / Fill table
        to_sift = [(p, q) for p in permutations for q in permutations]
        
    while len(to_sift) > 0:
        p, q = to_sift.pop()
        q = sift(tableau, product(p, q))
        
        if q is not None:
        # q est une nouvelle permutation ajoutee au tableau
            to_sift.extend([(p, q) for p in permutations])
            to_sift.extend([(q, p) for p in permutations])
            
    # Genere r? / Generates r?
    return sift(tableau, r) is None
    
# Exemple / Example
# a = tuple([2, 1, 3, 4, 5]) # (12)(3)(4)(5)
# b = tuple([2, 3, 4, 5, 1]) # (12345)
# r = tuple([2, 1, 4, 5, 3]) # (12)(345)
# print(appartenance_intelligent(set([a, b]), r))

f51 = tuple([3, 3, 5, 5, 7, 7, 1, 1, 11, 12, 12, 1])
f52 = tuple([3, 3, 1, 1, 5, 5, 7, 7, 7, 4, 12, 11])
f53 = tuple([1, 1, 3, 3, 5, 5, 9, 7, 9, 9, 10, 12])
s5 = set([f51, f52, f53])
f5 = tuple([7, 7, 3, 3, 1, 1, 5, 5, 12, 11, 10, 4])


print(composition(s5, f5))

