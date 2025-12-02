import time
import tracemalloc
from functools import wraps

def performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.counter += 1

        tracemalloc.start()
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        wrapper.total_time += end_time - start_time
        wrapper.total_mem += peak

        return result

    wrapper.counter = 0
    wrapper.total_time = 0.0
    wrapper.total_mem = 0
    return wrapper


@performance
def slow_add(x, y):
    time.sleep(0.1)
    return x + y

for _ in range(5):
    slow_add(3, 4)

print(slow_add.counter)      
print(slow_add.total_time)   
print(slow_add.total_mem)    
