def swap_f(s):
    
    if len(s) < 4:
        return "String is too short to swap!"

    
    first_two = s[:2]
    last_two = s[-2:]

    
    new_string = last_two + s[2:-2] + first_two

    return new_string


string = "abcdef"
swapped_string = swap_f(string)
print(swapped_string)  # Output: "efcdab"
