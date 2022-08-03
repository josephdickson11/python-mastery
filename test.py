print(f"this is a new {2022} format")




def day_in_sec(day):
    SECS_IN_DAYS = 60 * 60

    result = day * SECS_IN_DAYS

    return f"total number of secs in {day} days is {result} seconds"

def day_in_mins(day):
    MINS_IN_DAYS = 60

    result = day * MINS_IN_DAYS

    return f"total number of minutes in {day} days is {result} minutes"

day = int(input("please, input the number of days: "))

print(day_in_mins(day))

print(day_in_sec(day))