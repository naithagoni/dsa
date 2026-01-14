# Check Whether a Number is Even or Odd
```py
def isEven(num: int) -> str:
	if (num % 2 == 0):
		return "Given Number is Even"
	else:
		return "Given Number is Odd"
print(isEven(10))
```

```py
# Using Bitwise Operator
def is_even(num: int) -> bool:
	# Explanation:
		# num & 1 → performs a bitwise AND between num and 1
		#   - 1 in binary is 00000001, so it only isolates the least significant bit (LSB)
		## What is LSB?
			# Every integer is stored in binary in computers.
			# Example: 12 in binary (8-bit representation) → 00001100
			# Bit positions: 7 6 5 4 3 2 1 0
			# Binary:        0 0 0 0 1 1 0 0
			# - LSB = Least Significant Bit → the rightmost bit (position 0)
			# - MSB = Most Significant Bit → the leftmost bit (highest place value)

		## How num & 1 uses LSB

			# & = bitwise AND
			# 1 in binary = 00000001 → only the LSB is 1, others 0

			## Examples
			# num = 12  # 00001100
			# num & 1   # 00001100 & 00000001 = 00000000 → 0

			# num = 7   # 00000111
			# num & 1   # 00000111 & 00000001 = 00000001 → 1

		# not (num & 1) → "not" converts the result to a boolean:
		#   - If LSB = 0 → not 0 → True  → number is even
		#   - If LSB = 1 → not 1 → False → number is odd
    return not (num & 1)

num = 12
print("Even" if is_even(num) else "Odd")
```
