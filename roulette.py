import random
words = open("../../../downloads/wortliste.txt","r").read()
words = words.replace("\n"," ")
words = words.split(" ")
_ = []
for w in words:
    OK = True
    for c in w:
        if not c.lower() in "abcdefghijklmnopqrstuvwxyz":
            OK = False

    if not OK:
        continue
    if w != "":
        _.append(w)
words = _
while 1:
    w = words[random.randint(0,len(words)-1)]
    x = input(f"Type {w}: ")
    if x == w:
        print("Good")
