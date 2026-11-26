Agar recursive function bahut zyada baar andar-hi-andar call ho jaye to kya hota hai: Jab bhi 
koi function khud ko call karta hai, Python uski jaankari (jaise variables aur wapas aane ki jagah) ko call 
stack mein ek naye dabbe (stack frame) mein rakhta hai. Agar call bahut gehri chali jaye—jaise base case na ho,
 base case tak pahunch hi na paaye, ya input bahut bada ho—to stack bhar jaata hai, memory badhti hai, aur program beech mein hi ruk (crash ho) jaata hai.


Python mein kaun sa error aata hai: RecursionError (RecursionError: maximum recursion depth exceeded).


Bahut bade counting ke kaam ke liye loop kyun behtar hota hai: Loop ek hi jagah (for ya while se) chalta
 hai aur naye stack frames nahi banata, isliye recursion limit ki dikkat nahi aati aur memory bhi kam lagti hai.