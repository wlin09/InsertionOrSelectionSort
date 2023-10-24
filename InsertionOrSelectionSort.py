# This project intends to test the performance of insertion sort vs selection sort in differing scenarios.

# Imports
import random
import copy
import sys

# Implementation of insertion sort
def insertion_sort(arr):
  for k in range(1,len(arr)):
    cur = arr[k]
    j = k
    while j>0 and arr[j-1] > cur:
      arr[j] = arr[j-1]
      j = j-1
    arr[j] = cur

# Implementation of selection sort
def selection_sort(arr):
  for k in range(0,len(arr)):
    minloc = k
    j = k+1
    while j < len(arr):
        if arr[j]<arr[minloc]:
          minloc = j
        j = j + 1
    swap = arr[k]
    arr[k] = arr[minloc]
    arr[minloc] = swap

# Algorithm to allow for comparison of sorting methods in differing scenarios
if __name__ == '__main__':
  if len(sys.argv) < 3 or not sys.argv[1].isnumeric or sys.argv[2] not in ('increasing','decreasing','random'):
    print('Usage: python Sort.py <array_length> <increasing|decreasing|random>')
  else:
    if sys.argv[2] == "increasing":
      insertion_arr = [i for i in range(int(sys.argv[1]))]
    elif sys.argv[2] == "decreasing":
      insertion_arr = [int(sys.argv[1])-i for i in range(int(sys.argv[1]))]
    elif sys.argv[2] == "random":
      insertion_arr = [random.randint(0, 1000000000) for _ in range(int(sys.argv[1]))]
    selection_arr = copy.deepcopy(insertion_arr)
    insertion_sort(insertion_arr)
    selection_sort(selection_arr)