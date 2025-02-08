def first_unique_char(s: str) -> str:
    for char in s:
        if s.count(char) == 1:  
            return char
    return "None" 
s = input("Enter a string: ")
print("The first non-repeating character is:", first_unique_char(s))
