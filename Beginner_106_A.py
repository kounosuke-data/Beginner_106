#a, bを数値として受け取る
a, b = map(int, input().split())

#道を入れた面積を計算→その後道の分だけ引く
print(a*b - (a+b-1))