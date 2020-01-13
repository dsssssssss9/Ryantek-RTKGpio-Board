b = []
for index in range (2,3):
num = 49
while num != 0:
    bit = num % 2
    b.append(bit)
    num = int (num / 2 )

b = b[::-1]

#b = reversed (b)

for i in b:
    print (i)

    


    
LED_pins([1,0],[2,0],[3,0])

for i in b:
    LED_pins([i] [1]) = b(i)
    
