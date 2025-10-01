#!/usr/bin/env python3

# fib Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the fib sequence up to that many terms.

fibOut = 0;
fib1 = 0
fib2 = 1;

user_input = int(input("Enter a number to know the fib sequence to it: "));

while (user_input < 0):
    print("Please enter a positive number!\n");
    user_input = input("Enter a number to know the fib sequence to it: ");

for x in range (user_input):
  print(fibOut);
  fibOut = fib1 + fib2;
  fib2 = fib1;
  fib1 = fibOut;

  
