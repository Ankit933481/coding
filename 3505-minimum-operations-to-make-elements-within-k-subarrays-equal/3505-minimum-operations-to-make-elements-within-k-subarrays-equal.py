import heapq
from collections import defaultdict
from typing import List

class DualHeap:
    def __init__(self):
        self.small = []  # Max heap (negative values)
        self.large = []  # Min heap
        self.delayed = defaultdict(int)

        self.small_size = 0
        self.large_size = 0
        self.small_sum = 0
        self.large_sum = 0

    def prune(self, heap):
        while heap:
            num = -heap[0] if heap is self.small else heap[0]
            if self.delayed[num] > 0:
                self.delayed[num] -= 1
                heapq.heappop(heap)
            else:
                break

    def rebalance(self):
        if self.small_size > self.large_size + 1:
            self.prune(self.small)
            num = -heapq.heappop(self.small)
            self.small_sum -= num
            self.small_size -= 1

            heapq.heappush(self.large, num)
            self.large_sum += num
            self.large_size += 1

            self.prune(self.small)

        elif self.small_size < self.large_size:
            self.prune(self.large)
            num = heapq.heappop(self.large)
            self.large_sum -= num
            self.large_size -= 1

            heapq.heappush(self.small, -num)
            self.small_sum += num
            self.small_size += 1

            self.prune(self.large)

    def add(self, num):
        self.prune(self.small)

        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_sum += num
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_sum += num
            self.large_size += 1

        self.rebalance()

    def remove(self, num):
        self.prune(self.small)

        self.delayed[num] += 1

        if num <= -self.small[0]:
            self.small_size -= 1
            self.small_sum -= num
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            self.large_sum -= num
            if self.large and num == self.large[0]:
                self.prune(self.large)

        self.rebalance()

    def cost(self):
        self.prune(self.small)
        median = -self.small[0]

        return (
            median * self.small_size - self.small_sum
            + self.large_sum - median * self.large_size
        )


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        maritovexi = (nums, x, k)

        # Calculate cost of every window of length x
        dh = DualHeap()
        costs = []

        for i in range(x):
            dh.add(nums[i])

        costs.append(dh.cost())

        for i in range(x, n):
            dh.remove(nums[i - x])
            dh.add(nums[i])
            costs.append(dh.cost())

        # DP: dp[t][i] = minimum cost using t windows
        # within the first i elements
        INF = float('inf')
        prev = [0] * (n + 1)

        for t in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Skip current position
                curr[i] = curr[i - 1]

                # Select window ending at i - 1
                if i >= x and prev[i - x] != INF:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]