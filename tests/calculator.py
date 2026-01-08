#calculator

print("====calculator====")
print('')

#ask numbers
num1 = float(input("your first number:  "))
num2 = float(input("your second number:  "))


#operations
sum_result = num1 + num2
diff_result = num1 - num2
mult_result = num1 * num2

"""
#output results

print(f"\nResults:")
print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} - {num2} = {diff_result}")
print(f"{num1} * {num2} = {mult_result}")

# Деление с проверкой на ноль
if num2 != 0:
    div_result = num1 / num2
    print(f"{num1} / {num2} = {div_result}")
else:
    print("Fuck you! this is Zero")
"""

#extention
operation = input("type of operation:(+, -, *, /, **, %): ")
idiot = False
if operation == '+':
	result = num1 + num2
elif operation == '-':
        result = num1 - num2
elif operation == '*':
        result = num1 * num2
elif operation == '/':
	if num2 != 0:
	        result = num1 / num2
	else: 
		idiot = True
elif operation == '**':
        result = num1 ** num2
elif operation == '%':
        result = num1 % num2
else: 
	idiot = True
if idiot == False:
	print(f'{num1} {operation} {num2} = {result}')
else: 
	print("Are you Idiot?")

	

