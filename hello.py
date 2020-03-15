#A começar pelo inicio como deve ser!####
#########################################

# Clear the terminal screen
import os
import namer
os.system('clear')

'''#fizzbuzz exmple
num = 1
fizzcount = 0
buzzcount = 0
fizzbuzzcount = 0

while (num <= 1000000):
	if (num % 3 == 0) and (num % 5 == 0):
		print(str(num) + ": Fizzbuzz!")
		fizzbuzzcount += 1
	elif (num % 3 == 0):
		print(str(num) + ": Fizz!")
		fizzcount += 1
	elif (num % 5 == 0):
		print(str(num) + ": Buzz!")
		buzzcount += 1
	else:
		print(str(num))
	
	num +=1

print("----")
print("Fizz\t\tBuzz\t\tFizzBuzz")
print(str("{:,}".format(fizzcount)) + "\t\t" + str(buzzcount) + "\t\t" + str(fizzbuzzcount))


####functions#####
def mathit(num1, num2):
	return (num1 + num2)

outcome = mathit(9, 1)

print(outcome *10)
'''

####modules#####

namer.nameit("Pedro")