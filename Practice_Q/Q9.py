def merge_files(input1, input2, output):
    with open(input1,'r') as file1 :
        data1 = file1.readlines()
        
    with open(input2,'r') as file2 :
        data2 = file2.readlines()
        
    merge_data = data1 + data2
    
    with open(output,'w') as file3 :
        file3.writelines(merge_data)
        
    print("filename has been sucessfully created")
    
merge_files("input1.txt", "input2.txt", 'output_result.txt')