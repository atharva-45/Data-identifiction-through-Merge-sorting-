def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

def identify_duplicates(arr):
    sorted_arr = merge_sort(arr)
    duplicates = []
    
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] == sorted_arr[i+1]:
            duplicates.append(sorted_arr[i])
    
    return duplicates

# Example Usage:
data = [3, 1, 4, 2, 1, 6, 4, 3]
duplicates = identify_duplicates(data)

print("Duplicates: ", duplicates)
