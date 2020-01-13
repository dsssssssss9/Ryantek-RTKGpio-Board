import time





def dec2bin(n):
    b = []
#for index in range (2,3):
    num = n
    while num != 0:
        bit = num % 2
        b.append(bit)
        num = int (num / 2 )

    b = b[::-1]

    #b = reversed (b)

    for i in b:
        print (i, "\n")

for index in range (1,16):
    dec2bin(index)
    time.sleep(2)

    


