class Solution:
    def cleanString(self,s:str)->str:
        result=[]
        for c in s:
            if c.isalnum():
                result.append(c.lower())
        return "".join(result)
    def isPalindrome(self, s: str) -> bool:
        cleaned=self.cleanString(s)
        return cleaned==cleaned[::-1]
        