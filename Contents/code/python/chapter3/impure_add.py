count: int = 0

def increment_and_add(x: int) -> int:
    global count
    count += 1        # side effect: modifies external state
    print(count)      # side effect: performs I/O
    return x + count  # result depends on hidden external state
