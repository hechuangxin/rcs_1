import random

# 生成5个1至35之间不重复的随机数
def generate_red_balls():
    red_balls = random.sample(range(1, 36), 5)
    return sorted(red_balls)

# 生成2个1至12之间不重复的随机数
def generate_blue_balls():
    blue_balls = random.sample(range(1, 13), 2)
    return sorted(blue_balls)

# 打印一组彩票号码
def print_lottery_numbers(red_balls, blue_balls):
    print("红球：" + ' '.join(map(str, red_balls)) + "，蓝球：" + ' '.join(map(str, blue_balls)))

# 生成n注彩票号码
def generate_lottery_numbers(n):
    for i in range(n):
        red_balls = generate_red_balls()
        blue_balls = generate_blue_balls()
        print_lottery_numbers(red_balls, blue_balls)
        print()

# 生成3注彩票号码
generate_lottery_numbers(5)
