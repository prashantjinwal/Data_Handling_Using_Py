def count_elements(numbers):
    element_counts = {}
    
    for number in numbers:
        if number in element_counts:
            element_counts[number] += 1
        else:
            element_counts[number] = 1
            
    return element_counts

numbers = [1, 2, 2, 3, 4, 4, 4, 5]
element_counts = count_elements(numbers)

print("Element counts:", element_counts)
