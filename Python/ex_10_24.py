print("tworz skrypt z interfejsem tekstowym, ktory przyjmie od uzytkownika ile elementow chce on wprowadzic do listy [...]")

class Matma:
	def __init__(self, ilosc_elementow):
		self.elementy = []
		self.ilosc_elementow = ilosc_elementow
		for n in range(ilosc_elementow): self.PrzyjmijElement(n)

		self.srednia = self.ObliczSrednia()
		self.odchylenie = self.ObliczOdchylenie()

	def PrzyjmijElement(self, n):
		print("Wartosc elementu (nr. " + str(n+1) + "):")
		self.elementy.append(int(input()))

	def ObliczSrednia(self):
		return sum(self.elementy) / len(self.elementy)

	def ObliczOdchylenie(self):
		nnn = [(1/len(self.elementy)) * (n-self.srednia)**2 for n in self.elementy]
		wari = sum(nnn)		 
		return wari**0.5



print("Ilosc elementow listy:")
ilosc_elementow = int(input())

obliczenia = Matma(ilosc_elementow)
print("Srednia z liczb: " + str(obliczenia.srednia))
print("Odchylenie standardowe: " + str(obliczenia.odchylenie))