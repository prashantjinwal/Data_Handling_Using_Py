def main():
    filename="Question_10.txt"  
    MyDict={}                   
    vowels=['a','i','o','u','e']
    with open(filename, 'r') as fh :
        content=fh.read().lower()
        for el in vowels:
            count=content.count(el)   # count occurence of a vowel in content
            MyDict[el]=count          # create dict element of that vowel 
                
    print(MyDict)

if __name__=="__main__":
    main()
