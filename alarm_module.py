import datetime


def set_alarm(atime):
    alarm_time = str(datetime.datetime.now().strptime(atime,'%I:%M %p'))  # output comes with time
    alarm_time = alarm_time[11:-3]
    print(alarm_time)
    hour = int(alarm_time[:2])
    minutes = int(alarm_time[3:5])
    return alarm_time, hour, minutes


# print(string)