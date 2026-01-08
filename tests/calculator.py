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

