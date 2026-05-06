def reverse_tail_in_place(nums: List[int], start: int) -> None:
    n = len(nums)
    for i in range((n - start) // 2):
        nums[start + i], nums[n - 1 - i] = nums[n - 1 - i], nums[start + i]


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        The solution is based on: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
        """
        n = len(nums)
        if n <= 1:
            return
        
        k = n - 2
        while k >= 0:
            if nums[k] < nums[k + 1]:
                break
            
            k-=1
        
        if k == -1:
            reverse_tail_in_place(nums=nums, start=0)
            return
        
        l = n - 1
        while k < l:
            if nums[k] < nums[l]:
                break
            
            l-=1
        
        nums[k], nums[l] = nums[l], nums[k]
        reverse_tail_in_place(nums=nums, start=k + 1)


def test_next_permutation():
    nums_and_expectations = [
        ([0,1,2], [0,2,1]),
        ([0,2,1], [1, 0, 2])
    ]

    sol = Solution()
    for nums, expectation in nums_and_expectations:
        print(f"nums is: {nums}. Expects: {expectation}")
        sol.nextPermutation(nums=nums)
        assert nums == expectation, f"nums: {nums}"

test_next_permutation()

def test_reverse_tail_in_place():
    arrays_to_reverse = [
        ([0, 1, 2], 0),
        ([0, 1, 2], 1),
        ([0, 1, 2], 2),
        ([0, 1, 2, 3], 0),
        ([0, 1, 2, 3], 1),
        ([0, 1, 2, 3], 2),
        ([0, 1, 2, 3], 4),
        ([0, 1, 2, 3, 4], 0),
        ([0, 1, 2, 3, 4], 1),
        ([0, 1, 2, 3, 4], 2),
        ([0, 1, 2, 3, 4], 3),
        ([0, 1, 2, 3, 4], 4),
    ]

    for nums, start in arrays_to_reverse:
        print(f"nums is: {nums}, reverse at start: {start}")
        reverse_tail_in_place(nums=nums, start=start)
        print(f"Reversed: {nums}\n\n")