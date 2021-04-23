print('Hello! I am Rafi Robin. This is my python project.')

print('This tool genarate your age :)')

now_year=2021
birth_year=int(input('Inter your birth year :'))   #When a user input a number the value save as string. To make the input as number use int() .

age=(now_year-birth_year)

print(f'You are {age} years old :)')

if age<13:
	print('You are a kid :)')

if 13<age<16:
	print('You are a teen')

if age==16:
	print('You and I are the same age')

if 16<age<18:
	print('You are a teen')
	
if age>18:
	print('You are an adult')