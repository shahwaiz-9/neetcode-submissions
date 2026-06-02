class Solution:

    def create_map1(self, s: str)-> dict:
        map = dict()
        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]]  = 1

        return map

    def create_map2(self, t: str)-> dict:
        map = dict()
        for i in range(len(t)):
            if t[i] in map:
                map[t[i]] += 1
            else:
                map[t[i]]  = 1

        return map

    def isAnagram(self, s: str, t: str) -> bool:

        map1 = self.create_map1(s)
        map2 = self.create_map2(t)


        return (map1 == map2)    





        