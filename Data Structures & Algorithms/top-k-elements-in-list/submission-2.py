class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapa = {}
        lista = []
        rez = []
        for num in nums:
            key = num
            if key not in mapa:
                mapa[key] = 0
            mapa[key] += 1
        
        for vrijednost in mapa.items():
            lista.append(vrijednost)
        
        lista.sort(reverse=True, key=lambda x: x[1])

        for i in range(k):
            rez.append(lista[i][0])

        return rez