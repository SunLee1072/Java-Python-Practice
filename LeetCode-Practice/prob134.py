from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total_gas = 0
        total_cost = 0
        current_gas = 0
        start = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                start = i + 1
                current_gas = 0

        if total_gas - total_cost < 0:
            return -1

        return start


s = Solution()
gas = [5, 1, 2, 3, 4]
cost = [4, 4, 1, 5, 1]

print(s.canCompleteCircuit(gas, cost))
