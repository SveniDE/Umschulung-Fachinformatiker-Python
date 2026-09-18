for i in range(-5,6):
    try:
        print(i,1/i)
    except Exception as fehler:
        print("Was komisches ist passiert, und zwar:", fehler)

