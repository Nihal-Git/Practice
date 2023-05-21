#!/usr/bin/env python3

from prime_numbers import prime
from factorial import factor
from fibonacci_series.fibonacci import fibo



def choose():
	
	print("1 ---- Prime Numbers\n")
	print("2 ---- Factorial\n")
	print("3 ---- Fibonacci\n")
	
	choice= int(input('Enter Choice: '))
	
	return choice

def switch_case(choice):
	
	if choice == 1:
		print('Prime Number: \n')
		limit= int(input('Limit of prime numbers: '))
		prime(limit= limit)
	elif choice == 2:
		print('Factorial: \n')
		number= int(input('Enter an Integer for its factorial: '))
		factor(number= number)
			
	elif choice == 3:
		print('Fibonacci: \n')
		bound= int(input('Enter upper limit for Fibonacci: '))
		count= fibo(bound= bound)
		print(f"The {bound} numbers in fibonacci series are {count}")
		
	else:
		print('Invalid Input: ')
		print('Try again ////')
		exit();


choice = choose()
switch_case(choice)