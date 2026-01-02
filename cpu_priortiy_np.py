def priority_non_preemptive(processes):
    time = 0
    processes = [p.copy() for p in processes]
    n = len(processes)
    completed = 0
    
    results = []

    while completed < n:
        # Check who has arrived and isn't finished
        ready = [p for p in processes if p["at"] <= time and "ct" not in p]

        if not ready:
            # Jump to the next arrival if CPU is idle
            time = min(p["at"] for p in processes if "ct" not in p)
            continue

        # Pick highest priority (lowest number)
        curr = min(ready, key=lambda x: x["priority"])

        # Calculate times
        curr["ct"] = time + curr["bt"]
        curr["tat"] = curr["ct"] - curr["at"]
        curr["wt"] = curr["tat"] - curr["bt"]
        curr["rt"] = time - curr["at"]
        
        time = curr["ct"]
        completed += 1
        results.append(curr)
        print(curr)

processes = [
    {"pid": "P1", "at": 0, "bt": 2, "priority": 2},
    {"pid": "P2", "at": 1, "bt": 2, "priority": 1},
    {"pid": "P3", "at": 5, "bt": 3, "priority": 4},
    {"pid": "P4", "at": 6, "bt": 4, "priority": 3}
]

priority_non_preemptive(processes)

