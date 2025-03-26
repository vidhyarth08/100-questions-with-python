#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
#Suppose the following input is supplied to the program:
#hello world and practice makes perfect and hello world again
#Then, the output should be:
#again and hello makes perfect practice world

def sort_words(in_str):
    words = in_str.split(" ")
    words = list(set(words))
    words.sort()
    return " ".join(words)

in_str = input("Enter a sequence of whitespace seperated words: ")
print(sort_words(in_str))