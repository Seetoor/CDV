print("Zad. 18 - dni miesiaca ze slownika")
kalendarz = {
	1: {"nazwa": "Styczen", "dni": 31},
	2: {"nazwa": "Luty", "dni": 29},
	3: {"nazwa": "Marzec", "dni": 31},
	4: {"nazwa": "Kwiecien", "dni": 30},
	5: {"nazwa": "Maj", "dni": 31},
	6: {"nazwa": "Czerwiec", "dni": 30},
	7: {"nazwa": "Lipiec", "dni": 31},
	8: {"nazwa": "Sierpien", "dni": 31},
	9: {"nazwa": "Wrzesien", "dni": 30},
	10: {"nazwa": "Pazdziernik", "dni": 31},
	11: {"nazwa": "Listopad", "dni": 30},
	12: {"nazwa": "Grudzien", "dni": 31}
}

nr = 0
while((nr in range(1, 12+1)) == False):
	print("Podaj numer miesiaca (1-12)")
	nr = int(input())

print("Miesiac: " + str(kalendarz[nr]["nazwa"]))
print("Ilosc dni: " + str(kalendarz[nr]["dni"]))