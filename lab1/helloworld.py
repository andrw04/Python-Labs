# A simple script which:
#
#   -prints "Hello world";
#
#   -creates a function which takes three parameters:
# two numbers and operation(string like “add”, “sub”,
# “mult” and “div”) and returns the result of this
# operation with two given arguments;
#
#   -creates a list of numbers and returns a list of
# even numbers in this list.
print("Hello world")


def math_operation(num1, num2, operation):
    """
    Function which takes two numbers and operation
    and returns the result of this operation.
    """
    operation = operation.lower()

    if operation == "add":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2
    elif operation == "mult":
        return num1 * num2
    elif operation == "div":
        return num1 / num2
    else:
        print("Incorrect operation!")

    return None


num_list = list(range(0,10)) # list of 1, 2, ..., 9
even_nums = [i for i in num_list if i % 2 == 0 and i != 0] # even in num_list