class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={} #key:sorted word, value:list of anagrams
        for word in strs:
            key=''.join(sorted(word)) #signature for anagram group
            if key not in groups:
                groups[key]=[]
            groups[key].append(word)
        return list(groups.values())
