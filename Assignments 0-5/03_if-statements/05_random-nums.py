import random
def generate_random_numbers():
    for _ in range(10):
        print(random.randint(1, 100), end=" ")
generate_random_numbers()
