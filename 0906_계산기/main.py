import calc

num1 = int(input("숫자를 입력해 주세요: "))
num2 = int(input("숫자를 한 개 더 입력해 주세요: "))
operator = input("어떤 기능을 원하십니까? (+,-,*,/ 중 택 1): ")

if operator == "+":
    print(calc.add(num1,num2))
elif operator == "-":
    print(calc.minus(num1,num2))
elif operator == "*":
    print(calc.multiple(num1,num2))
else:
    print(calc.divide(num1,num2))