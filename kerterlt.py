#gyakorlás

print("1 - Háromszög")
print("2 - Kör")
print("3 - Téglalap")
print("4 - Nyolcszög")
v=input("Milyen alakztattal szeretnél dolgozni?")
if v=="1":
	haromszogKerulet()
	haromszogTerulet()
if v=="2":
	korKerulet()
	korTerulet()
if v=="3":
	teglalapKerulet()
	teglalapTerulet()
if v=="4":
	nyolcszogKerulet()
	nyolcszogTerulet()
    
def triangle(a,b,c):
    print("perimeter: ",a+b+c)
triangle(3,4,5)

def triangle(a,b,c):
    print("ker: ",a+b+c)
a = input("a oldal: ")
b = input("b oldal: ")
c = input("c oldal: ")
triangle(a,b,c)
