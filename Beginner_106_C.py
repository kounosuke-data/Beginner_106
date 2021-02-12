#s, kを入力として受け取る
s = str(input())
k = int(input())

#1じゃなかったらその数値をだす
for i in range(len(s)):
    if s[i] != "1":
        print(s[i])
        exit()
    elif s[i] == "1" and k == i+1:
        print("1")
        exit()
    else:
        continue