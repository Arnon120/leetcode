import heapq
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        len_cand = len(candidates)
        out_list = []
        heapq.heapify(out_list)
        stack_for_indices = []
        cur_stack = []
        cur_sum = 0
        i = 0
        while i < len_cand or len(cur_stack) > 0:
            if i < len_cand:
                if cur_sum + candidates[i] <= target:
                    stack_for_indices.append(i)
                    cur_stack.append(candidates[i])
                    i += 1
                    cur_sum += cur_stack[-1]
                    if cur_sum == target:
                        # We found a match!
                        cur_to_insert = cur_stack.copy()
                        if cur_to_insert not in out_list:
                            heapq.heappush(out_list,cur_stack.copy())
                        # clean up structures after a match
                        cur_top = cur_stack.pop()
                        stack_for_indices.pop()
                        cur_sum -= cur_top
                        i += 1
                else: # cur_sum + candidates[i] > target:
                    if len(cur_stack) >0:
                        cur_top = cur_stack.pop()
                        i = stack_for_indices.pop() + 1
                        cur_sum -= cur_top
                    else:
                        break
            else:
                i = stack_for_indices.pop() + 1
                cur_top = cur_stack.pop()
                cur_sum -= cur_top
        return out_list

candidates = [
    1,1,1,1,1,
    1,1,1,1,1]

target = 9
output = Solution().combinationSum2(candidates,target)
print(output)
        


