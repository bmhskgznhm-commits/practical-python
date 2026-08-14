# bounce.py
#
# Exercise 1.5


drop_height = 100  # Meters
bounce_ratio = 0.6  # 60% of the previous height
print(f'The initial drop height is {drop_height} meters.')
print(
    f'Each time the ball bounces it reaches {bounce_ratio * 100}% of the previous height')


for i in range(10):
    drop_height = drop_height * bounce_ratio
    print(round(drop_height, 4))


# Solution Example:

# height = 100
# bounce = 1
# while bounce <= 10:
#     height = height * (3/5)
#     print(bounce, round(height, 4))
#     bounce += 1
