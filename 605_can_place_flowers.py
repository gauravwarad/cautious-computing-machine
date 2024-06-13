class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        
        i = 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                flowerbed [i] = 1
                if n > 0:
                    n -= 1
                else:
                    return True

        while i < len(flowerbed):
            if i == 0:
                if  i+1 < len(flowerbed):
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        if n > 0:
                            n -= 1
                        else:
                            return True
                        
                elif flowerbed[i] == 0:
                    flowerbed[i] = 1
                    if n > 0:
                        n -= 1
                    else:
                        return True
            
            elif i + 1 < len(flowerbed):
                if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    if n > 0:
                        n -= 1
                    else:
                        return True
            elif i == len(flowerbed) - 1:
                if len(flowerbed) >= 2:
                    if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                        flowerbed[i] = 1
                        if n > 0:
                            n -= 1
                        else:
                            return True
                else:
                    if flowerbed[i] == 0:
                        flowerbed[i] = 1
                        if n > 0:
                            n -= 1
                        else:
                            return True
            i += 1
            # case 1: i is the first element
            # case 2: i is in the middle
            # case 3: i is in the end
        print(flowerbed)
        if n == 0:
            return True
        return False


flowerbed = [0,0,0,0,0]
n = 2
print(Solution().canPlaceFlowers(flowerbed, n))