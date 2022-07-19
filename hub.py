#!/usr/bin/ env python3
#pckg import
import sys
import os
import math
from tempfile import TemporaryFile
from this import d
import time
from sys import platform
from datetime import datetime
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
def isFloat(num):
    try:
        float(num)
        return True
    except:
        clear()
        a = input("Invalid Input! Would you like to try again? (Y/N)\n: ")
        if a in y:
            eMath()
        else:
            intro()
#main function
def intro():
    loady("load", 15)
    while True:
        print("""        Welcome to Quick Maths!\n
1.) Percent Change.        5.) Interest.
2.) Dollar Cost.           6.) Taxes.
3.) Entry Maths.           7.) Bills.
4.)                        8.) Mileage\n
             0.) To Exit.\n
X.) Log Settings.
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
#       if introSelection == "4":
#           placeholder()
#           continue
        if introSelection == "5":
            iMath()
            continue
        if introSelection == "6":
            taxCalculator()
            continue
        if introSelection == "7":
            billCalculator()
            continue
        if introSelection == "8":
            mlgCalc()
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
    result = "Current Price: ${0}\nFinal Price: ${1}\nPercent Change: {2}\n".format(str(pcCurrent), str(pcFinal), str(pcFormat))
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
    dcaSharePrices = [float(x) for x in input("Please enter dollar amounts with spaces inbetween. *correspond volume(x) with share price($).*\n$: ").split()]
    dcaVolumes = [float(x) for x in input("x: ").split()]
    if len(dcaSharePrices) == len(dcaVolumes):
        dcaTotalVolume = sum(dcaVolumes)
        dcaTotal = 0
        for v, p in zip(dcaSharePrices, dcaVolumes):
            dcaTotal += (v * p)
            for j in ["[", "]"]:
                dcaSharePrices = str(dcaSharePrices).replace(j, "")
                dcaVolumes = str(dcaVolumes).replace(j, "")
        dcaAvg = dcaTotal / dcaTotalVolume
        result = "Values: ${0}\nVolumes: x{1}\nAverage: {2}".format(dcaSharePrices, dcaVolumes, str(dcaAvg))
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
    if len(dcaSharePrices) != len(dcaVolumes):
        a = input("Not in correspondence! Do you want to try again? (Y/N)\n: ")
        if a in y:
            dca()
        else:
            loady("reset", 15)
            intro()
def eMath():
    loady("moduleLoad", 10)
    func = "Entry Maths"
    emTicker = str(input("Please enter the ticker:\n: "))
    if emTicker.isalpha() and len(emTicker) == 3:
        emValues = [float(x) for x in input("Please enter the entry point. *add spaces for average / correspond volume(x) with share price($).*\n$: ").split() if isFloat(x)]
        emVolumes = [float(x) for x in input("x: ").split() if isFloat(x)]
        while len(emValues) == len(emVolumes):
            emTotalVolume = sum(emVolumes)
            dcaTotal = 0
            for v, p in zip(emValues, emVolumes):
                dcaTotal += (v * p)
            emAvg = dcaTotal / emTotalVolume
            clear()
            while True:
                print("""How would you like to setup your trade?\n
        1.) 3:6
        2.) 6:12
        3.) Custom
                """)
                emTradeParams = input("Please select an option\n: ")
                clear()
                if emTradeParams == "1":
                    emTake = (emAvg * 0.06) + emAvg
                    emStop = emAvg - (emAvg * 0.03)
                elif emTradeParams == "2":
                    emTake = (emAvg * 0.12) + emAvg
                    emStop = emAvg - (emAvg * 0.06)
                elif emTradeParams == "3":
                    emTake = float(input("Where will you sell?\n$: "))
                    emStopIN = str(input("Do you want to set a stop loss?(Y/N)\n: "))
                    if emStopIN in y:
                        emStop  = input("Where do you want to set a stop? *for percent of entry postion add percent sign*\n$: ")
                    elif emStopIN in n:
                        emStop = "NA"
                    else:
                        clear()
                        continue
                else:
                    input("Not a valid option! Press enter to continue...")
                    loady("reset", 15)
                    eMath()
                emPosition = emAvg * emTotalVolume
                emProfit = (emTake - emAvg) * emTotalVolume
                emFutPlus = emProfit + emPosition
                if emStop == "NA":
                    emLoss = "NA"
                if "%" in str(emStop):
                    emStop =  emAvg - ((float(emStop.replace("%", "")) / 100) * emAvg)
                emLoss = ((emAvg - emStop) * emTotalVolume)
                emFutMinus = emPosition - emLoss
                for j in ["[", "]"]:
                    emValues = str(emValues).replace(j, "")
                    emVolumes = str(emVolumes).replace(j, "")
                result = "Ticker: {0}\n\n\tValues: ${1}\n\tVolumes: x{2}\n\n\tAverage: ${3}\n\tTotal Volume: x{4}\n\tPosition: ${5}\n\tFuture Position: (+)${6} | (-)${7}\n\n\tTake: ${8}\n\tStop: ${9}\n\n\tProfit: ${10}\n\tLoss: ${11}\n".format(emTicker.upper(), emValues, emVolumes, emAvg, emTotalVolume, emPosition, emFutPlus, emFutMinus, emTake, emStop, emProfit, emLoss)
                loady("math", 20)
                print(result)
                logInput = input("Do you want to log this output? (Y/N)\n: ")
                if logInput.lower() in y:
                    with open("trade.log", "a+") as file:
                        file.write(date + " | " + func  + "\n" + result)
                    loady("log", 12)
                    loady("reset", 15)
                    intro()
                else:
                    loady("reset", 15)
                    intro()
        else:
            a = input("Not in correspondence! Do you want to try again? (Y/N)\n: ")
            if a in y:
                eMath()
            else:
                loady("reset", 15)
                intro()
    else:
        a = input("Invalid Input. Do you want to try again? (Y/N)\n: ")
        if a in y:
            eMath()
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
    imTotal = (imVolume + imResult)
   # result = "Interest Rate: " + str(imRate) + "%\n" + "Borrowed Amount: $" + str(imVolume) + "\n" +"Interest Expense: $" + str(imResult) + "\n"
    result = "Interest Rate: {0}%\nBorrowed Amount: ${1}\nInterest Expense: ${2}\n\nTotal Due: ${3}".format(str(imRate), str(imVolume), str(imResult), str(imTotal))
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
        result = "Result: {0}\n".format(tcResult)
    elif tcParam == "2":
        func = "MJ Tax Calculator"
        tcResult = tcVolume + (tcVolume * 0.1625)
        #result = "Result: " + str(tcResult) +"\n"
        result = "Result: {0}\n".format(tcResult)
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
    bcTotal = sum(bcList)
    bcSplit = int(input("How are you splitting the bills?\n: "))
    bcTSplit = bcTotal / bcSplit
    bcESplit = bcElectric / bcSplit
    bcGSplit = bcGas / bcSplit
    bcUSplit = bcUtility / bcSplit
    bcISplit = bcInternet / bcSplit
    #result = "Electric Bill: $" + str(bcElectric) + " ($" + str(bcESplit) + ")" + "\nGas Bill: $" + str(bcGas) + " ($" + str(bcGSplit) + ")" + "\nUtility Bill: $" + str(bcUtility) + " ($" + str(bcUSplit) + ")" + "\nInternet Bill: $" + str(bcInternet) + " ($" + str(bcISplit) + ")" + "\n\nTotal: $" + str(bcTotal) + " ($" + str(bcTSplit) + ")\n"
    result = "Electric Bill: ${0} (${1})\nGas Bill: ${2} (${3})\nUtility Bill: ${4} (${5})\nInternet Bill: ${6} (${7})\n\nTotal: ${8} (${9})\n".format(bcElectric, bcESplit, bcGas, bcGSplit, bcUtility, bcUSplit, bcInternet, bcISplit, bcTotal, bcTSplit)
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
def mlgCalc():
    clear()
    func = "Mileage Calculator"
    loady("moduleLoad", 10)
    mMileage = (float(input("Miles to Destination?\n: ")))
    mMPG = (float(input("Miles per Gallon?\nmpg: ")))
    mPPG = (float(input("Cost per Gallon?\n$: ")))
    final = (mMileage / mMPG) * mPPG
    #result = "Miles to Destination: " + str(mMileage) + "\n" + "Miles per Gallon: " + str(mMPG) + "\n" + "Cost per Gallon: $" + str(mPPG) + "\n\n" + "Cost per Trip: $" + str(final) + "\n"
    result = "Miles to Destination: {0}\nMiles per Gallon: {1}\nCost per Gallon: ${2}\n\nCost per Trip: ${3}\n".format(mMileage, mMPG, mPPG, final)
    loady("math", 7)
    print(result)
    logInput = input("Do you want to log this output? (Y/N)\n: ")        
    if logInput.lower() in y:
        with open("mileage.log", "a+") as file:
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
            print("""Log Files:\n
        1.) trade.log
        2.) bills.log
        3.) mileage.log
            """)
            logChoice = str(input("Which log file do you want to view?\n: "))
            if logChoice == "1":
                clear()
                with open("trade.log", "r") as file:
                    text = file.read()
                    print(text)
                input("Press enter to continue...")
                logTools()
            if logChoice == "2":
                clear()
                with open("bills.log", "r") as file:
                    text = file.read()
                    print(text)
                input("Press enter to continue...")
                logTools()
            if logChoice == "3":
                clear()
                with open("mileage.log", "r") as file:
                    text = file.read()
                    print(text)
                input("Press enter to continue...")
                logTools()
        if logSelection == "2":
            clear()
            print("""Log Files:\n
        1.) trade.log
        2.) bills.log
        3.) mileage.log
            """)
            rmChoice = str(input("Which log would you like to remove?\n: "))
            clear()
            if rmChoice == "1":
                logResetConf = input("Are you sure you want to continue? This will reset the log file. (Y/N)\n: ")
                if logResetConf.lower() in y:
                    loady("reset", 10)
                    with open("trade.log", "w") as file:
                        file.write("")
                    logTools()
                else:
                    logTools()
            elif rmChoice == "2":
                logResetConf = input("Are you sure you want to continue? This will reset the log file. (Y/N)\n: ")
                if logResetConf.lower() in y:
                    loady("reset", 10)
                    with open("bills.log", "w") as file:
                        file.write("")
                    logTools()
                else:
                    logTools()
            elif rmChoice == "3":
                logResetConf = input("Are you sure you want to continue? This will reset the log file. (Y/N)\n: ")
                if logResetConf.lower() in y:
                    loady("reset", 10)
                    with open("mileage.log", "w") as file:
                        file.write("")
                    logTools()
                else:
                    logTools()
            clear()
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