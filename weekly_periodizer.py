tss_outline = [100, 110, 121, 60.5, 133, 146, 161, 80.5]
import calendar

def week_per(weekly_tss):
    daily_per = (0, 20, 15, 5, 20, 10, 30)
    daily_tss = [100, 100, 100, 100, 100, 100, 100]
    for i in range(0, 7):
        daily_tss[i] = round((daily_per[i]/100) * weekly_tss)

    for i in range(0, 7):
        if daily_tss[i] < 15:
            daily_tss[i + 1] += daily_tss[i]
            daily_tss[i] = 0

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

    for i in range(0, 7):
        weekday_tss[week_list[i]] =daily_tss[i]

    print(weekday_tss)

# week_per(100)

# print(week_per(200))