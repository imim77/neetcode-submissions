class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapa = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            if num not in mapa:
                mapa[num] = 0
            mapa[num] += 1

        for broj,br_pojavljivanja in mapa.items():
            freq[br_pojavljivanja].append(broj)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if(len(res) == k):
                    return res

        