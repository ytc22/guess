import random
# 都有空格 why
r = random.randint(1, 100)
count = 0 #要用一個計數基礎
while True:
	# 且count = 0 不能寫在while內，因為每重複一次就等於把計數歸零
	count += 1 # count = count + 1
    num = input('請猜數字：') # num = number縮寫
    num = int(num) # casting 型別轉換
    # 因為input會存成字串，要改整數
    if num == r:
        print('你猜中了！')
        # try: print('你猜了', count,'次') 重複性太高，不好
        break
    elif num > r:
        print('比答案大')
        # try: print('你猜了', count,'次')
    elif num < r:
        print('比答案小')
        # try: print('你猜了', count,'次')
    print('這是你猜的第', count,'次')
    # 但這樣猜中的時候就不會說猜幾次了!因為猜中下面馬上是break
    # 若要猜中也印出，就在猜中print下面加一句