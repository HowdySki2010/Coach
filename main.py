# start_tss = int(input("What is the starting TSS? "))
#
# ramp_rate = int(input("How many percent gain per week? "))
#
# rest_percentage = int(input("How many percent decrease in rest week? "))
#
# season_length = int(input("How long should the block be in months? "))
#
# block_length = int(input("How often do you want rest weeks? Every ?? weeks? "))

# rest_day = input("On which day would you like your rest day? Please use the whole day name: ").upper()
from weekly_per_2 import week_per
import calendar


start_tss = 200
ramp_rate = 10
rest_percentage = 50
season_length = 1
block_length = 4
rest_day = 'MONDAY'

tss_outline = [start_tss]

for i in range(0, ((season_length * block_length-1) - season_length)):
    weekly_tss = round(tss_outline[i] * ((100 + ramp_rate)/100))
    tss_outline.append(weekly_tss)

for j in range(1, season_length+ 1):
    tss_outline.insert((j * block_length)-1, (tss_outline[j * block_length-2]*(100-rest_percentage)/100))

for i in tss_outline:
    print(week_per(i, rest_day))




# rest_day()

