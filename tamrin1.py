def calculate_average(*args):
    if len(args) == 0:
        print("Oops! You didn't enter any numbers to calculate.")
        return 0

    total_numbers = len(args)
    max_number = max(args)
    min_number = min(args)
    final_average = sum(args) / total_numbers

    print(f"Total numbers given: {total_numbers}")
    print(f"Highest number: {max_number}")
    print(f"Lowest number: {min_number}")
    print(f"Calculated Average: {final_average}")

    return final_average


print("---       ---")
my_result = calculate_average(1,2,3,4,5,6,7)
print(f"The function returned: {my_result}")

print("---        ---")
empty_result = calculate_average()
print(f"The function returned: {empty_result}")
