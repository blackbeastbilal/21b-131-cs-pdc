Parallel Python Project (Chapters 1–3)
This project combines concepts from the first three chapters:
1. Classes, loops, and basic Python functions
2. Threading and Locks
3. Multiprocessing and Process Pools
It performs the same task three ways:
* Single-thread (normal execution)
* Threading (shared memory)
* Multiprocessing (using multiple CPU cores)
Project Files:
* main.py — runs all parts and compares results
* chapter1_basics.py — basic Python and OOP logic
* chapter2_threading.py — threading implementation
* chapter3_multiprocessing.py — multiprocessing implementation
* output_comparison.txt — stores timing results
How to Run:
1. Open the folder in VS Code or any IDE.
2. Run the program using:
   python main.py
3. Check the output in the terminal and in output_comparison.txt

Example Output:
Sum: 50000000, Average: 50.00
Single-thread time: 1.24s
Threading time: 0.81s
Multiprocessing time: 0.30s

Concepts Used:
Classes and objects, loops, conditionals, file handling, threading, multiprocessing, and performance measurement using time module.


