#!/usr/bin/env python3

def factor(number):
	
	fact, i= 1, 1
	while (i<=number):
		fact= fact*i
		i+= 1
	print(f'Factorial of {number} is = {fact}')
	return 0