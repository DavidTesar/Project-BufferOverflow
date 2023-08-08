def generate_as(num_as):
    return 'A' * num_as

desired_count = int(input("Enter the desired number of 'A's: "))
result = generate_as(desired_count)
print(result)