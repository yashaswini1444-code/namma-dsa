"""
Problem   : LC 412 - Fizz Buzz
Link      : https://leetcode.com/problems/fizz-buzz/
Difficulty: Easy
Pattern   : Loops + conditions
Status    : Solved with hint

APPROACH (in my own words, written BEFORE coding):
1. Create an empty list called answer.
2. Loop i from 1 to n.
3. If i is divisible by both 3 and 5 -> add "FizzBuzz"
   elif divisible by 3 -> add "Fizz"
   elif divisible by 5 -> add "Buzz"
   else -> add str(i)
4. After the loop, return answer.

DRY RUN (n = 5):
i=1 -> "1", i=2 -> "2", i=3 -> "Fizz", i=4 -> "4", i=5 -> "Buzz"
Output: ["1","2","Fizz","4","Buzz"]
"""


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:   # divisible by both 3 and 5
                answer.append("FizzBuzz")
            elif i % 3 == 0:                # divisible by 3
                answer.append("Fizz")
            elif i % 5 == 0:                # divisible by 5
                answer.append("Buzz")
            else:
                answer.append(str(i))       # the number as a string

        return answer


# ---------------- Local tests ----------------
if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(15))
    # expected: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz',
    #            '11', 'Fizz', '13', '14', 'FizzBuzz']


"""
TIME COMPLEXITY : O(n)  because the loop runs once for each number from 1 to n
SPACE COMPLEXITY: O(n)  because the answer list stores n strings
                  (O(1) extra space if we don't count the output list)

MISTAKES I MADE:
- Checked divisibility on n instead of i (n is fixed, i is the current number)
- Checked "divisible by 3" before "both" -> 15 would wrongly become "Fizz"
- Wrote 'i' (the letter) instead of str(i) (the value as text)
- Planned to return inside the loop -> must append, then return after the loop

KEY INSIGHT:
- Check the most specific condition first; % n == 0 means "divisible by n"
"""