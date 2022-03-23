# test
import random
r = random.randint(1, 100)
# "." 是 "的"的意思
# randint = random int產生隨機整數
# (start, end)數值，且包含本數
while True:
    ans = input('請輸入數字：') # input
    ans = int(ans)
    if ans == r:
        print('恭喜答對！')
        break
    elif ans > r:
        print('答案比這個數字小哦!')
    elif ans < r:
        print('答案比這個數字大哦!')


# ans
import random
# 都有空格 why
r = random.randint(1, 100)
while True:
    num = input('請猜數字：') # num = number縮寫
    num = int(num) # casting 型別轉換
    # 因為input會存成字串，要改整數
    if num == r:
        print('你猜中了！')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')