def combinationSumHelper(candidates, target, a, ans, index):
    if target == 0: 
        ans.append(a[:])
        return
    if target < 0: return

    for i in range(index, len(candidates)):
        a.append(candidates[i])
        combinationSumHelper(candidates, target - candidates[i], a, ans, i)
        a.pop()

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, a = [], []
        combinationSumHelper(candidates, target, a, ans, 0)
        return ans