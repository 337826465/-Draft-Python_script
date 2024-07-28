#####从可迭代对象中分解元素（解包）

# 可迭代对象均可被分解
# 但变量的总数要与源对象元素个数均等
# 也可使用形参替代变量
# 注："_"为Python通配符

T = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def drop(a):
    first, *middle, last = a
    return print(middle)


drop(T)

##使用match语句解包赋值
# 可用于根据字面值来绑定变量

for i in range(10):
    match (T[i]):
        case 1:
            print(f"1st={1}", end="   ")
        case 2:
            print(f"2nd={2}", end="   ")
        case 3:
            print(f"3rd={3}", end="   ")


################################
