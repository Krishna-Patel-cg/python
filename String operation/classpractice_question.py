a="krishna"
print(a[-5])
print(a[0:6])
print(a[0:])
print(a[:6])
print(a[:])
print(a[0:-1])
print(a[:-5])
a="krishna"
b="patel"
print(a+"  "+b)
print(a[::2])
print(a[:-8:-1])
print(a[::-1])
text = "Python"

print(text[0])
print(text[3])
print(text[-1])
print(text[-2])

text = "Programming"

print(text[0:4])
print(text[3:8])
print(text[:5])
print(text[5:])

text = "Python"

print(text[::2])
print(text[1::2])
print(text[::-1])

text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Java" not in text)

text = "banana"

print(text.find("a"))
print(text.find("z"))
print(text.find("r"))
print(text.count("a"))


a="python"
print("j"+a[1:])
b=a[0:1]+"c"+a[2:5]
print(b)


a="python"
print(a)

a="python"
print("capitalize:",a.capitalize())
print(a.upper())
print(a.lower())
print(a.casefold())
print("swap",a.swapcase())

a="krishna patel"
print(a.find("a"))
print(a.index("patel"))
# print(a.text())
print("kri" in a)
print("z" in a)
print("z" not in a) 

a="I like java"
print(a.replace("java","python"))


b="Hello"
print(b+"World")
print(b*3)

#part 3
name="krishna"
city="varanasi"
programing_launguage="python"
massage="My first like and last like Ana"
print(name,city,programing_launguage,massage)


a="banana"
print(a.count("a"))
c="bababababababaabsiocdishbabababksjibababaiojdwcsbjbabbaajfidjbbaabbaa"
print(c.count("b"))

c ="   "
print(len(c))
print(type(c))

a="Python Programing"
print(a)
print(len(a))
print(a[0:1])
print(a[16:])
print(a[2:3])
print(a[-1:])


b="Programing"
print(b[0:1])
print(b[1:2])
print(b[4:5])
print(b[-1:])

b="Programing"
print(b[-1:])
print(b[-2:-1])
print(b[-3:-2])


n="Krishna Patel"
print(n[0:1])
print(n[-1:])
print(n[-5:])


a="Python Programing"
print(a[0:6])
print(a[7:])
print(a[0:])
print(a[0:5])
print(a[-5:])

h="ABCDEFGHIJKL"
print(h[::2])
print(h[::3])
print(h[1:8:2])
print(h[::-1])

g="Python Programming"
print(g[-5:])
print(g[-10:])
print(g[::-1])

g="Python Programming"
print(g[:3])
print(g[-3:])
print(g[::2])
print(g[::-1])
# print(g())

a = "krishna"
b="karanthisismyfriend"
c="dipak is my friend and big brother"
print(len(a))
print(len(b))
print(len(c))

a = "Python Programming"
print(len(a))


first_name="krishna"
last_name="patel"
print(first_name+last_name)
first_name=" krishna "
last_name=" patel "
print(first_name+last_name)


name="krishna"
city="varanasi"
programing_launguage="python"
print(name+city+programing_launguage)

name="krishna"
b=5
# print(a+b)  type error
print(a+str(b))

a="*"
b=10 
print(a*b)

j="python programming language"
print(j.upper())
print(j.lower())
print(j.capitalize())
print(j.title())
print(j.swapcase())


a="Python"
b="python"
print(a.lower())
print(b.lower())

s="Python is a programming language"
print("Python" in s)
print("programming" in s)
print("Java" in s)
print("language" in s)


s="Python is a programming language"
print(s.find("Python"))
print(s.find("programming"))
print(s.find("Java"))
print(s.find("language"))

s="Python is a programming language"
print(s.find("Java"))
# print(s.index("Java"))


b="banana"
print(b.count("a"))
print(b.count("n"))
print(b.count("b"))


f= "student_notes.pdf"
print(f.startswith("student"))
print(f.endswith(".pdf"))
print(f.endswith(".txt"))

t= "I am learning Java"
print(t.replace("Java","Python."))


d= "apple apple apple"
print(d.replace("apple","mango"))

c= "apple apple apple"
print(c.replace("apple*2","mango*2"))



text = "Python"
print(text.upper())