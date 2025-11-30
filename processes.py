processes =[
    {"pid": 1, "pc": 0, "acc": 0, "state": "READY"},
    {"pid": 2, "pc": 0, "acc": 0, "state": "READY"},
] 
current_index = 0
def get_current_process():
    global current_index
    return processes[current_index]

def save_context():
    # get the current process object (call the accessor)
    p = get_current_process()
    # defensive: ensure p is a mapping before updating
    if isinstance(p, dict):
        p["pc"] += 1
        p["acc"] += 1
    else:
        # unexpected type - raise a clear error to make debugging easier
        raise TypeError(f"Expected current process to be a dict, got {type(p)!r}")

def switch_process():
    global current_index
    processes[ current_index ]["state"] = "READY"
    current_index = (current_index + 1) % len(processes)  # Round-robin scheduling
    processes[ current_index ]["state"] = "RUNNING"