# ミュータブル
import math

data1 = [1, 2, 3]
data2 = data1
data1[0] = 100

print(data1)
print(data2)

# イミュータブル
x = 1
y = x
x += 10

print(x)
print(y)

# ミュータブル型で値そのものを変更した場合全く別のものになる
data1 = [1, 2, 3]
data2 = data1
data1 = [2, 3, 4]

print(data1)
print(data2)

# アンパック代入
data = [1, 2, 3, 4, 5]
a, b, c, d, e, = data
print(a, b, c, d, e)

# 残りの要素をまとめて代入する
del data
data = [2, 3, 4, 5, 6, 7, 8]
m, n, *o, = data
print(m, n, *o)
print(o)

# 一部のデータを切り捨てる
del data
data = [2, 3, 4, 5, 6, 7]
a, _, b, c, d, e = data

# 変数のスワッピング
x = 15
y = 30
x, y = y, x
print(x, y)

# セイウチ演算子（かわいい）
z = (x := 20 / 10)

# 小数点第5位までの精度を保証する
EPSILON = 0.00001
del x, y
x = 0.2 * 3
y = 0.6
print(abs(x - y) < EPSILON)

# 近似比較
print(math.isclose(0.2 * 3, 0.6))

# 値が空か判定
del x, y, z

x = None
y = 'abc'
z = 1 + 5j

# Noneは==を使うべきではない（左オペランドの型によって結果が変化する可能性がある）
print(x == None)

# Noneはisで比較する
print(x is None)

# print文の中でif文使える
score = 75
print('合格' if score >= 75 else '不合格')

# 比較演算子の連結
del x
x = 20
print(5 <= x <= 30)

# if文
x = 30
if x == 30:
    print("30です")

if x != 30:
    print("30ではありません")
print("if文の外")

# if-elif-else文
# if(..)にしたくなるけど括弧がいらない、インデントすごく重要
# 実行されるのは最初に条件に合致した1つだけ
del x
x = 100

if x == 10:
    print("xは10です")
elif x < 10:
    print("xは10より小さい")
else:
    print("それ以外")

# 多重if文
# if文の外側
x = 11
if x == 10:

    # if文の内側
    if x is None:
        print("xは存在しません")
    elif x == 10:
        print("xは10です")
    else:
        print("？")

else:
    print("内側のループは通りません")

# if文で複数の条件式がある場合
del x
x = 10
y = 11
z = 12
if (x == 10
        and y == 11
        and z == 12):
    print("複数の条件式がある場合括弧で囲んでも良い。")

# if文でbooleanで比較する場合
# ==で比較しないところが重要
boo = True

if boo:
    print("Trueです")
if not boo:
    print("Falseです")

# 複数の条件（特に否定＋論理演算子の組み合わせの場合、ド・モルガンの法則をつかえる）
del boo
boo = False
foo = False

if not boo and not foo:
    print("ド・モルガンの法則をつかっていない")

if not (boo or foo):
    print("ド・モルガンの法則を使った場合")

# while：条件がTrueの間処理を続ける
i = 1
while i < 5:
    print(f'{i}番目のループです')
    i += 1

# for文
# リスト内を順に処理する
# イテラブル型に分類できるものはすべてfor文で回すことができる

data = ["apple", "lemon", "strawberry"]
for value in data:
    print(value)

# 通常のfor文
# range関数はm以上n未満の整数リストを生成する
del i
i = 1
for i in range(1, 6):
    print(f'{i}')

# 10までの整数リストを生成する
i = list(range(0, 7, 2))

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data2 = [i * 2 for i in data]
data2 = [str(i) for i in data2]
print(data2)

data_sum = [i * 2 for i in data]
data_str_sum = sum([i * 2 for i in data])
print(data_str_sum)

# break文（if文と一緒に使うのが普通）
# if文の条件を満たすとfor文を抜ける処理をかける
del i
i = 0
sum_num = 0

for i in range(10):
    sum_num += i
    if i > 6:
        break

print(sum_num)

# continue文
# 1から10までの偶数の数を全て足した数を出力する
del sum_num
sum_num = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue
    sum_num += i
print(sum_num)

# 例外処理
num = 0
try:
    num = input('数字を入力してください')
    print('2倍すると', int(num)*2)
except (ValueError, TypeError) as ex:
    print(f'error {ex}')
