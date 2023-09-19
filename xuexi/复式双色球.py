import random

def generate_red_balls(num_red_balls=6, num_choices=33):
    # 从1到num_choices中选取num_red_balls个红球
    red_balls = random.sample(range(1, num_choices+1), num_red_balls)
    return sorted(red_balls)

def generate_blue_ball(num_choices=16):
    # 从1到num_choices中选取1个蓝球
    blue_ball = random.randint(1, num_choices+1)
    return blue_ball

def generate_lottery_ticket(num_red_balls=6, num_choices=33, num_blue_balls=1):
    ticket = []
    for i in range(num_blue_balls):
        red_balls = generate_red_balls(num_red_balls=num_red_balls, num_choices=num_choices)
        blue_ball = generate_blue_ball(num_choices=num_choices)
        ticket.append({'红球': red_balls, '蓝球': blue_ball})
    return ticket

if __name__ == '__main__':
    ticket = generate_lottery_ticket(num_red_balls=8, num_blue_balls=2)
    print('双色球复式投注号码：', ticket)
