alpha=input("Enter allphabate character")
if chr(65) <= alpha <= chr(90):
    print("Uppercash")
elif chr(97) <= alpha <= chr(112):
    print("Lowercash")
elif chr(48)<=alpha <=chr(57):
    print("Digit")
else:
    print("Special character")