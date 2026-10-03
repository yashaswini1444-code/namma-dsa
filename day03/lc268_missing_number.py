"""
Problem   : LC 268 - Missing Number
Link      : https://leetcode.com/problems/missing-number/
Difficulty: Easy
Pattern   : Math (expected sum - actual sum)
Status    : Solved with hint

APPROACH (in my own words, written BEFORE coding):
1. nums has n numbers taken from 0..n, so exactly one number is missing.
2. expected = 0 + 1 + 2 + ... + n (add every i in range(n + 1)).
3. actual = sum(nums), computed ONCE, outside the loop.
4. The missing number = expected - actual.

DRY RUN (nums = [3,0,1]):
n = 3
expected = 0 + 1 + 2 + 3 = 6
actual   = 3 + 0 + 1     = 4
6 - 4 = 2
Output: 2
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected = 0
        for i in range(n + 1):
            expected += i
        actual = sum(nums)
        return expected - actual


# ---------------- Local tests ----------------
if __name__ == "__main__":
    s = Solution()
    print(s.missingNumber([3, 0, 1]))                    # expected: 2
    print(s.missingNumber([0, 1]))                       # expected: 2
    print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # expected: 8


"""
TIME COMPLEXITY : O(n)  because the range loop is n + 1 steps and sum() is another
                        n steps -> separate loops ADD: O(n) + O(n) = O(n)
SPACE COMPLEXITY: O(1)  because only n, expected, actual, i

MISTAKES I MADE:
- Loop variable was num but I used i inside -> NameError. The name after "for"
  is the only name the loop creates.
- Used range(1, n) -> stops at n - 1, so n is never added. range(n + 1) gives 0..n.
- Put sum(nums) inside the loop -> sum() is itself a hidden O(n) loop, so it became
  O(n^2). Compute it once, outside.
- Returned actual - expected -> reversed, gives a negative number.
  expected is the bigger one, so expected - actual.

KEY INSIGHT:
- (what SHOULD be there) - (what IS there) = what is missing.
- Also: 0 + 1 + ... + n = n * (n + 1) // 2, so expected can be O(1) without a loop.
"""
