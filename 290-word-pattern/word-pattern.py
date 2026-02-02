class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        # If lengths differ, impossible to match
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for ch, word in zip(pattern, words):
            # If ch already mapped, check consistency
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False
            else:
                char_to_word[ch] = word

            # If word already mapped, check consistency
            if word in word_to_char:
                if word_to_char[word] != ch:
                    return False
            else:
                word_to_char[word] = ch

        return True
