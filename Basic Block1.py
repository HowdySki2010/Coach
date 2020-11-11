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

def block_outline(a, b, c, d, e):
    outline = [int(a*((101-b)/100))]
    week = 1
    while d > 0:
        for i in range(0, e ):
            if week % e ==0:
                weekly_tss = outline[week-1] 
                weekly_tss *= c/100
                outline.append(int(weekly_tss))
                week += 1
            else:
                weekly_tss = outline[week-1]
                weekly_tss *= (b + 100) / 100
                outline.append(int(weekly_tss))
                week += 1
        d -= 1
    outline.pop(0)

    print(outline)


block_outline(start_tss, ramp_rate, rest_percentage, season_length, block_length)








