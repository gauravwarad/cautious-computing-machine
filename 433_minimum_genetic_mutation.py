from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        
        # A C G T
        # node - AACCGGTT -> 
        # assuming every string has to be in the bank to proceed ->
        bank = set(bank)
        if endGene not in bank:
            return -1
        
        queua = deque()
        queua.append((startGene, 0))
        visited = set()
        visited.add(startGene)


        def possible_mutations(x):
            # a, c, g, t
            possible = []
            li = list(x)
            print(li)
            for i in range(0,8):
                for j in ('A','C','G','T'):
                    li = list(x)
                    if li[i] != j:
                        li[i] = j
                    s = "".join(li)
                    if s in bank and s not in visited:
                        possible.append(s)
            # print(possible)
            return possible
        
        # bfs

        while len(queua) > 0:

            current, steps = queua.popleft()

            if current == endGene:
                return steps
            
            possible = possible_mutations(current)
            
            for p in possible:
                # if p not in visited:
                queua.append((p, steps+1))
                visited.add(p)
        
        return -1


startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
print(Solution().minMutation(startGene, endGene, bank))