while True:
    print("--------【闰年,平年】计算--------")
    year = int(input("输入一个年份: "))
    if (year % 4) == 0:
        print(year,"是闰年")       # 非整百年能被4整除的为闰年
    elif (year % 100) == 0 and (year % 400) == 0:
        print(year,"是闰年")   # 整百年能被400整除的是闰年
    else:
        print(year,"不是闰年")
    




