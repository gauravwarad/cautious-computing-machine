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
    def letterCombinations2(self, digits: str) -> list[str]:
        # backtracking 31st july 2024
        op = []
        if digits == "":
            return []
        mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def backtrack(current, i):
            print("current is - ", current)
            if len(current) == len(digits):
                op.append(current)
                return
            
            for j in range(i, len(digits)):
                for letter in mapping[digits[j]]:
                    current = current + letter
                    backtrack(current, j+1)
                    current = current[:-1]
            return
        backtrack("",0)

        return op
    

    def letterCombinations3(self, digits: str) -> list[str]:
        # backtracking 31st july 2024
        op = []
        if digits == "":
            return []
        mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def backtrack(current, i):
            print("current is - ", current)
            if len(current) == len(digits):
                op.append(current)
                return
            
            # for j in range(i, len(digits)):
            for letter in mapping[digits[i]]:
                current = current + letter
                backtrack(current, int(i)+1)
                current = current[:-1]
            return
        backtrack("",0)

        return op
digits = ""
print(Solution().letterCombinations3(digits))