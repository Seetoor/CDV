print ("Zad. Otworz skrypt do znajdywania miejsc zerowych")


def miejsca_zerowe(a, b, c):
	delta = (b**2) - 4*a*c

	if (delta > 0):
	    return (-b + delta**0.5) / (2 * a), (-b - delta**0.5) / (2 * a)
	elif (delta==0):
	    return [(-b) / (2 * a)]
	else:
		return []

print ("Podaj a:")
a=int(input())

print ("Podaj b:")
b=int(input())

print ("Podaj c:")
c=int(input())

arr = miejsca_zerowe(a, b, c)

if(len(arr) == 0):
	print("Brak miejsc zerowych")
	exit()

for x in arr:
	print("X: " + str(x))