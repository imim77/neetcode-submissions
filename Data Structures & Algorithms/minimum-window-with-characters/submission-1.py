class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        mapa = defaultdict(int)
        mapa2 = defaultdict(int)

        for nesto in t:
            mapa[nesto] += 1
        
        need = len(mapa)


        l = 0
        have = 0
        res = [-1, -1]
        resLen = float("infinity")

        for r in range(len(s)):
            if s[r] in mapa:
                mapa2[s[r]] += 1
                if mapa2.get(s[r]) == mapa.get(s[r]):
                    have += 1

            while have == need:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l,r]
                if s[l] in mapa:
                    if mapa2[s[l]] == mapa[s[l]]:
                        have -= 1
                    mapa2[s[l]] -= 1
                l += 1
        
        return s[res[0]:res[1]+1]
