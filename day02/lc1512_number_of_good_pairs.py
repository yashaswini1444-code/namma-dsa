"""
Problem   : LC 1512 - Number of Good Pairs
Link      : https://leetcode.com/problems/number-of-good-pairs/
Difficulty: Easy
Pattern   : Frequency map (pairs with earlier copies)
Status    : Solved with hint

APPROACH (in my own words, written BEFORE coding):
1. A good pair is (i, j) with i < j and nums[i] == nums[j].
2. Brute force: two nested loops check every pair -> O(n^2).
3. Better: walk left to right with a dict count = {number: how many seen so far}.
4. When I see num, it makes a new pair with EVERY earlier copy of num,
   so pairs += count.get(num, 0).
5. Then record this copy: count[num] = count.get(num, 0) + 1.
6. Return pairs.

DRY RUN (nums = [1,2,3,1,1,3]):
num 1 -> earlier 1s = 0 -> pairs = 0 -> count {1:1}
num 2 -> earlier 2s = 0 -> pairs = 0 -> count {1:1, 2:1}
num 3 -> earlier 3s = 0 -> pairs = 0 -> count {1:1, 2:1, 3:1}
num 1 -> earlier 1s = 1 -> pairs = 1 -> count {1:2, 2:1, 3:1}
num 1 -> earlier 1s = 2 -> pairs = 3 -> count {1:3, 2:1, 3:1}
num 3 -> earlier 3s = 1 -> pairs = 4 -> count {1:3, 2:1, 3:2}
Output: 4
"""


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        pairs = 0
        count = {}
        for num in nums:
            pairs += count.get(num, 0)
            count[num] = count.get(num, 0) + 1
        return pairs


# ---------------- Local tests ----------------
if __name__ == "__main__":
    s = Solution()
    print(s.numIdenticalPairs([1, 2, 3, 1, 1, 3]))  # expected: 4
    print(s.numIdenticalPairs([1, 1, 1, 1]))        # expected: 6
    print(s.numIdenticalPairs([1, 2, 3]))           # expected: 0


"""
TIME COMPLEXITY : O(n)  because one loop, and dict get / set are O(1) on average
SPACE COMPLEXITY: O(n)  because the dict can hold up to n different numbers

MISTAKES I MADE:
- Didn't understand nested loops at first. Learned them by writing the brute-force
  version (for i ..., for j in range(i + 1, n) ...) before the dict version.

KEY INSIGHT:
- Each new copy of a number pairs with ALL earlier copies of it. Count the earlier
  copies in a dict, add that count BEFORE recording the current one.
"""
