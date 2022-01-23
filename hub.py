#!/usr/bin/ env python3
#pckg import
import sys
import os
import math
import time
from sys import platform
from datetime import datetime

from matplotlib import backend_managers
#global variable declarations
y = ["Y", "y", "YES", "yes", "Yes", "1"]
n = ["N", "n", "NO", "no", "No", "0"]
percent = "%"
today = datetime.today()
date = today.strftime("\n%d/%m/%Y @ %H:%M:%S")
#global functions
def clear():
    if "linux" in sys.platform:
        os.system("clear")
    if "win32" in sys.platform:
        os.system("cls")
def exit():
    clear()
    sys.exit("Exiting...")
def loady(msg:int, times:int):
    clear()
    animation = "|/-\\"
    if str(msg) == "reset":
        for i in range(times):
            time.sleep(0.1)
            sys.stdout.write("\r" + "Resetting... " + animation[i % len(animation)])
            sys.stdout.flush()
    if str(msg) == "math":
        for i in range(times):
            time.sleep(0.1)
            sys.stdout.write("\r" + "Doing Maths... " + animation[i % len(animation)])
            sys.stdout.flush()
    if str(msg) == "moduleLoad":
        for i in range(times):
            time.sleep(0.1)
            sys.stdout.write("\r" + "Loading Module... " + animation[i % len(animation)])
            sys.stdout.flush()
    if str(msg) == "log":
        for i in range(times):
            time.sleep(0.1)
            sys.stdout.write("\r" + "Logging... " + animation[i % len(animation)])
            sys.stdout.flush()
    if str(msg) == "load":
        for i in range(times):
            time.sleep(0.1)
            sys.stdout.write("\r" + "Loading...  " + animation[i % len(animation)])
            sys.stdout.flush()
    clear()
#main function
def intro():
    loady("load", 15)
    while True:
        print("""
Welcome to Quick Maths!\n
    1.) Percent Change Calculator.        4.) Interest Calculator.
    2.) Dollar Cost Averager.             5.) Tax Calculator.
    3.) Entry Maths.                      6.) Bill Calculator.\n
                          0.) To Exit.\n\n
    X.) Log Tools.
        """)
        introSelection = input("Please select an option\n: ")
        if introSelection == "1":
            pChange()
            continue
        if introSelection == "2":
            dca()
            continue
        if introSelection == "3":
            eMath()
            continue
        if introSelection == "4":
            iMath()
            continue
        if introSelection == "5":
            taxCalculator()
            continue
        if introSelection == "6":
            billCalculator()
            continue
        if introSelection.lower() == "x":
            logTools()
        if introSelection == "0":
            exit()
        else:
            clear()
            invalidInput = input("Not a valid option. Want to try again? (Y/N)\n: ")
            if invalidInput.lower() in y:
                intro()
            else:
                exit()
#referenced functions
def pChange():
    loady("moduleLoad", 10)
    func = "Percent Change Calculator"
    pcCurrent = float(input("Enter the current price\n: "))
    pcFinal = float(input("Enter the final price\n: "))
    pcChange = (pcCurrent - pcFinal) / pcCurrent
    pcFormat = "%.0f%%" % (-100 * pcChange)
    result = "Current Price: $" + str(pcCurrent) + "\nFinal Price: $" + str(pcFinal) + "\nPercent Change: " + pcFormat + "\n"
    clear()
    loady("math", 20)
    print(result)
    logInput = input("Do you want to log this output? (Y/N)\n: ")
    if logInput.lower() in y:
        with open("trade.log", "a+") as file:
            file.write(date + " | " + func + "\n" + result)
        loady("log", 12)
        loady("reset", 15)
    else:
        loady("reset", 15)
        intro()
def dca():
    loady("moduleLoad", 10)
    func = "Dollar Cost Average"
    dcaInput = [float(x) for x in input("Please enter dollar amounts with spaces inbetween.\n$: ").split()]
    dcaAverage = (sum(dcaInput) / len(dcaInput))
    dcaValues = "Values: $" + str(dcaInput)
    result = "Average: $" + str(dcaAverage) + "\n"
    loady("math", 20)
    print(dcaValues)
    print(result)
    logInput = input("Do you want to log this output? (Y/N)\n: ")
    if logInput.lower() in y:
        with open("trade.log", "a+") as file:
            file.write(date + " | " + func + "\n" + result)
        loady("log", 12)
        loady("reset", 15)
    else:
        loady("reset", 15)
        intro()
