"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

user_input = input("")


while user_input[0][0] != 'q' and user_input[0][0] != 'Q':
    tokens = user_input.split(" ")
    if user_input[0] == '+':
        print(add(float(tokens[1]), float(tokens[2])))
    user_input = input("")
