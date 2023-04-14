l = int(input('starting from line: '))
u = int(input('end of the interval: '))

for num in range(l, u+1):
    if num > 1:

        for i in range(2, num):
            if num%i == 0:
                break
        else:
             print(num)