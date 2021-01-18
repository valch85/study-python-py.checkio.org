""" With this mission I want to start a series of missions with light bulbs. They will help you understand the concept
of processes and evaluation of the processes’ performance. Instead of light bulbs, in real life, there may be
equipment, the effectiveness of which must be calculated, or workers who go to work, and their wages must be calculated.
The first mission is quite simple. There is a light bulb, which by default is off, and a button, by pressing which
the light bulb switches its state. This means that if the light bulb is off and the button is pressed, the light
turns on, and if you press it again, it turns off. """
from datetime import datetime
from typing import List


def sum_light(els: List[datetime]) -> int:
    temp = sorted(els, reverse=True)
    sum_temp = []
    for i in range(0, len(els), 2):
        sum_temp.append(((temp[i]) - (temp[i+1])).total_seconds())
    answer = sum(sum_temp)
    return answer


print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
]))# == 610˚

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
]))# == 1220

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
    datetime(2015, 1, 12, 11, 10, 10),
    datetime(2015, 1, 12, 12, 10, 10),
]))# == 4820

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 1),
]))# == 1

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 13, 11, 0, 0),
]))# == 86410
