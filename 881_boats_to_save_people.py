import heapq
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        
        count = 0

        people.sort()

        while len(people) > 0:

            current = people.pop()
            if current <= limit:
                print(" 2 is less than limit")
                print("people is - ", len(people))
                if len(people) > 0 and people[0] + current <= limit:
                    print("inside if")
                    people.pop(0)
                
                count += 1 
            print(people)
        return count

    def numRescueBoats2(self, people: list[int], limit: int) -> int:

        count = 0

        people.sort()
        i = 0
        j = len(people) - 1
        while i <= j:
            count += 1
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1

        return count

people = [1,2]
limit = 3
print(Solution().numRescueBoats2(people, limit))