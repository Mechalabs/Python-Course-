def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        #here is the recursion - calls itself to simplify the problem
        #Otherwise we would need to account for how big the inputted number is
        return (x * calc_factorial(x-1))

num = 4
print("The factorial of", num, "is", calc_factorial(num))