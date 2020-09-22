"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
from functools import reduce


# Replace this with your code

user_input = input("")


while user_input[0][0] != 'q' and user_input[0][0] != 'Q':
    
    inputs = user_input.split(" ")
    operator = inputs.pop(0)
    
    tokens = []

    for num in inputs:
        tokens.append(float(num))

    try: 
        if operator == '+':
            print(reduce(add, tokens))
        
        elif operator == '-':
            print(reduce(subtract, tokens))
        
        elif operator == '*':
            print(reduce(multiply, tokens))
        
        elif operator == '/':
            print(divide(float(tokens[1]), float(tokens[2])))
        
        elif operator == 'square':
            print(square(float(tokens[1])))
        
        elif operator == 'cube':
            print(cube(float(tokens[1])))

        elif operator == 'pow':
            print(power(float(tokens[1]), float(tokens[2])))
        
        elif operator == 'mod':
            print(mod(float(tokens[1]), float(tokens[2])))
    except:
        print("invalid input")

    user_input = input("")
