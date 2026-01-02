def lru(pages, capacity):
    memory = []
    hits, miss = 0, 0
    for p in pages:
        if p not in memory:
            if len(memory) < capacity:
                memory.append(p)
            else:
                memory.pop(0)
                memory.append(p)
            miss += 1
        else: 
            lru = memory.pop(0)
            memory.append(p)
            hits += 1
    print(hits)
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 4
lru(pages, capacity)