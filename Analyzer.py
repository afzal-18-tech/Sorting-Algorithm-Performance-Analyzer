import random
import time

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
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


# ---------- Analyzer Function ----------

def analyze_sorting_algorithms(n):
    data = [random.randint(0, 10000) for _ in range(n)]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": lambda arr: quick_sort(arr)  # returns new list
    }

    print(f"\nAnalyzing sorting performance for {n} elements:\n")
    print("{:<20} {:<20}".format("Algorithm", "Time (seconds)"))
    print("-" * 40)

    for name, func in algorithms.items():
        arr_copy = data.copy()
        start = time.time()
        if name == "Quick Sort":
            func(arr_copy)
        else:
            func(arr_copy)
        end = time.time()
        print("{:<20} {:.8f}".format(name, end - start))

# ---------- Run Analyzer ----------

n = int(input("Enter number of elements to sort: "))
analyze_sorting_algorithms(n)
