#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_number = abs(number) % 10

sentence = str("")

if last_number > 5:
    sentence = "and is greater than 5"
elif last_number == 0:
    sentence = "and is 0"
else:
    sentence = "and is less than 6 and not 0"

print("Last digit of {}".format(number), "is {}".format(last_number), sentence)
