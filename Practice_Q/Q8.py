def clg_line(filename): 
    lines = [
        "line1 clg clg clg",
        "line2 hn hn acha clg",
        "line3 hn hn bhot acha clg",
        "line4 hn hn bhai bhot jada mast badiya best clg",
        "line5 arre bass kar bhai"
    ]
    
    with open(filename, 'w') as file:
        file.writelines(lines)
    print(f"{filename} has been created with the lines")    
    
    
clg_line("clg_info.txt")