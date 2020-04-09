import os
import args
os.system("rm -r WA_test*")
os.system("g++ pattern.cpp -o pattern && g++ toCheck.cpp -o toCheck")
tCnt = 0
tCnt = args.setTestsCount(tCnt)
for t in range (1, tCnt + 1):
    s = args.getArgs()
    f = open("input.txt", "w")
    f.write(s);
    f.close();
    os.system("./pattern < input.txt > outPattern.txt && ./toCheck < input.txt > outToCheck.txt")
    if (os.system("diff -i outPattern.txt outToCheck.txt")):
        print("WA")
        os.system("cp input.txt WA_test#_" + str(t))
    else:
        print("AC")

