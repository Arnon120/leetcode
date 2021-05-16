class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    def maxSubArray(self, nums) -> int:
        """
        input: nums = a list of integers:
            len(nums) > 0
        """
        nums_improved = list()
        so_far = 0
        maximal = 0
        for num in nums:
            maximal = max(maximal,num)
            if so_far * num <= 0:
                if so_far !=0:
                    nums_improved.append(so_far)
                so_far = num
            else:
                so_far +=num
        if len(nums_improved) == 0:
            return maximal
        elif len(nums_improved) == 1:
            if nums_improved[0] < 0:
                return maximal
            else: #nums_improved[0] >0  as nums_improved[0] != 0
                return nums_improved[0]
        if nums_improved[0] <0:
            nums_improved.pop(0)
        #at this point, we have a list, starting with a positive number, where we know the positives and negatives are alternating.
        accume = nums_improved[0]
        two_dim_dynamic_programing = [[]]

numsnums = [
    [-2,1,-3,4,-1,2,1,-5,4],
    [1],
    [5,4,-1,7,8],
    [1,1,1,1],
    [-1,-1,-1,-1],
    [-1,1,-1,1,-1,1]
]
res = Solution().maxSubArray(numsnums[0])
            