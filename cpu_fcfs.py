def fcfs(processes):
    time = 0
    processes = processes.copy()
    for p in processes:
        if time < p["at"]:
            time = p["at"]
        time_first_cpu = time 

        p["ct"] = time = time + p["bt"]
        p["tat"] = p["ct"] - p["at"]
        p["rt"] = time_first_cpu - p["at"]
        
        print(p)



processes = [
    {"pid": "P1", "at": 0, "bt": 2},
    {"pid": "P2", "at": 1, "bt": 2},
    {"pid": "P3", "at": 5, "bt": 3},
    {"pid": "P4", "at": 6, "bt": 4}
]
fcfs(processes)