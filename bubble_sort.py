import unittest

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def bubble_sort(arr):
    for i in range(len(arr)):
        sorted = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                # If the elements are reversed, swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False
        if sorted:
            # Short-circut
            break
    return arr

class TestBubbleSort(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(bubble_sort([]), [])
    def test_arr(self):
        self.assertEqual(bubble_sort([3, 2, 1]), [1, 2, 3])
    def test_negatives(self):
        self.assertEqual(bubble_sort([-1, 5, 2, 3, 67, -99]), [-99, -1, 2, 3, 5, 67])
        
if __name__ == '__main__':
    unittest.main()