class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stacku = []

        for i in asteroids:
            while i < 0 and len(stacku) > 0 and stacku[-1] > 0:
                difference = i + stacku[-1]
                if difference < 0:
                    stacku.pop()
                elif difference > 0:
                    i = 0
                else:
                    stacku.pop()
                    i = 0
            if i != 0:
                stacku.append(i)
            # print(stacku)

        return stacku



# what if [2,5,-4,-8,7,6] => 
asteroids = [5,10,-5]
print(Solution().asteroidCollision(asteroids))