class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append((temperatures[i], i))
                continue
            
            while stack and temperatures[i] > stack[-1][0]:
                elem = stack.pop()
                duljina = i - elem[1]
                res[elem[1]] = duljina
            
            stack.append((temperatures[i], i))
    

        return res