class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        # approaches - 2 pointers --?
        # or - stack & two iterations

        sl = list(s)
        print(sl)
        vowels = ['a', 'e', 'i', 'o', 'u']
        while i < j:
            if sl[i].lower() not in vowels:
                i += 1
            if sl[j].lower() not in vowels:
                j -= 1
            if sl[i].lower() in vowels and sl[j].lower() in vowels:
                temp = sl[i]
                sl[i] = sl[j]
                sl[j] = temp
                i += 1
                j -= 1
        return ''.join(sl)


s = "aA"
# op should be leotcede
print(Solution().reverseVowels(s))