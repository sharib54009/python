# def quick_sort_iterative(arr):
#     stack = [(0, len(arr) - 1)]   # store start and end indexes

#     while stack:
#         low, high = stack.pop()   # pop one range

#         if low < high:
#             pivot = partition(arr, low, high)

#             # push the left and right parts (instead of recursive calls)
#             stack.append((low, pivot - 1))
#             stack.append((pivot + 1, high))


# def partition(arr, low, high):
#     pivot = arr[high]   # pick last element as pivot
#     i = low - 1

#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1


# # Example
# arr = [10, 7, 8, 9, 1, 5]
# print("Before sorting:", arr)
# quick_sort_iterative(arr)
# print("After sorting :", arr)
lst=[10,7,8,9,1,5]
piv=lst[0]
for i in range(0,len(lst)-1):
    for j in range(len(lst)-1, 0, -1):
        if lst[i] < piv and lst[j] > piv :
            temp= lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)