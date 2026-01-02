def fcfs(reqs, current):
    total_dist = 0 
    for i in reqs:
        total_dist += abs(i - current)
        current = i
    print(total_dist)

reqs = [82, 170, 43, 140, 24, 16, 190]
current =  50


fcfs(reqs, current)