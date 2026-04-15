class Solution:
    #def searchRange(self, nums: List[int], target: int) -> List[int]:
    def searchRange(self, nums, target: int):
        left = 0
        right = len(nums) - 1
        if right == -1:
            return [-1,-1]
        left_val = nums[left]
        right_val = nums[right]
        if target < left_val or target > right_val:
            return [-1,-1]
        mid = (left + right) //2
        while left < right:
            mid_val = nums[mid]
            if mid_val < target:
                left = min(mid + 1, right)
            elif mid_val > target:
                right = max(mid - 1, left)
            else: #mid_val = target
                break
            mid = (left + right) //2
        if left == right:
            if nums[left] != target:
                return [-1,-1]
            # else:
            # return [left,right]
        left_up_bound = mid
        right_down_bound = mid
        left_val = nums[left]
        right_val = nums[right]
        while left_val < target:
            left_mid = (left + left_up_bound) //2
            left_mid_val = nums[left_mid]
            if left_mid_val < target:
                left = left_mid + 1
                left_val = nums[left]
            else: #left_mid_val == target
                left_up_bound = max(left, left_mid-1)
        while target < right_val:
            right_mid = (right_down_bound + right) // 2
            right_mid_val = nums[right_mid]
            if right_mid_val > target:
                right = right_mid - 1
                right_val = nums[right]
            else: #right_mid_val
                right_down_bound = min(right_mid +1,right)
        return [left,right]

array = [
    {"nums": [5,7,7,8,8,10], "target": 11},
    {"nums": [5,7,7,8,8,10], "target": 10},
    {"nums": [5,7,7,8,8,10], "target": 9},
    {"nums": [5,7,7,8,8,10], "target": 8},
    {"nums": [5,7,7,8,8,10], "target": 7},
    {"nums": [5,7,7,8,8,10], "target": 6},
    {"nums": [5,7,7,8,8,10], "target": 5},
    {"nums": [5,7,7,8,8,10], "target": 4},
    {"nums": [1,2,2,4,8,8,10], "target": 11},
    {"nums": [1,2,2,4,8,8,10], "target": 10},
    {"nums": [1,2,2,4,8,8,10], "target": 5},
    {"nums": [1,2,2,4,8,8,10], "target": 4},
    {"nums": [1,2,2,4,8,8,10], "target": 3},
    {"nums": [1,2,2,4,8,8,10], "target": 2},
    {"nums": [1,2,2,4,8,8,10], "target": 1},
    {"nums": [1], "target": 2},
    {"nums": [1], "target": 1},
    {"nums": [1], "target": 0},
    {"nums": [], "target": 0}
]
for d in array:
    print("nums = "+str(d["nums"])+" target = "+str(d["target"])+ " result = "+str(Solution().searchRange(d["nums"],d["target"])))