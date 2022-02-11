def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def choose_best_sum(t, k, ls):
    # t  - maximum sum of distances
    # k  - number of towns to visit
    # ls - list of distances
    
    if k > len(ls):
        return None
    
    gen = combinations(ls, k)
    sum_best = None
    
    for i in gen:
        sum_cur = sum(i)
        if sum_cur <= t:
            if sum_best is None:
                sum_best = sum_cur
            else:
                if sum_cur > sum_best:
                    sum_best = sum_cur
    
    return sum_best
