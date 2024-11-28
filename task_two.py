import random
def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        print("Error: Please ensure 'min' is greater than 1 and 'max' is less than 1000.")
    else:
        try:
            res = random.sample(range(min, max), quantity)
            print(res)
        except ValueError as e:
            range_size = max - min
            print(f"Error: The range size ({range_size}) is too small for the requested quantity ({quantity}). "
                  "Ensure the difference between 'min' and 'max' is greater than or equal to 'quantity'.")
get_numbers_ticket(10, 11, 3)
