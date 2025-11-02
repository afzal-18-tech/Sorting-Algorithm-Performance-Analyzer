import random
import time
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk, messagebox

# ---------- Sorting Algorithms ----------

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# ---------- Performance Analyzer Function ----------

def analyze_sorting_algorithms():
    try:
        n = int(entry_size.get())
        if n <= 0:
            messagebox.showerror("Error", "Please enter a positive number!")
            return
    except:
        messagebox.showerror("Error", "Invalid input! Enter an integer.")
        return

    data = [random.randint(0, 10000) for _ in range(n)]
    selected_algos = [algo for algo, var in algo_vars.items() if var.get()]

    if not selected_algos:
        messagebox.showwarning("Warning", "Please select at least one algorithm!")
        return

    results = {}

    for name in selected_algos:
        arr_copy = data.copy()
        start = time.time()
        if name == "Bubble Sort":
            bubble_sort(arr_copy)
        elif name == "Insertion Sort":
            insertion_sort(arr_copy)
        elif name == "Merge Sort":
            merge_sort(arr_copy)
        elif name == "Quick Sort":
            quick_sort(arr_copy)
        end = time.time()
        results[name] = round(end - start, 6)

    # Display results in text box
    result_box.delete("1.0", END)
    for name, t in results.items():
        result_box.insert(END, f"{name}: {t:.6f} seconds\n")

    # Plot bar chart
    plt.figure(figsize=(6,4))
    plt.bar(results.keys(), results.values(), color=["blue", "green", "orange", "red"])
    plt.xlabel("Algorithms")
    plt.ylabel("Time (seconds)")
    plt.title(f"Sorting Performance for {n} elements")
    plt.tight_layout()
    plt.show()

# ---------- Tkinter GUI ----------
root = Tk()
root.title("Sorting Algorithm Performance Analyzer")
root.geometry("500x550")
root.configure(bg="#f7f7f7")

Label(root, text="Sorting Algorithm Performance Analyzer", font=("Arial", 14, "bold"), bg="#f7f7f7").pack(pady=10)

frame = Frame(root, bg="#f7f7f7")
frame.pack(pady=10)

Label(frame, text="Enter number of elements:", bg="#f7f7f7").grid(row=0, column=0, padx=5, pady=5)
entry_size = Entry(frame, width=10)
entry_size.grid(row=0, column=1, padx=5)

Label(root, text="Select Algorithms:", font=("Arial", 11, "bold"), bg="#f7f7f7").pack(pady=5)

algo_vars = {
    "Bubble Sort": BooleanVar(),
    "Insertion Sort": BooleanVar(),
    "Merge Sort": BooleanVar(),
    "Quick Sort": BooleanVar()
}

for name, var in algo_vars.items():
    Checkbutton(root, text=name, variable=var, bg="#f7f7f7", font=("Arial", 10)).pack(anchor=W, padx=100)

Button(root, text="Analyze Performance", command=analyze_sorting_algorithms, bg="#4CAF50", fg="white", font=("Arial", 11, "bold")).pack(pady=10)

Label(root, text="Results:", font=("Arial", 11, "bold"), bg="#f7f7f7").pack()
result_box = Text(root, height=10, width=50)
result_box.pack(pady=5)

Button(root, text="Exit", command=root.destroy, bg="#E74C3C", fg="white", font=("Arial", 11, "bold"), width=12).pack(pady=10)
root.mainloop()
