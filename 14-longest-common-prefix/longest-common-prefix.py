class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
       
        common=""
        for i in range(len(strs[0])):
            char=strs[0][i]

            for word in strs:
                if i >= len(word) or word[i] != char:
                    return common
            common += char
        
        return common
