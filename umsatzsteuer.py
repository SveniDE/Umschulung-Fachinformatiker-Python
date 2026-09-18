brutto=float(input("Bruttobetrag> "))

steuer=brutto*0.19

netto=brutto-steuer

print("Der Bruttobetrag ist: ", brutto)
print("Die Steuern sind: ", round(steuer,2))
print("Der Nettobetrag ist: ", netto)
