def sun_angle(time):
    h, m = map(int, time.split(':'))
    #One hour is 15 degrees (= 360 / 24) and one minute is 0.25 degrees (= 360 / (24 * 60))
    angle = 15 * h + m * 0.25 - 90
    #return angle if 0 <= angle <= 180 else "I don't see the sun!"

    if 0 <= angle <= 180:
        return angle
    else:
        return "I don't see the sun!"


sun_angle("07:10") #== 15
sun_angle("01:23") #== "I don't see the sun!"


