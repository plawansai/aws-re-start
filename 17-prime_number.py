def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Find and display prime numbers between 1 and 250
prime_numbers = [num for num in range(1, 251) if is_prime(num)]

# Display prime numbers
print("Prime numbers between 1 and 250:")
print(prime_numbers)

# Save prime numbers to results.txt
with open('results.txt', 'w') as file:
    file.write('\n'.join(map(str, prime_numbers)))

print("Results have been saved to results.txt.")
