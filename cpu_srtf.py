def srtf(processes):
    processes = processes.copy()

    for p in processes:
        p["remt"] = p["bt"] 

    n = len(processes)
    completed = 0
    time = 0
    total_rt = 0

    while completed < n:
        ready = [p for p in processes if p["at"] <= time and p["remt"] > 0]

        if not ready:
            time = min(p["at"] for p in processes if p["remt"] > 0)
            continue
        
        curr = min(ready, key=lambda x: x["remt"])

        if curr["remt"] == curr["bt"]:
            curr["rt"] = time - curr["at"]
            total_rt += curr["rt"]

        curr["remt"] -= 1
        time += 1

        if curr["remt"] == 0:
            curr["ct"] = time 
            curr["tat"] = curr["ct"] - curr["at"]
            curr["wt"] = curr["tat"] - curr["bt"]
            completed += 1

    
    for p in processes:
        print(p)




processes = [
    {"pid": "P1", "at": 0, "bt": 6},
    {"pid": "P2", "at": 1, "bt": 3},
    {"pid": "P3", "at": 2, "bt": 7}
]

srtf(processes)