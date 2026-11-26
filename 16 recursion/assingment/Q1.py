def show(n):
    if n==0:
        print("End")
        return
    print("Start",n)
    show(n-1)
    print("Back",n)
show(2)

# def show(n):
#     if n == 0:
#         print("Stop")
#         return

#     print(n)
#     show(n - 1)
#     print(n)

# show(2)