print("Zad. W klasie przeprowadzono sprwadzian, za ktory uczniowie mogli otrzymac maksymalnie 40 punktow. [...]")

class WyznaczOcene:
	def __init__(self, punkty, max_punkty):
		self.punkty = punkty
		self.max_punkty = max_punkty

		self.wynik_procentowy = self.WyliczProcenty()
		self.ocena_numeryczna = self.ocenaNumeryczna()
		self.ocena_slowna = self.OcenaSlowna()
	def WyliczProcenty(self):
		return (self.punkty / self.max_punkty) * 100
	def ocenaNumeryczna(self):
		if(self.SprwadzPrzedzial(0,39)):
			return 1
		if(self.SprwadzPrzedzial(40,49)):
			return 2
		if(self.SprwadzPrzedzial(50,69)):
			return 3
		if(self.SprwadzPrzedzial(70,84)):
			return 4
		if(self.SprwadzPrzedzial(85,99)):
			return 5
		return 6
	def SprwadzPrzedzial(self, min, max):
		return self.wynik_procentowy >= min and self.wynik_procentowy <= max
	def OcenaSlowna(self):
		return ["ndst", "dop", "dst", "db", "bdb", "cel"][self.ocena_numeryczna - 1]



max_punkty = 40
print("Maksymalna ilosc punktow: " + str(max_punkty))
print("Wprowadz zdobyte punkty:")
zdobyte_punkty = input()
zdobyte_punkty = int(zdobyte_punkty)

if(zdobyte_punkty > max_punkty or zdobyte_punkty < 0):
	print("Niepoprawna ilosc zdobytych punktow")
	exit()

WyznaczonaOcena = WyznaczOcene(zdobyte_punkty, max_punkty)

print("Wynik procentowy: " + str(WyznaczonaOcena.wynik_procentowy))
print("Ocena numeryczna: " + str(WyznaczonaOcena.ocena_numeryczna))
print("Ocena słowna: " + WyznaczonaOcena.ocena_slowna)