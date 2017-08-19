
inp = input("Enter a string : ")
inp = inp.split()

for word in inp:
    index = inp.index(word)
    inp[index] = word.capitalize()
original = ' '.join(w for w in inp)
print (original)
