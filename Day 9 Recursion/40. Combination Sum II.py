def combinationSumHelper(candidates, target, a, ans, index):
    if target == 0: 
        ans.append(a[:])
        return
    if target < 0: return

    for i in range(index, len(candidates)):
        if i > index and candidates[i] == candidates[i - 1]:                        
            continue                                                                
        a.append(candidates[i])
        combinationSumHelper(candidates, target - candidates[i], a, ans, i + 1)
        a.pop()


class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans, a = [], []
        combinationSumHelper(candidates, target, a, ans, 0)
        return ans