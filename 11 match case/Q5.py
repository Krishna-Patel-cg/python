user_choice=2
match user_choice:
    case 1:
        print("View Profile")
    case 2:
        print("View Courses")
    case 3:
            print("View Marks")
    case 4:
            print("View Attendance")
    case 5:
            print("Logout")
    case _:
            print("Invalid ")