import time

def my_function(a, b):
    r = round(a + b)
    # Code to be timed
    time.sleep(1)  # Simulate some work
    return r

start_time = time.perf_counter()
my_function(2.4, 2.2)
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Execution time: {execution_time:.4f} seconds")