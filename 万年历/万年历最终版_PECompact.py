import sys
while True:
    begin = input("是否进入（yes or other buttons）")
    if begin == "yes":
        year_in = int(input("请输入年份"))
        month_in = int(input("请输入月份"))
        sum_day = 0
        month_sumDay = 0
        for year in range(1900,year_in):#计算1900年1月1日~(year_in-1)年12月31日
            if (year%4==0 and year%100!=0) or (year%400==0):
                sum_day += 366
            else:
                sum_day +=365
        for month in range(1,month_in):#计算完1月1日~(month-1)月30日
            if month == 2:
                if (year_in%4==0 and year_in%100!=0) or (year_in%400==0):
                    sum_day +=29
                else:
                    sum_day+=28
            elif month == 4 or month == 6 or month ==9 or month == 11:
                sum_day += 30
            else:
                sum_day += 31
        sum_day+=1#加上month月1日当天

        week = sum_day%7

        if month_in == 2:
            if (year_in % 4 == 0 and year_in % 100 != 0) or (year_in % 400 == 0):
                month_sumDay = 29
            else:
                month_sumDay = 28
        elif month_in == 4 or month_in == 6 or month_in == 9 or month_in == 11 :
            month_sumDay = 30
        else:
            month_sumDay = 31

        print("\t\t",year_in,"年",month_in,"月")
        print("日\t一\t二\t三\t四\t五\t六")
        for i in range(0,week):
            print(end = "\t")
        for day in range(1,month_sumDay+1):
            print(day,end = "\t")
            if sum_day%7 == 6:
                print()
            sum_day +=1
        print("开发者：PECompact\n感谢你的使用！\n")
    elif begin == "wyx" or begin == "520" or begin == "5201314" or begin == "金丫丫":
        print("Love you")
    else:
        sys.exit()