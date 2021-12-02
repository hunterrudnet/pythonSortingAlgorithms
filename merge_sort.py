import unittest

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def merge(left, right):
    # We will make sure both lists are sorted here, this take O(nlogn) time
    # but we will disregard for the correctness of merge
    left.sort()
    right.sort()
    if len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    result = []
    leftidx, rightidx = 0, 0
    while len(result) < len(left) + len(right):
        if left[leftidx] < right[rightidx]:
            result.append(left[leftidx])
            leftidx += 1
        else:
            result.append(right[rightidx])
            rightidx += 1
        if rightidx == len(right):
            result += left[leftidx:]
            break
        if leftidx == len(left):
            result += right[rightidx:]
            break
    return result

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    midpoint = len(arr) // 2
    return merge(left=merge_sort(arr[:midpoint]), right=merge_sort(arr[midpoint:]))

class TestMergeSort(unittest.TestCase):
    def test_mergesort_empty(self):
        self.assertEqual(merge_sort([]), [])
    def test_arr(self):
        self.assertEqual(merge_sort([3, 2, 1]), [1, 2, 3])
    def test_negatives(self):
        self.assertEqual(merge_sort([-1, 5, 2, 3, 67, -99]), [-99, -1, 2, 3, 5, 67])
    def test_merge_empty(self):
        self.assertEqual(merge([], []), [])
    def test_merge_left_empty(self):
        self.assertEqual(merge([], [3, 1, 2]), [1, 2, 3])
    def test_merge_right_empty(self):
        self.assertEqual(merge([3, 1, 2], []), [1, 2, 3])
    def test_merge_arr(self):
        self.assertEqual(merge([3, 2, 1], [1]), [1, 1, 2, 3])
    def test_merge_negatives(self):
        self.assertEqual(merge([-1, 5, 2, 3, 67, -99], [1, 2, 3]), [-99, -1, 1, 2, 2, 3, 3, 5, 67])

if __name__ == '__main__':
    unittest.main()