priority=int(input("Enter your priority"))
match priority:
    case 1 | 2:
        print("Normal Priority")
    case 3 | 4:
            print("Urgent Priority")