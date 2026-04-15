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

sol = Solution()
l = [1,2,3,3,4,4,4,4,5,7,7,8,9,10]


for i in range(12):
    index = sol.find_next_biggest_in_sorted_list(l,i)
    print ('for '+str(i)+' we get '+str(index))