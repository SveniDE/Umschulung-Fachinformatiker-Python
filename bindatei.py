do = open("testzahlen.bin","wb")
for i in range(0,256):
    do.write(i.to_bytes(1))
do.close()

print("Datei geschrieben")