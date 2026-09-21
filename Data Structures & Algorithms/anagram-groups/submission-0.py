class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {} # key = sorted str, val = list of unsorted strs

        for x in strs:
            sort_x = "".join(sorted(x))

            if sort_x not in m:
                m[sort_x] = [x]
            else:
                m[sort_x].append(x)


        return list(m.values())