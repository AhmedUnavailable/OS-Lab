def fifo(pages, capacity):
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
            hits += 1
    print(hits, miss)  

pages = [0, 2, 1, 6, 4, 0, 1, 0, 3, 1, 2, 1]
capacity = 4
fifo(pages, capacity)