# coding = utf-8
#猜数字游戏
import random
'''
print(random.Random())
print(random.randint(100,186))
'''
number = random.randint(1,10)#生成1到10随机整数
number1 = input("请输入一个1到10整数：")

if number == number1:
	print('恭喜你，猜中了!')
else:
	print('遗憾告诉你，猜错了！')
