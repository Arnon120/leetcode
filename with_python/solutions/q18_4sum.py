from typing import Dict, Tuple, List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = []

        n = len(nums)
        nums.sort()
        # Counts sum accoumulated -> List pairs of indices.
        counted_pairs: Dict[int, Tuple[int, int]] = {}
        last_a = None
        for i in range(n):
            a = nums[i]
            if last_a == a:
                continue
            last_a = a

            if i + 1 < n:
                last_b = None
                for j in range(i + 1, n):
                    b = nums[j]
                    if last_b == b:
                        continue
                    last_b = b

                    partial_target = a + b
                    
                    my_list = counted_pairs.setdefault(partial_target, [])
                    my_list.append((i, j))
        
        last_d = None
        for l in reversed(range(n)):
            d = nums[l]
            if last_d == d:
                continue
            
            if l > 0:
                last_c = None
                for k in reversed(range(l)):
                    c = nums[k]
                    if last_c == c:
                        continue

                    key = target - c - d
                    potentials = counted_pairs.get(key)
                    if potentials is None:
                        continue
                    for (i, j) in potentials:
                        if j < k:
                            result.append([nums[i], nums[j], c, d])
                            last_c = c
                            last_d = d
        
        return result
    
sol = Solution()
test_cases = [
    # (
    #     [2,2,2,2,2], 8, [[2,2,2,2]],
    # ), 
    # (
    #     [1,0,-1,0,-2,2], 0 , [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]],
    # ),
    # (
    #     [-3,-2,-1,0,0,1,2,3], 0, [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]],
    # )
    (
        [1,-2,-5,-4,-3,3,3,5],
        -11,
        [[-5,-4,-3,1]]
    )
]

for nums, target, expected in test_cases:
    result = sol.fourSum(nums=nums, target=target)
    assert len(result) == len(expected)



# [
#     [-3,-2,2,3]
#     [-3,-1,1,3],
#     [-3,0,1,2],
#     [-2,-1,0,3],
#     [-2,-1,1,2],
# ]

# [
#     [-3,-2,2,3],
#     [-3,-1,1,3],
#     [-3,0,0,3],  # Missing.
#     [-3,0,1,2],
#     [-2,-1,0,3],
#     [-2,-1,1,2],
#     [-2,0,0,2],  # Missing.
#     [-1,0,0,1]   # Missing.
# ]