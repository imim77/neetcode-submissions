class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_size = k
        res = []
        q = collections.deque()

        l = 0
        for r in range(len(nums)):
                while len(q) >= 1 and nums[r] > q[len(q)-1]:
                    q.pop()
                q.append(nums[r])

                if window_size == r-l+1:
                    if q[0] == nums[l]:
                        res.append(q.popleft())
                    else:
                        res.append(q[0])
                    l += 1


        return res    