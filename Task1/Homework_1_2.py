numbers = (i ** 3 for i in range(1, 1001, 2))

# функция подсчета суммы числа:
def sum_digits(value):
    sum = 0
    while value != 0:
        sum += value % 10
        value //= 10
    return sum

res = 0 # сумма кубов из списка, сумма цифр которых делится нацело на 7.
res17 = 0 # сумма кубов + 17 из списка , сумма цифр которых делится нацело на 7.
for i in numbers:
    if sum_digits(i) % 7 == 0:
        res += i
    if sum_digits(i + 17) % 7 == 0:
        res17 += i

print(res)
print(res17)


