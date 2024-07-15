# backtracking
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        op = []
        mapping = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        def backtracking(i, current):
            if len(current) == len(digits):
                print("current is, ", current)
                op.append(current)
                return

            for chara in mapping[int(digits[i])]:
                print("characters in mapping -- ", chara)
                backtracking(i+1, current + chara)
            
        backtracking(0, "")
        return op

digits = "23"
print(Solution().letterCombinations(digits))