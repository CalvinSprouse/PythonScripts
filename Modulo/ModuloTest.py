publicModulus = 2333
publicKey = 649
publicNumber = 166

aliceKey = 0
for i in range (1, publicModulus):
    if ((publicKey * i) % publicModulus == 1):
        aliceKey = i
        break

bobKey = 0
for i in range (1, publicModulus):
    if ((publicKey * i) % publicModulus == publicNumber):
        bobKey = i
        break

print ("Alice " + str(aliceKey))
print ("Bob " + str(bobKey))
