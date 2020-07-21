import random
print("Bobby's Awesome Calculator Game")
print('-------------------------------')
"""num1 = input("Enter first number: ")
print(f"num1: {num1}")
num2 = input("Enter second number: ")
print(f"num1: {num2}")
bobby = int(num1) * int(num2)
print(f"{num1} * {num2} is {bobby}")

bobby = int(num1) + int(num2)
print(f"{num1} + {num2} is {bobby}")


bobby = int(num1) - int(num2)
print(f"{num1} - {num2} is {bobby}")
"""
count = 0
tries = 0
while True:
    tries = tries + 1
    num1 = random.randint(0, 15)
    num2 = random.randint(0, 15)
    answer = num1 * num2
    guess = input(f"What is {num1} * {num2}: ")
    if answer == int(guess):
        count = count + 1
        print(f"Correct! ({count} of {tries})")
    else:
        print(f"Wrong! Answer is {answer}! ({count} of {tries})")


print(f"{num1} * {num2} is {num1 * num2}")