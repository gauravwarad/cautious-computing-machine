class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()
        # print(asteroids)
        for asteroid in asteroids:
            if asteroid > mass:
                return False
            mass += asteroid
        return True
mass = 10
asteroids = [3,9,19,5,51]
print(Solution().asteroidsDestroyed(mass, asteroids))