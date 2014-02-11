#!/usr/bin/env python

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == '__main__':

    non_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = non_leap_year[:]
    leap_year[1] += 1

    # 0 = monday, 6 = sunday
    current_day = 365 % 7
    sun_count = 0

    for year in range(1901, 2001):
        for days in (leap_year if is_leap_year(year) else non_leap_year):
            current_day += days
            sun_count += int(current_day % 7 == 6)
    print sun_count





