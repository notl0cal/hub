#!/usr/bin/ env python3
#pckg import
import sys
import os
import math
import time
from sys import platform
from datetime import datetime
#global variable declarations
y = ["Y", "y", "YES", "yes"]
n = ["N", "n", "NO", "no"]
today = datetime.today()
date = today.strftime("\n%d/%m/%Y @ %H:%M:%S")
#global functions
def clear():
    if "linux" in sys.platform:
        os.system("clear")
    if "win32" in sys.platform:
        os.system("cls")
def exit():
    sys.exit("Exiting...")
def resetting(times:int):
    animation = "|/-\\"
    for i in range(times):
        time.sleep(0.1)
        sys.stdout.write("\r" + "Resetting... " + animation[i % len(animation)])
        sys.stdout.flush()
    clear()
    print("Finished!")
    time.sleep(2)
    clear()
def loading(times:int):
    animation = "|/-\\"
    for i in range(times):
        time.sleep(0.1)
        sys.stdout.write("\r" + "Doing Maths... " + animation[i % len(animation)])
        sys.stdout.flush()
        clear()
    print("Finished!")
    time.sleep(2)
    clear()
#main function
def intro():
    clear()
    c = 1
    while c > 0:
        print("""
        Welcome to Quick Maths!\n
        1.) Percent Change Calculator.\n
        2.) Dollar Cost Averager.\n
        3.) Entry Maths.\n
        4.) Interest Calculator.\n
        9.) Read Log.\n
        0.) To Exit.\n
        """)
        a = input("Please select an option: ")
        if a == "1":
            clear()
            pChange()
            continue
        if a == "2":
            clear()
            dca()
            continue
        if a == "3":
            clear()
            eMath()
            continue
        if a == "4":
            clear()
            iMath()
            continue
        if a == "9":
            clear()
            readLog()
            continue
        if a == "0":
            clear()
            exit()
        else:
            clear()
            d = input("Not a valid option. Want to try again? (Y/N)")
            if d in y:
                continue
            else:
                exit()
#referenced functions
def pChange():
    func = "Percent Change Calculator"
    pc1 = float(input("Enter the current price: "))
    pc2 = float(input("Enter the final price: "))
    pc2 = (pc1 - pc2) / pc1
    result = "%.0f%%" % (-100 * pc2)
    clear()
    loading(20)
    clear()
    print(result)
    f = input("Do you want to save this file? (Y/N)")
    if f in y:
        with open("trade.log", "a+") as file:
            file.write(date + " | " + func + "\n" + result+ "\n")
    else:
        clear()
        resetting(15)
        intro()
def dca():
    func = "Dollar Cost Average"
    dca1 = [float(x) for x in input("Please enter dollar amounts with spaces inbetween.\n$: ").split()]
    dca2 = (sum(dca1) / len(dca1))
    dca1.sort()
    values = "\nValues: $" + str(dca1)
    result = "\nAverage: $" + str(dca2) + "\n"
    clear()
    loading(20)
    clear()
    print(values)
    print(result)
    f = input("Do you want to save this file? (Y/N)")
    if f in y:
        with open("trade.log", "a+") as file:
            file.write(date + " | " + func + result)
    else:
        clear()
        resetting(15)
        intro()
def eMath():
    func = "Entry Maths"
    ticker = str(input("Please enter the ticker:\n: "))
    em1 = float(input("Enter your entry point in dollars:\n$: "))
    eVol = float(input("Please enter number of " + ticker.upper() + " purchased:\n#: "))
    print("""
How would you like to setup your trade?

        1.) 3:6
        2.) 6:12
""")
    eRatio = int(input("Please select an option: "))
    if eRatio == 1:
        emTake = (em1 * 0.06) + em1
        emStop = em1 - (em1 * 0.03)
        ePos = em1 * eVol
        emProfit = (emTake - em1) * eVol
        emLoss = (em1 - emStop) * eVol
        eFut = emProfit + ePos
    elif eRatio == 2:
        emTake = (em1 * 0.12) + em1
        emStop = em1 - (em1 * 0.06)
        ePos = em1 * eVol
        emProfit = (emTake - em1) * eVol
        emLoss = (em1 - emStop) * eVol
        eFut = emProfit + ePos
    else:
        print("Not a valid option...")
        resetting(15)
        clear()
        eMath()
    result = "\nTicker: " + str(ticker.upper()) + "\n\nEntry: $" + str(em1) + "\nPosition: $" + str(ePos) + "\nFuture Position: $" + str(eFut) + "\n\nTake: $" + str(emTake) + "\nStop: $" + str(emStop) + "\n\nProfit: $" + str(emProfit) + "\nLoss: $" + str(emLoss) + "\n"
    clear()
    loading(25)
    clear()
    print(result)
    f = input("Do you want to save this file? (Y/N)")
    if f in y:
        with open("trade.log", "a+") as file:
            file.write(date + " | " + func  + result)
    else:
        clear()
        resetting(15)
        intro()
def iMath():
    func = "Interest Calculator"
    im1 = float(input("Please enter the interest rate:\n%:"))
    im2 = float(input("Please enter borrowed amount:\n$: "))
    clear()
    loading(7)
    clear()
    im3 = (im1 / 100) * im2
    result = "Interest Expense: $" + str(im3) + "\n"
    print(result)
    f = input("Do you want to save this file? (Y/N)")        
    if f in y:
        with open("trade.log", "a+") as file:
            file.write(date + " | " + func + "\n" + result)
    else:
        clear()
        resetting(15)
        intro()
def readLog():
    with open("trade.log", "r") as file:
        p = file.read()
        print(p)
    input("Press enter to continue...")
    resetting(15)
#main function call
def main():
    intro()
#dunder check
if __name__ == "__main__":
    main()