while True:
    marks = int(input("Enter marks between 0 and 100: "))

    if 0 <= marks <= 100:
        print("Valid marks")
        break
    else:
        print("Invalid marks. Try again.")