def look(reqs, curr, dirc):
    left = [x for x in reqs if x <= curr]
    right = [x for x in reqs if x > curr]

    seq = []
    if dirc == "l":
        seq  = sorted(left)[::-1] + sorted(right)
    elif dirc == "r":
        seq = sorted(right) + sorted(left)[::-1]


    total_dist = 0
    for i in seq:
        total_dist += abs(i - curr)
        curr = i

    print("\n",total_dist)

reqs = [ 176, 79, 34, 60, 92, 11, 41, 114 ]
curr = 50
dirc = "r"

look(reqs, curr, dirc)