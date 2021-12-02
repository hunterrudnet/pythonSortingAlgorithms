import unittest

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        item = arr[i] # this is the item we want to place
        j = i - 1
        while j >= 0 and item < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item
    return arr

class TestInsertionSort(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(insertion_sort([]), [])
    def test_arr(self):
        self.assertEqual(insertion_sort([3, 2, 1]), [1, 2, 3])
    def test_negatives(self):
        self.assertEqual(insertion_sort([-1, 5, 2, 3, 67, -99]), [-99, -1, 2, 3, 5, 67])
        
if __name__ == '__main__':
    unittest.main()