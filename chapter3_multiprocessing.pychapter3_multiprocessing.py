import multiprocessing
import random
import time

def partial_sum(numbers):
    return sum(numbers)

def multiprocessing_execution():
    numbers = [random.randint(1, 100) for _ in range(1_000_000)]
    num_processes = 4
    size = len(numbers) // num_processes
    parts = [numbers[i*size : (i+1)*size] for i in range(num_processes)]

    start = time.time()
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(partial_sum, parts)

    total = sum(results)
    avg = total / len(numbers)
    end = time.time()

    print("\n--- Chapter 3: Multiprocessing Execution ---")
    print(f"Sum: {total}, Average: {avg:.2f}")
    print(f"Multiprocessing execution time: {end - start:.4f}s")

    return end - start
