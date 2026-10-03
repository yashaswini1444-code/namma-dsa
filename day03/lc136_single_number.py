"""
Problem   : LC 136 - Single Number
Link      : https://leetcode.com/problems/single-number/
Difficulty: Easy
Pattern   : Frequency map
Status    : Solved with hint

APPROACH (in my own words, written BEFORE coding):
1. Every number appears twice except one. Find that one.
2. Build a frequency map: count = {number: how many times it appears}.
3. Loop over the KEYS of count. The one with count 1 is the answer -> return it.

DRY RUN (nums = [4,1,2,1,2]):
build count:
4 -> {4:1}
1 -> {4:1, 1:1}
2 -> {4:1, 1:1, 2:1}
1 -> {4:1, 1:2, 2:1}
2 -> {4:1, 1:2, 2:2}
check keys:
4 -> count 1 -> return 4
Output: 4
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num in count:
            if count[num] == 1:
                return num


# ---------------- Local tests ----------------
if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2, 2, 1]))        # expected: 1
    print(s.singleNumber([4, 1, 2, 1, 2]))  # expected: 4
    print(s.singleNumber([1]))              # expected: 1


"""
TIME COMPLEXITY : O(n)  because two separate loops (build + check), each at most n
                        -> O(n) + O(n) = O(n)
SPACE COMPLEXITY: O(n)  because the dict holds about n / 2 + 1 keys

MISTAKES I MADE:
- Wrote "for count in nums" -> this REUSED the name count, overwrote my dict with
  a number, and looped over nums instead of the dict. Loop variable names must
  not clash with variables I still need.
- In a dry run I tallied {'a': 3} as {'a': 2} -> go slowly, +1 per occurrence.

KEY INSIGHT:
- Frequency map = "how many times does each thing appear?" in one pass.
- Alternative with O(1) space: XOR. a ^ a = 0 and a ^ 0 = a, so XOR-ing every
  number cancels all pairs and leaves only the single one
  (result = 0, then result ^= num for each num). LeetCode's follow-up asks for this.
"""
