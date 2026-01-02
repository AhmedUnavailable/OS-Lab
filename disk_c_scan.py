def c_scan(reqs, curr, dirc):
    left = [x for x in reqs if x <= curr]
    right = [x for x in reqs if x > curr]

    seq = []
    if dirc == "l":
        seq  = sorted(left)[::-1] + [0, 199] + sorted(right)[::-1]
    elif dirc == "r":
        seq = sorted(right) + [199, 0] + sorted(left)


    total_dist = 0
    for i in seq:
        total_dist += abs(i - curr)
        curr = i

    print("\n",total_dist)

reqs = [ 176, 79, 34, 60, 92, 11, 41, 114 ]
curr = 50
dirc = "r"


c_scan(reqs, curr, dirc)