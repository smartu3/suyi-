#coding=utf-8

#示例条件判断代码
# floop = True
# while floop:
    # ninjianums = input('How many Narutos at the moment')
    # ninjianums = int(ninjianums)
    # if ninjianums >= 100:
        # print("Incredible!")
    # elif ninjianums >15 and ninjianums<100:
        # print("Great Ninjutsu")
    # elif ninjianums >5 and ninjianums<=15:
        # print("just so so")
    # else:
        # print("...")
    # print()


#体重练习
# height = 1.75
# weight = 80.5
# BMI = weight/(height**2)
# if BMI >=32:
    # print("严重")
# elif BMI >=25 and BMI <32:
    # print("过重")
# elif BMI >=18.5 and BMI <25:
    # print("正常")
# else:
    # print("过轻")


#while循环计算100以内奇数和
# sum = 0
# n = 99
# while n > 0:
    # sum = sum + n
    # n = n - 2
# print(sum)
# #同理，使用for 循环也可以
# sum = 0
# for i in range(100):
    # if i%2 != 0:
        # sum += i
# print(sum)


#continue语句
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
#break语句
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')