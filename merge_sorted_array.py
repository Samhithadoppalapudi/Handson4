
import heapq

def merge_k_sorted_arrays(arrays):
    min_heap = []
    result = []

    # Initialize the heap with the first element from each array
    for i, array in enumerate(arrays):
        if array:
            heapq.heappush(min_heap, (array[0], i, 0))

    # Extract elements from the heap and insert the next element from the respective array
    while min_heap:
        value, array_idx, element_idx = heapq.heappop(min_heap)
        result.append(value)

        # If there's another element in the same array, push it into the heap
        if element_idx + 1 < len(arrays[array_idx]):
            next_value = arrays[array_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, array_idx, element_idx + 1))

    return result

# Example usage
arrays1 = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
print(merge_k_sorted_arrays(arrays1))
