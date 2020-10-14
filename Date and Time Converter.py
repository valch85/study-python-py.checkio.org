"""
# first solution
from datetime import datetime


def date_time(time: str) -> str:
    # convert string to datetime format
    temp_date = datetime.strptime(time, "%d.%m.%Y %H:%M")

    if temp_date.hour == 1:
        hhh = " hour "
    else:
        hhh = " hours "
    if temp_date.minute == 1:
        mmm = " minute"
    else:
        mmm = " minutes"

    # convert to correct output month format
    #month_correct = temp_date.strftime("%B %Y")
    return(str(temp_date.day) + " " + month_correct + " year " + str(temp_date.hour) + hhh + str(temp_date.minute) + mmm)
"""


# second solution
from datetime import datetime


def date_time(time: str) -> str:
    # convert string to datetime format
    temp_date = datetime.strptime(time, "%d.%m.%Y %H:%M")
    # convert to correct output month format
    month_correct = temp_date.strftime("%-d %B %Y year %-H hour" + 's' * (temp_date.hour != 1) + ' %-M minute' + 's' * (temp_date.minute != 1))
    return month_correct



"""
# third solution
import time as tm


def date_time(time: str) -> str:
    time = tm.strptime(time, '%d.%m.%Y %H:%M')
    timestring = tm.strftime('%-d %B %Y year %-H hour' + 's' * (time.tm_hour != 1) + ' %-M minute' + 's' * (time.tm_min != 1), time)
    print(timestring)
"""

date_time("01.01.2000 00:00") #== "1 January 2000 year 0 hours 0 minutes", "Millenium"
date_time("09.05.1945 06:30") #== "9 May 1945 year 6 hours 30 minutes", "Victory"
date_time("20.11.1990 03:55") #== "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
