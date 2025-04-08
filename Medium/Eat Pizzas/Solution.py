from collections import deque
from typing import List

class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        q = deque(pizzas)
        res = 0
        # odd days
        for _ in range(1, (len(pizzas) // 4)+1, 2):
            for i in range(3):
                q.popleft()
            res += q.pop()
        # even days
        for _ in range(2, (len(pizzas) // 4)+1, 2):
                for i in range(2):
                    q.popleft()
                q.pop()
                res += q.pop()

        return res