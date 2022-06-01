def sum_digits(value):
    res = 0

    while value != 0:
        res += value % 10
        value //= 10

    return res


arr = [i**3 for i in range(1, 1001, 2)]

variant_a= sum(filter(lambda num: sum_digits(num) % 7 == 0, arr))
variant_b= sum(filter(lambda num: sum_digits(num + 17) % 7 == 0, arr))

print(variant_a)
print(variant_b)