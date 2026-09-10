class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(path, i, total):
            if total == target:
                res.append(path.copy())
                return
            
            if i == len(candidates) or total > target:
                return
            
            curr_elem = candidates[i]
            path.append(curr_elem)
            backtrack(path, i+1, total+curr_elem)
            path.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(path, i+1, total)

        backtrack([], 0, 0)
        return res    