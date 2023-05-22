#!/usr/bin/env python3

# recursion for recurring sum from 1 to n
def recurring_sum(n):
	
	if n!=0:
		return n+ recurring_sum(n-1)
	else:
		return 0
	
# Factorial
def factorial(n):
	if n==0:
		return 1
	else:
		return n* factorial(n-1)
	
	
# Fibonacci
def fibonacci(n):
	
	if n in [0, 1]:
		return 1
	
	else:
		return fibonacci(n-1)+fibonacci(n-2)
	
	
# product of numbers in a list
def product(list1):
	
	if len(list1) == 0:
		return 1
	elif len(list1) == 1:
		return list1[0]
	else:
		return list1[-1] * product(list1[:-1])

# string reversal
def reversal(string):
	
	if len(string)==0:
		return 'void!'
	elif len(string) == 1:
		return string
	else:
		return string[-1]+ reversal(string[:-1])
	
	
# string palindrome
def palindrome(string):
	
	if len(string)==0:
		return True
	if string[0] != string[len(string)-1]:
		return False
	return palindrome(string[1:-1])

			
	
	
	