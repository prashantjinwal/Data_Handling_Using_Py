def calculate_sum_and_average(numbers):
    total_sum = sum(numbers)
    
    average = total_sum / len(numbers) if numbers else 0
    
    return total_sum, average

numbers = [10, 20, 30, 40, 50]
total_sum, average = calculate_sum_and_average(numbers)

print(f"Sum: {total_sum}")
print(f"Average: {average}")
