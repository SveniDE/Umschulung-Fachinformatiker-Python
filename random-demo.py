import random  # Modul für Pseudo-Zufallszahlen
random.seed(100)   # Random-Generator auf Startwert festlegen
print(random.randint(0,100)) # Erzeugt Zufallszahlen von 0...100
print(random.randrange(0,100)) # Erzeugt ZZ von 0...99
print(random.uniform(0,100)) # Erzeugt ZZ als Float von 0...100
print(random.random()) # Erzeugt eine ZZ von 0...1 als Float
liste = ["Ja", "Nein", "Vielleicht"]
print(random.choice(liste)) # Wählt einen Zufälligen Wert aus einer Liste