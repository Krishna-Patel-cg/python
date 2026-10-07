# # number = int(input("Enter a number: "))
# # total = 0
# # while number != 0:
#     # number = int(input("Enter a number: "))
# num1=int(input("Enter first number :"))
# num2=int(input("Enter second number :"))
# choice=int(input("Enter your choice 1.Addition 2.Subtraction 3.Multiplication 4.Division :"))
# while choice != 0:
#     match choice:
#         case 1:
#             print("Addition is:", num1 + num2)
#         case 2:
#             print("Subtraction is", num1 - num2)
#         case 3:
#             print("Multiplication is", num1 * num2)
#         case 4:
#                 print("Division is",num1/num2)
#         case _:
#             print("Invalid choice")
#         break
        


# account = "student"
# choice = 2

# match account:

#     case "student":

#         match choice:
#             case 1:
#                 print("View Courses")
#             case 2:
#                 print("View Marks")
#             case 3:
#                 print("View Attendance")
#             case _:
#                 print("Invalid Choice")

#     case "teacher":

#         match choice:
#             case 1:
#                 print("View Students")
#             case 2:
#                 print("Enter Marks")
#             case _:
#                 print("Invalid Choice")

#     case _:
#         print("Invalid Account Type")

# day=4
# match day:
#     case 1 or 2 or 3 or 4 or 5:
#        print("Weekday")               //error
#     case 6 or 7:
#        print("Weekend")
#     case _:
#       print("Invalid")

# day=4
# match day:
#     case 1 | 2 | 3 | 4 | 5:
#        print("Weekday")
#     case 6 | 7:
#        print("Weekend")
#     case _:
#       print("Invalid")

# day=4
# match day:
#     case 1 | 2 | 3 | 4 | 5:
#        print("Weekday")
#     case 6 | 7:
#        print("Weekend")
#     case _:
#       print("Invalid")


# marks=933
# match marks:
#     case k if marks>=90  and marks<=100:
#       print("A")
#     case k if marks>=75:
#         print("A")
#     case k if marks>=60:
#         print("A")
#     case k if marks>=40:
#           print("A")
#     case k if marks>=0:
#       print("Fail")
#     case _:
#       print("Invalid marks")

# =================================  Gas Booking  =====================


user=input("choice you are manager or custmer")
match "user":
   case "PMUY":
      choice=int(input("Choice "))
      match choice:
        case 1:
            need=input("OTP varification")
            match need:
                case "Text massage":
                  print("Booking successful")
                case "whatsapp":
                   print("Booking successful")

match "user":
   case manager:
       choice=input("Choice ")
       match choice:
          case "1":
            varification=input("See account deatails")
            match varification:
                case "Yes":
                   print("Varification successful")
                case "No":
                   print("Need EKYC")



# category = "student"
# choice = 3

# match category:
#     case "student":
#         match choice:
#             case 1:
#                 print("Course")
#             case 2:
#                 print("Marks")
#             case 3:
#                 print("Attendance")
#             case _:
#                 print("Invalid")

#     case "teacher":
#         print("Teacher")

#     case _:
#         print("Unknown")


# choice = 3
# age = 17

# match choice:
#     case 1:
#         if age >= 18:
#             print("Adult")
#         else:
#             print("Minor")

#     case 2:
#         print("Option 2")

#     case 3:
#         if age >= 18:
#             print("Allowed")
#         else:
#             print("Not Allowed")

#     case _:
#         print("Invalid")



# command = "pause"
# choice = 2

# match command:
#     case "start":
#         print("Starting")

#     case "pause":
#         match choice:
#             case 1:
#                 print("Pause Music")
#             case 2:
#                 print("Pause Video")
#             case _:
#                 print("Invalid Pause Choice")

#     case "stop":
#         print("Stopping")

#     case _:
#         print("Unknown Command")