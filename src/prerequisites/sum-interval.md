# Find the Sum of the Numbers in a Given Interval

- Formula: `Sum = ((Number of terms) * (First term + Last term)) / 2`.

    Where:

    - **Number of terms** = `num2 - num1 + 1`
    - **First term** = `num1`
    - **Last term** = `num2`

    So:

    `Sum from num1 to num2 = ((num2 − num1 + 1) * (num1 + num2)) / 2`.

  >>  💡
  >> - This formula works for **any consecutive interval**, positive or negative numbers.
  >> - Efficient formula: **O(1) time**, no need to loop.

```py
  ## FORMULA BASED "SUM"
  # Sum of numbers in a given interval [num1, num2]
  num1 = 5
  num2 = 15

  # Approach 1: Using float division and converting to int
  # sum_interval = int(((num2 - num1 + 1) * (num1 + num2)) / 2)
  # Approach 2 (preferred): Using integer division "//"
  # sum_interval = (num2 - num1 + 1) * (num1 + num2) // 2
  # - Multiplying first and then dividing ensures correct integer result for any interval
  # - Avoids potential rounding issues from float division
  sum_interval = int(((num2 - num1 + 1) * (num1 + num2)) / 2)

  print(f"Sum of numbers from {num1} to {num2} is: {sum_interval}")
```

```py
## RECURSION BASED "SUM"
def recursum(num1, num2) -> int:
    if num1 > num2:  # Base case: empty interval
        return 0
    return num1 + recursum(num1 + 1, num2)  # Add current number and recurse

num1, num2 = 5, 15
print("Sum:", recursum(num1, num2))
```

>> 💡 Recursion Time & Space complexity:
>> - Time complexity: **O(num2 - num1 + 1)** → linear in the number of terms
>> - Space complexity: **O(num2 - num1 + 1)** → call stack of recursive calls

```py
## "For" loop BASED "SUM"
num1, num2 = 5, 15
sum_interval = 0
for i in range(num1, num2 + 1):
  sum_interval += i
print(sum_interval)
```


>> 💡
>> “**For**” loop Time & Space complexity:
>>
>> - Time complexity: **O(num2 - num1 + 1):**
>>     - The loop **iterates once for each number in the interval**.
>>     - Number of iterations = `(num2 - num1 + 1)` → total numbers from `num1` to `num2`.
>>     - Each iteration does **one addition**.
>>
>>              **Time complexity = O(num2 − num1 + 1)**
>>
>>     - Example: `[5, 15]` → 11 iterations
>>     - Example: `[1, 1,000,000]` → 1 million iterations → linear time in the number of terms
>>
>>     ✅ Linear time because the **number of steps grows with interval size**.
>>
>> - Space complexity: **O(1):**
>>     - We only use **a few variables**:
>>         - `sum_interval` → stores the running total
>>         - `i` → loop variable
>>     - **No extra memory grows with input size**
>>
>>                 **Space complexity = O(1)**
>>
>>     - Independent of `(num2 - num1 + 1)`
>>     - Compare with recursion, where **each function call uses stack memory** → O(num2 - num1 + 1)
>>
>> # Note:
>>
>> In Big O notation for space complexity:
>>
>> - Constant variables like `num1`, `num2`, `sum_interval` are ignored
>> - Loop variables like `i` are also ignored, because they occupy fixed memory
>> - Only memory that grows with `input size` (like arrays or recursion stack) affects space complexity
>>
>> Therefore, for this loop:
>>
>> # num1, num2 = 5, 15
>>
>> # sum_interval = 0
>>
>> # for i in range(num1, num2 + 1):
>>
>> # sum_interval += i
>>
>> Space complexity = **O(1)**
>>
>> # Constant vs Growing Memory Examples
>>
>> # Constant variables (O(1) space)
>>
>> ```py
>> num1 = 5
>> num2 = 15
>> sum_interval = 0
>> i = 0  # loop variable
>> ```
>>
>> - Memory usage does NOT grow with input size
>> - Example: `num1`, `num2`, `sum_interval`, `i` always occupy same fixed memory → O(1)
>>
>> # Memory that grows with input size (O(n) space)
>>
>> ```py
>> n = 5 # input size — the number of elements you want to store in `arr`.
>> arr = []
>> for i in range(n):
>>     arr.append(i)
>> ```
>> - Memory usage grows as n increases
>> - Example: arr has 5 elements for n = 5, 100 elements for n = 100 → O(n)

