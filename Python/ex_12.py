print("Ciąg Fibonacciego")

class Fib:
	def it (self, n):
	    a=0
	    b=1
	    for i in range (0,n-1):
	        a,b = b, a+b
	    return b

	def rek (self, n):
	    if n==0 :
	        return 0
	    if n==1:
	        return 1
	    if n>1:
	        return self.rek(n-1) + self.rek(n-2)

	def __init__ (self, n):
		print("Iteracyjnie: " + str(self.it(n)))
		print("Rekurencyjnie: " + str(self.rek(n)))

    
print ("Wpisz nr wyszukiwanego wyrazu ciągu:")
print("Ciekawostka: rekurencyjny trwa znacznie dluzej")
n = int(input())
Fib(n)