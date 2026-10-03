# Day 03: Time & space complexity (Big O)

Problems: 1295, 268, 136

## 1. What is Big O?

Big O tells you **how the work grows when the input grows**. It's not about seconds.
`n` = size of the input (e.g. length of the list).

| Big O | Name | In simple words | Example |
|---|---|---|---|
| O(1) | constant | same work no matter how big n is | `nums[0]`, `d[key]` |
| O(log n) | logarithmic | cut the problem in half each step | binary search |
| O(n) | linear | touch each item once | one `for` loop |
| O(n log n) | linearithmic | a good sort | `sorted(nums)` |
| O(n^2) | quadratic | for each item, look at every item | nested loops |

For n = 1,000,000: O(log n) ≈ 20 steps, O(n) = 1 million, O(n^2) = 1 trillion (too slow).

## 2. Rules

1. **Drop constants.** O(2n) -> O(n). O(n / 2) -> O(n). O(500) -> O(1).
2. **Keep the biggest term.** O(n^2 + n) -> O(n^2). O(n + log n) -> O(n).
3. **Nested loops multiply.**
   ```python
   for i in range(n):       # n times
       for j in range(n):   # n times each
           ...              # -> n * n = O(n^2)
   ```
4. **Separate loops add.**
   ```python
   for x in nums: ...   # O(n)
   for x in nums: ...   # O(n)
   # O(n) + O(n) = O(2n) = O(n)
   ```
5. Different inputs get different letters: loop over `a` then `b` -> O(a + b);
   nested -> O(a * b).

## 3. Hidden loops

Some one-liners are loops in disguise. Each costs O(n) on a list:

- `x in my_list`
- `sum(nums)`, `max(nums)`, `min(nums)`
- `nums.count(x)`, `nums.index(x)`
- `nums[a:b]` (copies the slice), `nums + nums`

Put one inside a loop and it becomes O(n^2):

```python
for i in range(n):
    total = sum(nums)   # O(n) inside O(n) -> O(n^2)  ❌
total = sum(nums)       # once, outside -> O(n)       ✅
```

This was my mistake in LC 268.

## 4. Space complexity

**Extra memory** the algorithm uses as the input grows (not counting the input itself).

- A few variables (`count`, `i`, `total`) -> **O(1)**
- A new list / dict / set that can grow with n -> **O(n)**
- An n x n grid -> **O(n^2)**

Often there's a trade-off: use O(n) extra space (a dict) to save time.

## 5. List vs dict lookup

| Question | List | Dict / Set |
|---|---|---|
| `x in ...` | O(n): checks one by one | O(1) average: jumps by hash |
| get by position | `nums[i]` O(1) | no positions |
| get by key | no keys | `d[key]` O(1) average |

If you're asking "have I seen x?" many times, use a dict or set, not a list.

## 6. Python operations cost table

| Operation | Cost |
|---|---|
| `nums[i]`, `nums[i] = x` | O(1) |
| `len(nums)` | O(1) |
| `nums.append(x)` | O(1) |
| `nums.pop()` (last) | O(1) |
| `nums.pop(0)`, `nums.insert(0, x)` | O(n): everything shifts |
| `x in nums` | O(n) |
| `nums.count(x)`, `nums.index(x)` | O(n) |
| `sum`, `max`, `min` | O(n) |
| `nums[a:b]` | O(b - a) |
| `nums + other` | O(n + m) |
| `sorted(nums)`, `nums.sort()` | O(n log n) |
| `d[key]`, `d[key] = v`, `d.get(key)` | O(1) average |
| `key in d`, `x in some_set` | O(1) average |
| `s.replace`, `s.split`, `"".join(parts)` | O(n) |
| `str(num)`, `len(s)` | O(digits), O(1) |

## 7. Today's problems through the Big O lens

| Problem | Time | Space | Note |
|---|---|---|---|
| 1295 Even digits | O(n) | O(1) | `len(str(num))` is tiny per number |
| 268 Missing number | O(n) | O(1) | two separate O(n) parts add up; `sum` must stay outside the loop |
| 136 Single number | O(n) | O(n) | dict; XOR version gets O(1) space |

## Key takeaway

Count the loops, including the hidden ones. Nested multiplies, separate adds, drop
constants, keep the biggest term.
