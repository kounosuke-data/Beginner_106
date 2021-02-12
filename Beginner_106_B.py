#nを数値として受け取る
n = int(input())

#約数を列挙する
def divisor(x): 
    i = 1
    table = []
    while i * i <= x:
        if x%i == 0:
            table.append(i)
            table.append(x//i)
        i += 1
    table = list(set(table))
    return table


cntlist = []

#105以下は0、それ以外は奇数か確認し、約数の数が8つだったらリストに入れる
if n < 105:
    print(0)
    exit()
else:
    for i in range(105, n+1):
        if i%2 == 1:
            if len(divisor(i)) == 8:
                cntlist.append(i)
print(len(cntlist))