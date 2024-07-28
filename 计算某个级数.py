########### y=1-1/2+1/3-1/4...±1/n
def factorial(n):
    "定义阶乘"
    result = 1
    match n:
        case 0:
            return 1
        case _ if n > 0:
            for b in range(1, n + 1):
                result *= b
            return result
        case _:
            return


k = int(input("Enter n:"))


def nuy(p):
    "定义运算"
    ans = 0
    if p == 0:
        return 0
    elif p % 2 == 0:
        for i in range(p + 1):
            a = factorial(2 * i)
            b = factorial(2 * (i + 1))
            ans += a / b
        return ans
    elif p == 1:
        return 1
    else:
        for i in range(p):
            c = factorial(2 * i)
            d = factorial(2 * (i + 1))
            ans += c / d
        return ans + 1 / k


p = nuy(k)
print(p)