def eMath():
    loady("moduleLoad", 10)
    func = "Entry Maths"
    emTicker = str(input("Please enter the emTicker:\n: "))
    emEntry = [float(x) for x in input("Please enter the entry point. *add spaces for dca*\n$: ").split()]
    emEntry = (sum(emEntry) / len(emEntry))
    emVolume = float(input("Please enter number of " + emTicker.upper() + " purchased:\n#: "))
    clear()
    print("""How would you like to setup your trade?\n
    1.) 3:6
    2.) 6:12
    3.) Custom
    """)
    emTradeParams = int(input("Please select an option\n: "))
    clear()
    if emTradeParams == 1:
        emTake = (emEntry * 0.06) + emEntry
        emStop = emEntry - (emEntry * 0.03)
    elif emTradeParams == 2:
        emTake = (emEntry * 0.12) + emEntry
        emStop = emEntry - (emEntry * 0.06)
    elif emTradeParams == 3:
        emTake = float(input("Where will you sell?\n$: "))
        emStopIN = str(input("Do you want to set a stop loss?(Y/N)\n: "))
        if emStopIN in y:
            emStop  = input("Where do you want to set a stop? *for percent of postion add percent sign*\n$: ")
        if emStopIN in n:
            emStop = "NA"
    else:
        print("Not a valid option...")
        loady("reset", 15)
        eMath()
    emPosition = emEntry * emVolume
    emProfit = (emTake - emEntry) * emVolume
    emFutPlus = emProfit + emPosition
    if emStop == "NA":
        emLoss = "NA"
    elif "%" in emStop:
        emStop = emStop.replace("%", "")
        emStop =  emEntry - ((int(emStop) / 100) * emEntry)
    emLoss = ((emEntry - emStop) * emVolume)
    emFutMinus = emPosition - emLoss
    result = "emTicker: " + str(emTicker.upper()) + "\n\nEntry: $" + str(emEntry) + "\nVolume: x" + str(emVolume) + "\nPosition: $" + str(emPosition) + "\nFuture Position: (+)$" + str(emFutPlus) + " | (-)$" + str(emFutMinus)+ "\n\nTake: $" + str(emTake) + "\nStop: $" + str(emStop) + "\n\nProfit: $" + str(emProfit) + "\nLoss: $" + str(emLoss) + "\n"
    loady("math", 20)
    print(result)
    logInput = input("Do you want to log this output? (Y/N)\n: ")
    if logInput.lower() in y:
        with open("trade.log", "a+") as file:
            file.write(date + " | " + func  + "\n" + result)
        loady("log", 12)
        loady("reset", 15)
    else:
        loady("reset", 15)
        intro()
def iMath():
    loady("moduleLoad", 10)
    func = "Interest Calculator"
    imRate = float(input("Please enter the interest rate:\n%: "))
    imVolume = float(input("Please enter borrowed amount:\n$: "))
    loady("math", 7)
    imResult = (imRate / 100) * imVolume
    result = "Interest Rate: " + str(imRate) + "%\n" + "Borrowed Amount: $" + str(imVolume) + "\n" +"Interest Expense: $" + str(imResult) + "\n"
    print(result)
    logInput = input("Do you want to log this output? (Y/N)\n: ")        
    if logInput.lower() in y:
        with open("trade.log", "a+") as file:
            file.write(date + " | " + func + "\n" + result)
        loady("log", 12)
        loady("reset", 15)
    else:
        loady("reset", 15)
        intro()
def taxCalculator():
    loady("moduleLoad",10)
    func = "Tax Calculator"
    tcVolume = int(input("How much did you spend?\n$ "))
    clear()
    print("""Which Taxes?
    1.) Sales
    2.) Sales + MJ
    """)
    tcParam = input("Please select an option.\n: ")
    if tcParam == "1":
        func = "Sales Tax Calculator"
        tcResult = tcVolume + (tcVolume * 0.0825)
        result = "Result: " + str(tcResult)
    elif tcParam == "2":
        func = "MJ Tax Calculator"
        tcResult = tcVolume + (tcVolume * 0.1625)
        result = "Result: " + str(tcResult) +"\n"
    loady("math",7)
    print(result)
    logInput = input("Do you want to log this output? (Y/N)\n: ")        
    if logInput.lower() in y:
        with open("trade.log", "a+") as file:
            file.write(date + " | " + func + "\n" + result)
        loady("log", 12)
        loady("reset", 15)
    else:
        loady("reset", 15)
        intro()
def billCalculator():
    loady("moduleLoad", 10)
    func = "Bills"
    bcList = []
    bcElectric = float(input("Electric Bill\n$ "))
    bcGas = float(input("Gas Bill\n$ "))
    bcUtility = float(input("Utility Bill\n$ "))
    bcInternet = float(input("Internet Bill\n$ "))
    bcList.append(bcElectric + bcGas + bcUtility + bcInternet)
    bcSplit = int(input("How are you splitting the bills?\n: "))
    bcTotal = sum(bcList)
    bcTSplit = bcTotal / bcSplit
    bcESplit = bcElectric / bcSplit
    bcGSplit = bcGas / bcSplit
    bcUSplit = bcUtility / bcSplit
    bcISplit = bcInternet / bcSplit
    result = "Electric Bill: $" + str(bcElectric) + " ($" + str(bcESplit) + ")" + "\nGas Bill: $" + str(bcGas) + " ($" + str(bcGSplit) + ")" + "\nUtility Bill: $" + str(bcUtility) + " ($" + str(bcUSplit) + ")" + "\nInternet Bill: $" + str(bcInternet) + " ($" + str(bcISplit) + ")" + "\n\nTotal: $" + str(bcTotal) + " ($" + str(bcTSplit) + ")\n"
    loady("math",7)
    print(result)
    logInput = input("Do you want to log this output? (Y/N)\n: ")        
    if logInput.lower() in y:
        with open("bills.log", "a+") as file:
            file.write(date + " | " + func + "\n" + result)
        loady("log", 12)
        loady("reset", 15)
    else:
        loady("reset", 15)
        intro()
def logTools():
    loady("moduleLoad",10)
    while True:
        print("""Log tools:\n
        1.) Read Log.
        2.) Reset Log.
        0.) Back
        """)
        logSelection = input("How would you like to proceed?\n: ")
        if logSelection == "1":
            clear()
            with open("trade.log", "r") as file:
                text = file.read()
                print(text)
            input("Press enter to continue...")
            logTools()
        if logSelection == "2":
            clear()
            logResetConf = input("Are you sure you want to continue? This will reset the log file. (Y/N)\n: ")
            if logResetConf.lower() in y:
                loady("reset", 10)
                with open("trade.log", "w") as file:
                    file.write("")
                logTools()
            else:
                logTools()
        if logSelection == "0":
            intro()
        else:
            clear()
            invalidInput = input("Not a valid option. Want to try again? (Y/N)\n: ")
            if invalidInput.lower() in y:
                logTools()
            else:
                intro()
#main function call
def main():
    intro()
#dunder check
if __name__ == "__main__":
    main()