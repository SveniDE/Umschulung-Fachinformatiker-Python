def hash16(text):
    hash = 0
    for i in range(0,len(text)):
        zeichen = text[i]
        asciiCode = ord(zeichen)
        hash = hash + (i*asciiCode)
    return (hash % 65536)

def hash64(text):
    hash = 0
    for i in range(0,len(text)):
        zeichen = text[i]
        asciiCode = ord(zeichen)
        hash = hash + (i*asciiCode)
    return (hash % 2**64)


while True:
    ein = input(">")
    print(hex(hash64(ein)))
 