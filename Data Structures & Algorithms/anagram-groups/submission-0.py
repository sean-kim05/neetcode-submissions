class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for i in strs:
            key = ''.join(sorted(i))
            dict[key].append(i)

        return dict.values()

        
        