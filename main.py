def find_prime_numbers():
    prime_numbers = []
    for num in range(1, 101):
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    return prime_numbers

def print_prime_numbers(prime_numbers):
    for num in prime_numbers:
        print(num)

def main():
    prime_numbers = find_prime_numbers()
    print("1 dan 100 gacha tub sonlar:")
    print_prime_numbers(prime_numbers)

main()