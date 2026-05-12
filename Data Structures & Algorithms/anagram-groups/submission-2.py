class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sorted = dict()
        for x in strs:
            temp = ''.join(sorted(x))
            if temp in strs_sorted:
                strs_sorted[temp].append(x)
            else:
                strs_sorted[temp] = [x]
        return list(strs_sorted.values())