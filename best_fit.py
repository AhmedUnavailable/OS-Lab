def bf(frames, processes):
    available = frames.copy()
    tif = 0
    unallocated = []
    for p in processes:
        options = [f for f in available if f >= p]

        if options:
            best_fit = min(options)
            tif += best_fit - p
            print(f"Process {p} allocated to {best_fit}")

            available.remove(best_fit)
        else:
            unallocated.append(p)
    print(tif)

    


# frames = [100, 50, 30, 120, 35]
# processes = [90, 50, 30, 40]
frames = [30, 50, 200, 700]
processes = [20,200,500,50] 
bf(frames, processes)