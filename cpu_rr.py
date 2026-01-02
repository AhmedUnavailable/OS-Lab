def rr(processes, quantum):
    processes = processes.copy()
    n = len(processes)
    for p in processes:
        p["remt"] = p["bt"]

    processes.sort(key = lambda x: x["at"])

    ready = []
    time = 0 
    completed = 0
    while completed < n:
        for p in processes:
            if p["at"] <= time and p not in ready and p["remt"] > 0:
                ready.append(p)

        if not ready:
            time = min(p["at"] for p in processes if p["remt"] > 0)
            continue
    
        curr = ready.pop(0)

        if curr["bt"] == curr["remt"]:
            curr["rt"] = time - curr["at"]
        
        duration = min(curr["remt"], quantum)

        curr["remt"] -= duration
        time += duration

        for p in processes:
            if p["at"] <= time and p not in ready and p["remt"] > 0 and p != curr:
                ready.append(p)


        if curr["remt"] == 0:
            curr["ct"] = time
            curr["tat"] = curr["ct"] - curr["at"]
            curr["wt"] = curr["tat"] - curr["bt"]
            completed += 1


    for p in processes:
        print(p)





processes = [
    {"pid": "P1", "at": 0, "bt": 8},
    {"pid": "P2", "at": 5, "bt": 2},
    {"pid": "P3", "at": 1, "bt": 7},
    {"pid": "P4", "at": 6, "bt": 3},
    {"pid": "P5", "at": 8, "bt": 5}

]

rr(processes, 3)