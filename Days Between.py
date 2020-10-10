import datetime


def days_diff(date1, date2):
    d1 = datetime.date(date1[0], date1[1], date1[2])
    d2 = datetime.date(date2[0], date2[1], date2[2])
    return abs(d1 - d2).days


if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
