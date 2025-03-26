#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT

def capitalize_lines(in_str):
    lines = in_str.split("\n")
    return "\n".join([line.upper() for line in lines])

in_str = input("Enter the sequence of lines: ")
print(capitalize_lines(in_str))