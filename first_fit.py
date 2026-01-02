def ff(frames, processes):
    available = frames.copy()
    total_int_frag = 0
    unallocated = []

    for p in processes:
        target = None

        for f in available:
            if f >= p:
                target_frame = f
                break
        if target_frame is not None:
            total_int_frag += target_frame - p
            print(f"Process {p} allocated to {target_frame}")
            available.remove(target_frame)
        else:
            unallocated.append(p)
    print(f"{total_int_frag}")
    print(unallocated)   


frames = [100, 50, 30, 120, 35]
processes = [90, 50, 30, 40]
ff(frames, processes)