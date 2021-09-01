#Heron of Alexandria's algorithm for the square root of a number.

y = float(input("Enter the number whose square root you want to find: "))
guess = float(input("Enter a starting guess: "))

# Accuracy/error of the result: epsilon 
epsilon = float(input("Enter the desired precision: "))

while (abs(guess**2 - y) >= epsilon):
    guess = (1/2) * (guess + y / guess)

print("An approximation to the square root of " + str(y) + " is " + str(guess))

