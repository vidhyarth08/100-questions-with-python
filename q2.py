#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

n = int(input())
print(factorial(n))