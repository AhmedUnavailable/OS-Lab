def sstf(reqs, curr):
    total_dist = 0
    curr
    while reqs:
        sst = min(reqs, key =  lambda x: abs(x - curr))
        
        total_dist += abs(sst - curr)
        curr = sst
        reqs.remove(sst)

    print(total_dist)


reqs = [82, 170, 43, 140, 24, 16, 190]
current =  50


sstf(reqs, current)