#FIZZBUZZ GAME
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0: # as an example, 15 can be divided by 3 5 times and vice versa with 0 remainder after the division. use this to check if code working properly
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)