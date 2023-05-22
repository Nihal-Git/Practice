#!/usr/bin/env python3

# Using Recursion

from recursion_codes import *

def choose():
	
	print("1 ---- Recurring Sum\n")
	print("2 ---- Factorial\n")
	print("3 ---- Fibonacci\n")
	print("4 ---- Product of numbers in a list\n")
	print("5 ---- String Reversal\n")
	print("6 ---- String Palindrome\n")
	choice= int(input('Enter Choice: '))
	return choice

def switch_case(choice):
	
	if choice == 1:
		print('\n\tRecurring Sum:')
		number= int(input('\tEnter Number: '))
		sum= recurring_sum(n= number)
		print(f'\tRecurring Sum from 1 to {number} = {sum}\n')
	elif choice == 2:
		print('\n\tFactorial:')
		number= int(input('\tEnter an Integer for its factorial: '))
		fact=  factorial(n= number)
		print(f'\tFactorial of {number} = {fact}\n')
		
	elif choice == 3:
		print('\n\tFibonacci:')
		limit= int(input('\tEnter number of Fibonacci numbers required: '))
		lasst= fibonacci(limit)
		print(f"\tThe {limit} number in fibonacci series: {lasst}\n")
	
	elif choice == 4:
		print('\n\tProduct of numbers in a list:')
		input_string = input("\tEnter the elements of the list separated by space: ")
		input_list = input_string.split()
		list1 = [int(element) for element in input_list]
		prod= product(list1= list1)

		print(f'\tProduct of {list1} = {prod}\n')
		
	elif choice == 5:
		print('\n\tString Reversal:')
		string= input('\tEnter a string: ')
		reversed= reversal(string= string)
		
		print(f"\tReversed string for {string}= {reversed}\n")
	
	elif choice == 6:
		print('\n\tString Palindrome: ')
		mystring= input('\tEnter a string: ')
		palin= palindrome(string= mystring)
		if palin == True:
			print(f"\tString {mystring} is a Palindrome\n")
		else:
			print(f"\tString {mystring} is not a Palindrome\n ")
		
	else:
		print('\n\tInvalid Input: Try again ////')
		print('\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@1')
		exit();
		
		
choice = choose()
switch_case(choice)