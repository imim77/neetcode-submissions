import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapa1 = dict.fromkeys(string.ascii_lowercase, 0)
        mapa2 = dict.fromkeys(string.ascii_lowercase, 0)

        for slovo in s:
            mapa1[slovo] += 1

        for slovo in t:
            mapa2[slovo] += 1


        for kljuc, vrijednost in mapa1.items():
            if vrijednost != mapa2[kljuc]:
                return False
        
        return True

       