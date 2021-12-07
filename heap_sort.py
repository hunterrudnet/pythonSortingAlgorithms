import unittest

# We will use a Max Heap in our implementation
# Time Complexity: O(nlog(n))

def heapify(arr, heap_size, root):
    largest = root
    left = (2 * root) + 1
    right = (2 * root) + 2
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, heap_size, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

class TestHeapSort(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(heap_sort([]), [])
    def test_arr(self):
        self.assertEqual(heap_sort([3, 2, 1]), [1, 2, 3])
    def test_negatives(self):
        self.assertEqual(heap_sort([-1, 5, 2, 3, 67, -99]), [-99, -1, 2, 3, 5, 67])
        
if __name__ == '__main__':
    unittest.main()