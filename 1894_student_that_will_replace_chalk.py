class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        suma = sum(chalk)
        final_round = k % suma
        for i in range(len(chalk)):
            if final_round < chalk[i]:
                return i
            final_round -= chalk[i]
        return 0