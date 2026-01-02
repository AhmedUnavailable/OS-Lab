def wf(frames, processes):
    available = frames.copy()
    tif = 0
    unallocated = []
    for p in processes:
        options = [f for f in available if p <= f]

        if options:
            w_f = max(options)
            tif +=  w_f - p
            print(f"{p} allocated to {w_f}")
            available.remove(w_f)

        else:
            unallocated.append(p)

    print(tif)


        


frames = [100, 50, 30, 120, 35]
processes = [90, 50, 30, 40]

wf(frames, processes)