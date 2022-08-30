inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

def print_total_snow_fall(inches_snow):
    total_snow=0
    for i in inches_snow.values():
        total_snow=i+total_snow
    print('Total snowfall inches:', total_snow)

print_total_snow_fall(inches_snow)

thursday_snow=input("How many snow fell on Thursday?")

inches_snow["Thursday"]=int(thursday_snow)

print_total_snow_fall(inches_snow)