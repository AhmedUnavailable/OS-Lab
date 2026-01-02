def sjf(processes):
    processes = processes.copy()
    time = 0
    n = len(processes)
    total_tat, total_rt, total_wt = 0, 0, 0
    while processes:
        ready = [p for p in processes if p["at"] <= time]

        if not ready:
            time = min(p["at"] for p in processes)
            continue

        curr = min(ready, key= lambda x: x["bt"])
        processes.remove(curr)

        time_first_cpu = time

        curr["ct"] = time = time + curr["bt"]
        curr["tat"] = curr["ct"] - curr["at"]
        curr["rt"] = time_first_cpu - curr["at"]
        curr["wt"] = curr["tat"] - curr["bt"]
        
        total_wt += curr["wt"]
    
    print(f"Avg wait time {total_wt/n}")
        

     

        



processes = [
    {"pid": "P1", "at": 2, "bt": 6},
    {"pid": "P2", "at": 5, "bt": 2},
    {"pid": "P3", "at": 1, "bt": 8},
    {"pid": "P4", "at": 0, "bt": 3},
    {"pid": "P4", "at": 4, "bt": 4}
]
sjf(processes)