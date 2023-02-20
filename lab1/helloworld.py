# A simple script which:
#
#   -prints "Hello world";
#
#   -creates a function which takes three parameters:
# two numbers and operation(string like “add”, “sub”,
# “mult” and “div”) and returns the result of this
# operation with two given arguments;
print("Hello world")


def math_operation(num1, num2, operation):
    """
    Function which takes two numbers and operation
    and return the result of this operation.
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
