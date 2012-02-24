from lernstube.kern.aufgabe import Aufgabe
from math import pow
from random import random

class Addition(Aufgabe):

    def __init__(self, stellen=3, anzahl=2):
        self.anzahl = anzahl
        self.stellen = stellen
        self.zahlen = []
        self.ergebnis = None
        self.korrekt = 0
        self.eingabe = None
        self.generator()

    def generator(self):
        unit = pow(10,self.stellen)
        self.zahlen = [int(unit*random()) for i in range(self.anzahl)]
        self.ergebnis = sum(self.zahlen)

    def beschreibung(self):
        zahlen = str(self.zahlen[0]) + "".join([" und " + str(i) for i in self.zahlen[1:]])
        return "\n Wie lautet die Summe von %s? \n" % zahlen

    def pruefung(self, val, test=False):
        try:
            self.eingabe = val
            if self.ergebnis == int(val):
                self.korrekt = 1
                if not test:
                    print "\n %s ist richtig." % val
            else:
                self.korrekt = 0
                if not test:
                    print "\n %s ist falsch. Das richtige Ergebnis lautet %s. \n" % (val, self.ergebnis)
        except:
            print "Eingabefehler"

    def istKorrekt(self):
        return self.korrekt

    def eingabe(self):
        return self.eingabe
