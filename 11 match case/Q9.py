weather=input("Enter weather")
match weather:
    case "rainy":
        print("Carry an umbrella")
    case "sunny":
            print("Wear sunglasses")
    case "cloudly":
            print("Weather may change")
    case "snowy":
            print("Wear warm clothes")
    case _:
            print("Invalid Weather")