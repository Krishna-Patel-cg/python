# x=1
# def kp():
#     y=22
#     print(x)
#     print(y)
# kp()

# Ans ==  1 22 
# -----------------------------------------------------------------------

# x=1
# def kp():
#     y=22
#     x=12
#     print(x)
#     print(y)
# kp()

# Ans == 12   22 

# -------------------------------------------------------------------------------------------

# x=1 
# def ap():
#     x=2
#     def kp():
#         x=3
#         print("Inner sees x equal to",x)
#         return
#     kp()
#     print("Outer sees x equal to",x)
#     return
# ap()
# print("Global sees x equal to",x)

# Ans =Inner sees x equal to 3
#     Outer sees x equal to 2
#     Global sees x equal to 1
# ..................................................................
# x=1 
# def ap():
#     def kp():
#         print("Inner sees x equal to",x)
#         return
#     kp()
#     print("Outer sees x equal to",x)
#     return
# ap()
# print("Global sees x equal to",x)

# Ans=  Inner sees x equal to 1
#     Outer sees x equal to 1
#     Global sees x equal to 1

# ..............................................

x=1 
def ap():
    x=2
    def kp():
        global x
        x=3
        print("Inner sees x equal to",x)
        return
        
    kp()
    print("Outer sees x equal to",x)
    return
ap()
print("Global sees x equal to",x)