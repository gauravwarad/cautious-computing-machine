from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        # bfs?
        queua = deque()
        queua.append(((0,0,0,0), 0))
        visited = set()
        visited.add((0,0,0,0))

        directions = ((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),
                      (-1,0,0,0),(0,-1,0,0),(0,0,-1,0),(0,0,0,-1))
        deadends_set = set()
        for i in deadends:
            deadends_set.add(tuple(int(j) for j in i))
        target_tuple = tuple((int(i) for i in target))
        # print(deadends_set)
        # print(target_tuple)
        while len(queua) > 0:

            current, steps = queua.popleft()

            for d in directions:
                new_no = []
                for i in range(0,4):
                    temp = current[i] + d[i]
                    if temp == 10:
                        temp = 0
                    if temp == -1:
                        temp = 9
                    new_no.append(temp)
                if tuple(new_no) == target_tuple:
                # if "".join(str(x) for x in new_no) == target:
                    return steps + 1
                if tuple(new_no) not in visited:
                    if tuple(new_no) not in deadends_set:
                        queua.append((tuple(new_no), steps+1))
                    visited.add(tuple(new_no))
                # else:
                    # print("it's in visited, - ", tuple(new_no))
            # break
            # count += 1
            # if count == 100:
            #     break
            # print(len(visited))
        print(visited)
        return -1

                

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(Solution().openLock(deadends, target))