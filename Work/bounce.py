# bounce.py
#
# Exercise 1.5
# The origin high of the rubber ball
ORIGIN_HIGH = 100

# Calculate the the height of bounce.
def back_up_high(origin_high):
    return round(origin_high * 3 / 5, 4)


# Calculate the first 10 bounces
for i in range(10):
    ball_high = back_up_high(ORIGIN_HIGH)
    print(i+1, ball_high)
    ORIGIN_HIGH = ball_high
