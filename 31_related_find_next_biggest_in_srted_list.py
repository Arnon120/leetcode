class Solution:
    def find_next_biggest_in_sorted_list(self,nums, pivot: int) -> int:
    #def find_next_biggest_in_sorted_list(self,nums: List[int], pivot: int) -> int:
        """
        return:     first index in nums bigger then pivot, 
                    or len(nums) if all elements in nums are smaller or equal to pivot,

        Assumes len(nums) >= 1
        """
        step = len(nums) // 2
        i = len(nums) //2
        while step > 0:
            if i >= len(nums):
                i = len(nums) -1
            if i == len(nums) -1:
                if nums[i] <= pivot:
                    return len(nums)
                else:
                    return i
            if i == 0:
                if nums[i] > pivot:
                    return 0
            if nums[i] <= pivot and nums[i+1] > pivot:
                return i+1
            
            step = (step // 2) + (step % 2)
            if nums[i] <= pivot:
                i = i + step
            elif nums[i] > pivot:
                i = i - step
            
        return i
    
    #def nextPermutation(self, nums: List[int]) -> None:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return None
        critical_point = 0
        for i in range(1,len(nums))[::-1]:
            if nums[i-1] < nums[i]:
                critical_point = i
                break
        if critical_point == 0:
            nums.sort()
            return None
        past_head = nums[critical_point-1]
        """ This part of the list is sorted in inverse order. One can do binary search to improve the find of the next head. 
        nums[i::-1]
        """
        index = critical_point + len(nums[-1: critical_point -1 :-1]) -1 - self.find_next_biggest_in_sorted_list(nums[-1: critical_point -1 :-1],past_head)
        if index == len(nums):
            nums.sort()
            return None
        else:
            temp = nums[index]
            nums[index] = past_head
            nums[critical_point-1] = temp
            for i in range(len(nums)-critical_point):
                if i+critical_point >= len(nums) - i -1:
                    break
                temp = nums[i+critical_point]
                nums[i+critical_point] = nums[len(nums) - i-1]
                nums[len(nums) - i -1 ] = temp 
            return None


sol = Solution()

numsnums =[
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]]
for nums in numsnums:
    sol.nextPermutation(nums)
print(numsnums)
"""
nums = [2,3,1]
sol.nextPermutation(nums)
print(nums)
"""