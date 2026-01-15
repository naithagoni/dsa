# Time: O(n × d)
# Space: O(1) (power array size is constant = 10)
def armstrongInRange(low: int, high: int):
    result = []

    for num in range(low, high + 1):
        s = str(num)
        d = len(s)

        # Precompute digit powers
        power = [i ** d for i in range(10)]

        total = 0
        for ch in s:
            total += power[int(ch)]

        if total == num:
            result.append(num)

    return result

print(armstrongInRange(150, 160))



# Time: O(n × d)
# Space: O(n) (recursion stack)
def armstrongRec(n: int, d: int) -> int:
    if n == 0:
        return 0
    return (n % 10) ** d + armstrongRec(n // 10, d)


def armstrongInRangeRec(low: int, high: int):
    result = []

    for num in range(low, high + 1):
        if num == armstrongRec(num, len(str(num))):
            result.append(num)

    return result

print(armstrongInRangeRec(150, 160))