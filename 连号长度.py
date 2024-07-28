s = input("Enter Num：")
g = list(s)
n = len(s)
k = [1] + [int(x) + 1 for x in g]
G = []
h, y, p, q = 1, 1, 0, 0
for i in range(1, n):
    if int(g[i]) is k[i - q]:
        y += 1
        G.append(y)
    else:
        p = 1
        if p == 1:
            k.pop(i - q)
            q += 1
            p = 0
        y = 1

G.sort(reverse=True)
print(G[0])
