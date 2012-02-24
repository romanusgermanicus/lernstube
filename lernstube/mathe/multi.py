from lernstube.kern.aufgabe import Aufgabe
from math import pow
from random import random
from operator import mul

class Multiplikation(Aufgabe):

    def __init__(self, stellen=2, anzahl=2):
        self.anzahl = anzahl
        self.stellen = stellen
        self.zahlen = []
        self.ergebnis = None
        self.generator()

    def generator(self):
        unit = pow(10,self.stellen)
        self.zahlen = [int(unit*random()) for i in range(self.anzahl)]
        self.ergebnis = reduce(mul, self.zahlen, 1)

    def beschreibung(self):
        zahlen = str(self.zahlen[0]) + "".join([" und " + str(i) for i in self.zahlen[1:]])
        return "\n Wie lautet das Produkt von %s? \n" % zahlen

    def pruefung(self, val, test=False):
        retval = 0
        try:
          if self.ergebnis == int(val):
              if not test:
                  print "\n %s ist richtig." % val
              retval += 1
          else:
              if not test:
                  print "\n %s ist falsch. Das richtige Ergebnis lautet %s. \n" % (val, self.ergebnis)
        except:
            print "Eingabefehler"
        return retval
