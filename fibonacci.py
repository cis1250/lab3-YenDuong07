#!/usr/bin/env python3

# fib Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the fib sequence up to that many terms.

fibOut = 0;
fib1 = 0
fib2 = 1;
int user_input = 0;
int output;

while (user_input < 0):
  user_input = input("Enter a number to know the fib sequence to it: ");
  if (user_input < 0):
    print("Please enter a positive number!\n");

for x in range (user_input):
  fibOut = fib1 + fib2;
  print("fibOut\n");
  fib2 = fib1;
  fib1 = fibOut;

  
