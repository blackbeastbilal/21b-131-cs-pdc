import random
import time

class ComputeNumbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_sum(self):
        return sum(self.numbers)

    def get_average(self):
        return sum(self.numbers) / len(self.numbers)

def basic_execution():
    numbers = [random.randint(1, 100) for _ in range(1_000_000)]
    comp = ComputeNumbers(numbers)

    start = time.time()
    total = comp.get_sum()
    avg = comp.get_average()
    end = time.time()

    print("\n--- Chapter 1: Basic Execution ---")
    print(f"Sum: {total}, Average: {avg:.2f}")
    print(f"Single-thread execution time: {end - start:.4f}s")

    return end - start
