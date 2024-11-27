import random
def get_numbers_ticket(min, max, quantity):
    res = random.sample(range(min, max), quantity)
    print(res)

get_numbers_ticket(10, 22, 3)
