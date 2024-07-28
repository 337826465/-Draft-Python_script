##基础变量
A1 = int(input("输入范围起点："))
A2 = int(input("输入范围终点："))
A = [A1, A2]
B = int(input("输入模n："))
C = input("是否做加法（y或n）")
D = input("是否做乘法（y或n）")

a, b = A[0], A[1]
zone = range(a, b + 1)


# 以下为函定义
def parallel(a, b, n):  ##运算
    p = a - b
    if p % n == 0:
        return True
    else:
        return


def pa_class(a):  ##定义等价类
    p = []
    for i in zone:
        if parallel(i, a, B) is True:
            p.append(i)
    return p


#### pa_zone
if b - a <= 50:  ##当zone较小时，计算所有等价类集合
    K = {}
    for i in zone:
        K[str(i)] = [pa_class(x) for x in zone]


def pa_add(a, b):  ##定义加法
    if "K" in dir():
        c = K[str(a + b)]
    else:
        c = pa_class(a + b)
    return c


def pa_times(a, b):  ##定义乘法
    if "K" in dir():
        c = K[str(a * b)]
    else:
        c = pa_class(a * b)
    return c


##操作
if C.lower in ["yes", "y"]:
    L1 = int(input("请输入加数(a)"))
    L2 = int(input("请输入加数(b)"))
    print(f"输出：{pa_add(L1, L2)}")
if D.lower in ["yes", "y"]:
    M1 = int(input("请输入乘数(a)"))
    M2 = int(input("请输入乘数(b)"))
    print(f"输出：{pa_times(M1, M2)}")
