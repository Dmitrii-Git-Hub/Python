# elif синтаксический сахар
a = 200
b = 300
c = 400
if a > b:
  if a > c:
    print("max =", a)
  else:
    print("max =", c)
elif  b > c:
 print("max =", b)
else:
 print("max =", c)
