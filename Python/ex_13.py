class Mat:
    def silnia(self, x):
        if x>1:
            return x*self.silnia(x-1)
        elif x in (0,1):
            return 1

    def newton(self):
        return self.silnia(self.n)/(self.silnia(self.k) * self.silnia(self.n-self.k))

    def oblicz(self):
        self.wynik = self.newton()
        
r = Mat()
r.n = int(input("Podaj n: "))
r.k = int(input("Podaj k: "))
r.oblicz()

print("Wynik: " + str(r.wynik))