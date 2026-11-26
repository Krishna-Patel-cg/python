# def num(n):
#     if n==5:
#         return
#     print(n)
#     num(n+1)
# num(1)


count=0
def fun(n):
    global count
    if n==5:
        return
    fun(n+1)
    count+=1
    print(count)
fun(1)



count=0
def fun(n,count):
    if n==count:
        return
    count+=1
    print(count)
    fun(n,count)
fun(4,count)