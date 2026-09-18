def primtest(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
 

def test_primtest():   # Ziel: Mindestens vollständige Codeüberdeckung
    assert primtest(2) == True  # Behauptungen (Testfälle) für die Funktion primtest
    assert primtest(3) == True
    assert primtest(4) == False
    assert primtest(5) == True
    assert primtest(1) == False
    assert primtest(-1) == False
    assert primtest(0) == False
    assert primtest(17) == True
    assert primtest(18) == False
    print("All tests passed")

test_primtest() # Aufruf der Testfunktion, um die Tests auszuführen