# start_tss = int(input("What is the starting TSS? "))
#
# ramp_rate = int(input("How many percent gain per week? "))
#
# rest_percentage = int(input("How many percent decrease in rest week? "))
#
# season_length = int(input("How long should the block be in months? "))
#
# block_length = int(input("How often do you want rest weeks? Every ?? weeks? "))

start_tss = 100
ramp_rate = 10
rest_percentage = 50
season_length = 2
block_length = 4

tss_outline = [start_tss]

for i in range(0, ((season_length * block_length-1) - season_length)):
    weekly_tss = round(tss_outline[i] * ((100 + ramp_rate)/100))
    tss_outline.append(weekly_tss)

for j in range(1, season_length+ 1):
    tss_outline.insert((j * block_length)-1, (tss_outline[j * block_length-2]*(100-rest_percentage)/100))
print(tss_outline)

for i in tss_outline:
    print(i)
