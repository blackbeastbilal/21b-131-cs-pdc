from chapter1_basics import basic_execution
from chapter2_threading import threading_execution
from chapter3_multiprocessing import multiprocessing_execution

def main():
    print("\nParallel Python Project (Chapters 1–3)")
    print("-------------------------------------")

    single_time = basic_execution()
    thread_time = threading_execution()
    process_time = multiprocessing_execution()

    print("\nSummary of Execution Times (in seconds):")
    print(f"Single-thread     : {single_time:.4f}")
    print(f"Threading         : {thread_time:.4f}")
    print(f"Multiprocessing   : {process_time:.4f}")

    with open("output_comparison.txt", "w") as f:
        f.write("Performance Comparison (seconds)\n")
        f.write("--------------------------------\n")
        f.write(f"Single-thread     : {single_time:.4f}\n")
        f.write(f"Threading         : {thread_time:.4f}\n")
        f.write(f"Multiprocessing   : {process_time:.4f}\n")

    print("\nResults saved in 'output_comparison.txt'")

if __name__ == "__main__":
    main()
