num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
operator:str = input("Please enter +, -, *, /: ")

if operator == '+':
         result = num1+num2
elif operator == '-':
         result = num1-num2
elif operator == '*':
         result = num1*num2
elif operator == '/':
         result = num1/num2
print(result)
