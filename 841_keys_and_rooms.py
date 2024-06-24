class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        # i = 0
        
        keys = [0] # queue to store the keys
        visited = [0]*len(rooms)

        # i = 0

        while len(keys) > 0:
            current = keys.pop(0)
            # current is the room no which we are unlocking
            
            if visited[current] == 1:
                continue
            else:
                visited[current] = 1

            for j in rooms[current]:
                if j != 0:
                    keys.append(j)
            print(current)
            print(visited)
            print(keys)
            # break
        

        for i in visited:
            if i == 0:
                return False

        return True



class Room:
    def __init__(self, room_no, keys) -> None:
        self.room_no = room_no
        self.keys = keys # array
    

rooms = [[1,3],[3,0,1],[2],[0]]
print(Solution().canVisitAllRooms(rooms))