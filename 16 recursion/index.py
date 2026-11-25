# count=0
# def function(n):
#     global count
#     count +=1
#     if (count==5):
#         return count
#     return function(n+1)
# print(function(1))

# Ans=5

# --------------------------------------------------------------------

add=0
def addition(n):
    global add
    add +=n
    if (n==10):
        return add
    return addition(n+1)
print(addition(1))