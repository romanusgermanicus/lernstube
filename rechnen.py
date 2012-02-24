#!/usr/bin/python
# -*- coding: utf-8 -*-

from lernstube.mathe.addition import Addition
from lernstube.mathe.multi import Multiplikation
from random import random


print "\n==============================================================="
print "Bist Du bereit für den großen Mathe-Check?"
print "Wie gut ist Dein Gehirn für die Grundrechenarten verdrahtet?"
print "Ich werde Dir eine Reihe von Aufgaben geben."
print "Rechne sie im Kopf oder auf dem Papier."
print "Andere Hilfsmittel sind nicht erlaubt."
print "===============================================================\n"

result = []
test = True
IMAX = 2
punkte = 0
for i in range(IMAX):
    print "\n Aufgabe %s" % i
    print "-----------"
    if random() < 0.5:
        aufgabe = Addition(stellen=1, anzahl=2)
    else:
        aufgabe = Multiplikation(stellen=1, anzahl=2)
    eingabe = raw_input(aufgabe.beschreibung())
    # Ergebnis pruefen
    aufgabe.pruefung(eingabe, test=test)
    # Aufgabe an die Ergebnisliste haengen
    result.append(aufgabe)

# Ermittle Ergebnisstatistik
# filter alle falschen Antworten
# falsche = filter((def f(x): return x.istKorrekt > 0), result)
korrekte = [x for x in result if x.istKorrekt() > 0]

print "\n Auswertung"
print "-----------"
print "Du hast %s von %s möglichen Punkten erreicht." % (len(korrekte), IMAX)
quote = round(100*len(korrekte)/(IMAX*1.0),0)
print "Eine Quote von %s Prozent." % quote
#print "Fehlerliste"
#for f in fehlerliste:
#    print f["aufgabe"].pruefung(f["eingabe"], test=False)
