import calendar
from weekly_per_2 import week_per

trying = True
while trying:
    rest_day = input("On which day would you like your rest day? Please use the whole day name: ").upper()
    if rest_day == 'MONDAY':
        day_num = calendar.MONDAY
        trying = False
    elif rest_day == 'TUESDAY':
        day_num = calendar.TUESDAY
        trying = False
    elif rest_day == 'WEDNESDAY':
        day_num = calendar.WEDNESDAY
        trying = False
    elif rest_day == 'THURSDAY':
        day_num = calendar.THURSDAY
        trying = False
    elif rest_day == 'FRIDAY':
        day_num = calendar.FRIDAY
        trying = False
    elif rest_day == 'SATURDAY':
        day_num = calendar.SATURDAY
        trying = False
    elif rest_day == 'SUNDAY':
        day_num = calendar.SUNDAY
        trying = False
    else:
        print("Sorry, please enter a full day of the week")
        trying = True

calendar.setfirstweekday(day_num)

cal = calendar.weekheader(3)
week_list = cal.split()

weekday_tss = {}

daily_load = week_per(200)

for i in range(0, 7):
    weekday_tss[week_list[i]] =daily_load[i]

print(weekday_tss)


