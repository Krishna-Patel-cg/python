num1=int(input("Enter first name"))
num2=int(input("Enter second name"))
operaters="*"
match operaters:
    case "+":
        print(num1+num2)
    case "-":
            print(num1-num2)
    case "*":
            print(num1*num2)
    case "/":
            print(num1/num2)
    case _:
            print("Invalid operators")