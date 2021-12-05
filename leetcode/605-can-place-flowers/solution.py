from typing import *


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        vacant_places = self.get_vacant_places(flowerbed)
        while n > 0:
            try:
                vacant_place = next(vacant_places)
            except StopIteration:
                return False
            n -= 1
        return True

    def get_vacant_places(self, flowerbed):
        current_index = 0
        while current_index < len(flowerbed):
            if self.is_vacant(current_index, flowerbed):
                yield current_index
                current_index += 2
            else:
                current_index += 1

    def is_vacant(self, index, flowerbed):
        left_index = max(0, index-1)
        right_index = min(index+1, len(flowerbed)-1)
        return (
            flowerbed[left_index] == 0
            and flowerbed[index] == 0
            and flowerbed[right_index] == 0
        )


solution = Solution()

print(solution.canPlaceFlowers([1, 0, 0, 0, 0], 3))
