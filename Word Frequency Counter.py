class Solution:
    def countWords(self, text: str) -> dict[str, int]:
        l1 = []
        words = text.split()
        unique_words = set(words)
        wordCount = {}
        for x in unique_words:
            wordCount[x] = words.count(x)

        return wordCount


# --- Test Your Code ---
sol = Solution()
print(sol.countWords("apple banana apple cherry banana apple"))