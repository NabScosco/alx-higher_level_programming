#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit > 5:
    l_string = "and is greater than 5"
elif last_digit == 0:
    l_string = "and is 0"
elif last_digit < 6 and not 0:
    l_string = "and is less than 6 and not 0"
elif number < 0:
    last_digit = -1 * last_digit
print(F"Last digit of {number} is {last_digit} {l_string}")
