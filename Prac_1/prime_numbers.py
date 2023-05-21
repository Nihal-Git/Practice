#!/usr/bin/env python3

def prime(limit):
	
	for i in range(1, limit+ 1):
		if i> 1:
			for j in range(2, i):
				if (i% j == 0):
					break
			else:
				print(i)