def scan(reqs, curr, dirc):
    right = [r for r in reqs if r >= curr]
    left = [r for r in reqs if r < curr ]

    
    seq = []
    if dirc == "r":
        seq = sorted(right) + [199] + sorted(left)[::-1] 
    elif dirc == "l":
        seq = sorted(left)[::-1] + [0] + sorted(right)
    
    total_dist = 0
    for i in seq:
        total_dist += abs(curr - i)
        curr = i
    print(total_dist)



reqs = [ 176, 79, 34, 60, 92, 11, 41, 114 ]
current =  50
dirc = "l"

scan(reqs, current, dirc)