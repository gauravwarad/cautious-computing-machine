import math

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        pairs = []
        potions.sort()
        print(potions)
        history = {}

        for i in spells:
            if i in history:#history[i]:
                pairs.append(history[i])
                continue
            target = (success/i)
            print(target)
            left = 0
            right = len(potions)
            while left < right:
                print("pairs currently is, -", pairs)
                mid = int((left + right)/2)
                print("left, right and mid are - ", left, right, mid)
                if left == right - 1:
                    if potions[left] >= target:
                        pairs.append(len(potions) - left)
                    elif right < len(potions) and potions[right] >= target:
                        pairs.append(len(potions) - right)
                    else:
                        pairs.append(0)
                    history[i] = pairs[-1]
                    break


                if potions[mid] == target:
                    while mid-1 !=0:
                        if potions[mid-1] == target:
                            mid = mid - 1
                        else:
                            break
                    pairs.append(len(potions) - mid)
                    print("found for target, ", target)
                    print("pairs is, ", pairs)
                    history[i] = pairs[-1]

                    break
                elif potions[mid] < target:
                    left = mid
                else:
                    right = mid
                # history[i] = pairs[-1]
        print(history)
        return pairs


    def successfulPairs2(self, spells: list[int], potions: list[int], success: int) -> list[int]:

        op = []
        potions.sort()
        history = {}

        for i in spells:
            if i in history:
                op.append(history[i])
                continue

            left = 0
            right = len(potions) - 1

            
            indi = len(potions)
            target = success/i

            while left <= right:
                mid = (left + right)//2

                if potions[mid] >= target:
                    indi = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            op.append(len(potions) - indi)
            history[i] = op[-1]


        return op














spells = [5,1,3, 5, 5]
potions = [2,1,3,4,5]
success = 7


# spells = [3,1,2]
# potions = [8,5,8]
# success = 16
# spells = [24]
# success = 600
# potions = [31,40,29,19,27,16,25,8,33,25,36,21,7,27,40,24,18,26,32,25,22,21,38,22,37,34,15,36,21,22,37,14,31,20,36,27,28,32,21,26,33,37,27,39,19,36,20,23,25,39,40]
print(Solution().successfulPairs2(spells, potions, success))