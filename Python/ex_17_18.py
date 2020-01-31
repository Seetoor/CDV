print("Utwórz funkcje, ktora bedzie generowac listy danych do wykreslenia w oparciu o [...]")

import csv


class Funkcje:
  def liniowa (self):
    self.x=[]
    self.y=[]    
    for i in range (0,100):
      self.x.append (i-50)
      self.y.append (self.a * self.x[i] + self.b)

  def kwadratowa (self):
    print("c:")
    c=int (input())
    self.x=[]
    self.y=[]
    for i in range (0,100):
      self.x.append (i-50)
      self.y.append (self.a * self.x[i] * self.x[i] + self.b * self.x[i] + c)

  def odwrotna (self):
    self.x=[]
    self.y=[]
    for i in range (100):
      self.x.append (i+1)
      self.y.append (self.a / self.x[i]**self.b)

  def Zapisz_plik (self):
    with open('zad18.csv', 'w', newline='') as csvfile:
      spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      spamwriter.writerow(self.x)
      spamwriter.writerow(self.y)
  def __init__(self):
    print("1. Funkcja liniowa")
    print("2. Funkcja kwadratowa")
    print("3. Funkcja odwrotna")

    wybrana_funkcja = int(input())

    switcher = {
      1:self.liniowa,
      2:self.kwadratowa,
      3:self.odwrotna
    }

    f = switcher.get(wybrana_funkcja)

    if("method" in str(type(f))):      
      print ("a:")
      self.a = int(input())
      print("b:")
      self.b = int(input())
      
      f()

      print ("X:{}".format(self.x))
      print ("Y:{}".format(self.y))

      self.Zapisz_plik()

    else:
      print("Niepoprawna wartosc...")
      Funkcje()

Funkcje();
