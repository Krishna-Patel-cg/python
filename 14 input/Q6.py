
temperature = int(input("Enter a temperature  "))
while temperature < -20 or temperature > 45:
    print("Invalid temperature")
    temperature = float(input("Enter a temperature "))
print(f"Valid temperature : {temperature}")