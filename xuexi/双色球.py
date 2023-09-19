import random

def generate_red_balls(num_red_balls=6):
    # 从1到33中选取num_red_balls个红球
    red_balls = random.sample(range(1, 34), num_red_balls)
    return sorted(red_balls)

def generate_blue_ball():
    # 从1到16中选取1个蓝球
    blue_ball = random.randint(1, 17)
    return blue_ball

def generate_multiple_lottery_tickets(num_tickets=1):
    for i in range(num_tickets):
        red_balls = generate_red_balls()
        blue_ball = generate_blue_ball()
        print('红球：', red_balls, '蓝球：', blue_ball)

if __name__ == '__main__':
    generate_multiple_lottery_tickets(num_tickets=5)
