import threading
import random
import time

def partial_sum(numbers, results, index, lock):
    total = sum(numbers)
    with lock:
        results[index] = total

def threading_execution():
    numbers = [random.randint(1, 100) for _ in range(1_000_000)]
    num_threads = 4
    size = len(numbers) // num_threads
    threads = []
    results = [0] * num_threads
    lock = threading.Lock()

    start = time.time()
    for i in range(num_threads):
        part = numbers[i*size : (i+1)*size]
        thread = threading.Thread(target=partial_sum, args=(part, results, i, lock))
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()

    total = sum(results)
    avg = total / len(numbers)
    end = time.time()

    print("\n--- Chapter 2: Threading Execution ---")
    print(f"Sum: {total}, Average: {avg:.2f}")
    print(f"Threading execution time: {end - start:.4f}s")

    return end - start
