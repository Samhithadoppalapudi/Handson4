problem 0
link is uploaded in github 

Problem 1
Implementation is found in merge_sorted_arrays.py
Time complexity is shown in the comments as T(n) = O(n * K * logK)
One way to improve the implementation is to use a priority queue or heap, pushing all first elements of k arrays into the heap. The lowest of the heap is put into the array, and the next element is pushed to the heap. Process repeats until the heap is empty and all elements are now in the merged sorted array.

Problem 2
Implementation is found in remove_duplicates.py
Time complexity is shown in the comments as O(n)
One way to improve this implementation is to check for arrays containing one element, as there is no need to process the removal of a single element.
