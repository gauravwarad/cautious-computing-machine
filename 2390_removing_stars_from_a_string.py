class Solution:
    def removeStars(self, s: str) -> str:
        stacku = []

        for i in s:
            if i == "*":
                stacku.pop()
            else:
                stacku.append(i)

        return "".join(stacku)



s = "leet**cod*e"
print(Solution().removeStars(s))