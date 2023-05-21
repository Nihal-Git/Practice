#!/usr/bin/env python3

def fibo(bound):
	
	term_1, term_2, count= 0, 1, 2
	fib_list= [0]
	while(count<= bound):
		
		term_3= term_1 + term_2
		term_1= term_2
		term_2= term_3
		fib_list.append(term_1)
		count+= 1
		
	return fib_list
