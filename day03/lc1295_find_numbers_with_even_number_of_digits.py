"""
Problem   : LC 1295 - Find Numbers with Even Number of Digits
Link      : https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
Difficulty: Easy
Pattern   : Counter variable
Status    : Solved alone (typed it myself)

APPROACH (in my own words, written BEFORE coding):
1. Start with count = 0.
2. For each number, turn it into a string. The string's length = number of digits.
3. If the number of digits is even (digits % 2 == 0) -> count += 1.
4. After the loop, return count.

DRY RUN (nums = [12,345,2,6,7896]):
12   -> "12"   -> 2 digits -> even -> count = 1
345  -> "345"  -> 3 digits -> odd  -> count = 1
2    -> "2"    -> 1 digit  -> odd  -> count = 1
6    -> "6"    -> 1 digit  -> odd  -> count = 1
7896 -> "7896" -> 4 digits -> even -> count = 2
Output: 2
"""


class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            digits = len(str(num))
            if digits % 2 == 0:
                count += 1
        return count


# ---------------- Local tests ----------------
if __name__ == "__main__":
    s = Solution()
    print(s.findNumbers([12, 345, 2, 6, 7896]))   # expected: 2
    print(s.findNumbers([555, 901, 482, 1771]))   # expected: 1


"""
TIME COMPLEXITY : O(n)  because one loop over n numbers; str(num) is O(1) here since
                        every number has at most 6 digits (nums[i] <= 10^5)
SPACE COMPLEXITY: O(1)  because only count and digits (a tiny temporary string)

MISTAKES I MADE:
- None. Typed it myself and it passed.

KEY INSIGHT:
- len(str(num)) is the easiest way to count digits of a positive number.
  Even check = % 2 == 0.
"""
