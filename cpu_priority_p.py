def priority(processes):
    completed = 0
    n = len(processes)
    
    time = 0
    for p in processes:
        p["remt"] = p["bt"]

    while completed < n:
        ready = [p for p in processes if p["at"] <= time and p["remt"] > 0]
        
        
        if not ready:
            time = min(p["at"] for p in processes if p["remt"] > 0)
            
            continue
        
        curr = min(ready, key=lambda x: x["prrty"])
        
        if curr["remt"] == curr["bt"]:
            curr["rt"] = time - curr["at"]


        time += 1
        
        curr["remt"] -= 1

        if curr["remt"] == 0:
            curr["ct"] = time
            completed += 1
    for p in processes:
        print(p)

        


processes=[
    {"pid": "p1", "at":0, "bt":3, "prrty":3},
    {"pid": "p2", "at":1, "bt":4, "prrty":2},
    {"pid": "p3", "at":2, "bt":6, "prrty":4},
    {"pid": "p4", "at":3, "bt":4, "prrty":6},
    {"pid": "p5", "at":5, "bt":2, "prrty":10}
]

priority(processes)