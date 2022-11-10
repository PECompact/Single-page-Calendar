day_sum = 0
#1900年--2019年12月31日
for i in range(1900,2020):
    if(i%4==0) and (i%100!=0) or (i%400==0):
        day_sum +=366
    else:
        day_sum +=365
#2020年1月1日--2020年9月30日的天数
for month in range(1,10):
    if month==2:
        if (2020%4==0) and (2020%100!=0) or (2020%400==0):
            day_sum +=29
        else:
            day_sum +=28
    elif month == 4 or month == 6 or month == 9 or month == 11: 
        day_sum +=30
    else:
        day_sum +=31
day_sum +=1
print(day_sum)
                

        
