import time
import random

# Bubble sorting
def bubble_sort(arr):
    
    n = len(arr)
    
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
   
                
# Selection sorting
def selection_sort(arr):
    
    n = len(arr)
    
    for i in range(0, n-1):
        
        min_index = i
        
        for j in range(i+1, n):
            if(arr[j] < arr[min_index]):
                min_index = j
                
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
        
        
# Insertion sorting
def insertion_sort(arr):
    
    n = len(arr)
    
    for i in range(1, n):
        
        key = arr[i]
        j = i - 1
        
        while(j >= 0 and key < arr[j]) :
                arr[j+1] = arr[j]
                j = j - 1
                
        arr[j+1] = key
        
        
print("\n------------------ For Bubble sort ------------------\n")
        

# For best case

best_case1 = []

for i in range(15000):
    best_case1.append(i)
 
start = time.time()
bubble_sort(best_case1)
end = time.time()

print("Elapsed time (Best case): ", (end - start) * 1000, " milliseconds")

# For average case

avg_case1 = []

for i in range(15000):
    avg_case1.append(random.randint(0, 15000))
    

avg_case_unsorted = []
avg_case_unsorted = avg_case1

start = time.time()
bubble_sort(avg_case1)
end = time.time()

print("Elapsed time (Average case): ", (end - start) * 1000, " milliseconds")

# For worst case

worst_case1 = []

for i in range(15000, 0, -1):
    worst_case1.append(i)
    
worst_case_unsorted = []
worst_case_unsorted = worst_case1
    
start = time.time()
bubble_sort(worst_case1)
end = time.time()

print("Elapsed time (Worst case): ", (end - start) * 1000, " milliseconds")


print("\n------------------ For Selection sort ------------------\n")

# For best case

best_case2 = []
best_case2 = best_case1

start = time.time()
selection_sort(best_case2)
end = time.time()

print("Elapsed time (Best case): ", (end - start) * 1000, " milliseconds")

# For average case

avg_case2 = []
avg_case2 = avg_case_unsorted
    
start = time.time()
selection_sort(avg_case2)
end = time.time()

print("Elapsed time (Average case): ", (end - start) * 1000, " milliseconds")

# For worst case

worst_case2 = []
worst_case2 = worst_case_unsorted

for i in range(1000, 0, -1):
    worst_case2.append(i)
    
start = time.time()
selection_sort(worst_case2)
end = time.time()

print("Elapsed time (Worst case): ", (end - start) * 1000, " milliseconds")


print("\n------------------ For Insertion sort ------------------\n")


# For best case

best_case3 = []
best_case3 = best_case1

start = time.time()
insertion_sort(best_case3)
end = time.time()

print("Elapsed time (Best case): ", (end - start) * 1000, " milliseconds")


# For average case

avg_case3 = []
avg_case3 = avg_case_unsorted

start = time.time()
insertion_sort(avg_case3)
end = time.time()

print("Elapsed time (Average case): ", (end - start) * 1000, " milliseconds")


# For worst case

worst_case3 = []
worst_case3 = worst_case_unsorted

start = time.time()
insertion_sort(worst_case3)
end = time.time()

print("Elapsed time (Worst case): ", (end - start) * 1000, " milliseconds")