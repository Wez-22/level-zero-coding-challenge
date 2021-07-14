def number_to_time_converter(x):
    time_hour = int(x / 60)
    time_minute = x % 60
    if (time_hour > 1 or time_hour == 0) and (time_minute > 1 or time_minute == 0):
        print(str(time_hour) + " hours, " + str(time_minute) + " minutes")
    elif time_hour == 1 and time_minute == 1:
        print(str(time_hour) + " hour, " + str(time_minute) + " minute")
    elif (time_hour > 1 or time_hour == 0) and time_minute == 1:
        print(str(time_hour) + " hours, " + str(time_minute) + " minute")
    else:
        print(str(time_hour) + " hour, " + str(time_minute) + " minutes")


number_to_time_converter(133)
