#Question 1
#Level 1
#
#Question:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
#
#Hints: 
#Consider use range(#begin, #end) method

def printnumbers():
    numbers = [] 
    k=1
    for number in range(2000,3201)[::k]:
        if (number%7 is 0) and (number%5 is not 0):
            numbers.append(number) 
            if k is not 7: 
                 k=7;
    print(numbers)

def fact(n):
	fa = 1
	for d in range(n,1,-1):
		fa = fa * d
	return fa;

n = int(input('Number --> '))
print(fact(n))
