import random

x = "qwertyuıopüasdfghjklşizxcvbnmöçQWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ1234567890*-!'^+%&/()=?_>£#$½{[]}\|"
y = int(input("Parolanızın uzunluğu ne kadar olsun?: "))

z = ""

for i in range(y):
    a = random.choice(x)
    z = z+a

print("Parolanız: ", z)
