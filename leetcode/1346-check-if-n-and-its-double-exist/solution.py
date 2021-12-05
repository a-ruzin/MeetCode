from typing import *


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) > 1:
            return True
        uniq_arr = set(arr) - set([0])
        uniq_arr2 = {x * 2 for x in uniq_arr}
        return bool(uniq_arr & uniq_arr2)


solution = Solution()
print(solution.checkIfExist([1, 3, 5, 15, 6]))
