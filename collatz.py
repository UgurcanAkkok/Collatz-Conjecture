#!/usr/bin/python
while True:
    fnum = int(input("Enter the first number you want to start\n>>"))
    if fnum == "q":
        break
    nums = [fnum]
    def collatz(fnum):
        if fnum == 1 :
            for n in nums:
                print(int(n))
        elif fnum % 2 != 0:
            nnum = fnum * 3 + 1 
            nums.append(nnum)
            collatz(nnum)
        elif fnum % 2 == 0:
            nnum = fnum/2
            nums.append(nnum)
            collatz(nnum)

    collatz(fnum)
