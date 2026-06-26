#!/usr/bin/python3
def fizzbuzz():
    final = ""
    for i in range(1, 101):
        if i % 3 == 0:
            final += "Fizz "
        elif i % 5 == 5:
            final +=  "Buzz "
        elif i % 3 == 0 and i % 5 == 0:
            final += "FizzBuzz "
        else:
            final += f"{i} "
    return final
print(fizzbuzz())
