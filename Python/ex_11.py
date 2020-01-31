print("Zad. Obliczanie silni")
print("Wpisz silnie")

silnia = int(input())
if(silnia <= 0):
	print("Niepoprawna wartosc")
	exit()

# Metoda 1 #
print("Metoda 1")

wynik1 = 1;
for i in range(silnia):
	wynik1 *= i + 1
print(wynik1)


#metoda 2#

print("Metoda 2")
def Obliczanie(n):
	if n <= 1:
		return 1
	return n * Obliczanie(n - 1)


wynik2 = Obliczanie(silnia)
print(wynik2)