day_sum = 0
month = int(input("请输入月份："))
year = int(input("请输入年份："))
day = int(input("请输入今天的日期："))
for a in range(8,13):
    if a==2:
        if (2007%4==0) and (2007%100!=0) or (2007%400==0):
            day_sum +=29
        else:
            day_sum +=28
    elif a == 4 or a == 6 or a == 9 or a == 11: 
        day_sum +=30
    else:
        day_sum +=31
day_sum +=26
#1900年--(year-1)年12月31日
for i in range(2008,year):
    if(i%4==0) and (i%100!=0) or (i%400==0):
        day_sum +=366
    else:
        day_sum +=365
#1900年1月1日--year年month月的天数
for a in range(1,month):
    if a==2:
        if (year%4==0) and (year%100!=0) or (year%400==0):
            day_sum +=29
        else:
            day_sum +=28
    elif a == 4 or a == 6 or a == 9 or a == 11: 
        day_sum +=30
    else:
        day_sum +=31
day_sum += day
print("2007年7月26日到",year,"年",month,"月一共有",day_sum,"天")
                
