#!/usr/bin/ env python3
#pckg import
import sys
import os
import math
import time
from sys import platform
from datetime import datetime
#global variable declarations
y = ["Y", "y", "YES", "yes", "Yes", "1"]
n = ["N", "n", "NO", "no", "No", "0"]
percent = "%"
global func 
func = ""
global result
result = ""
global module
module = 0
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
    if str(msg) == "exit":
        for i in range(times):
            time.sleep(0.1)
            sys.stdout.write("\r" + "Exiting... " + animation[i % len(animation)])
    clear()
def oSave(file):
    logInput = input("Do you want to log this output? (Y/N)\n: ")
    if logInput.lower() in y:
        with open(file, "a+") as open_file:
            open_file.write(date + " | " + func + "\n" + result)
        loady("log", 12)
        loady("reset", 15)
    else:
        loady("reset", 15)
        intro()
def modSwitch(mod):
    global module
    module = mod
def isFloat(num):
    try:
        float(num)
        return True
    except:
        clear()
        a = input("Invalid Input! Would you like to try again? (Y/N)\n: ")
        if a.lower() in y and module == 1:
            pChange()
        if a.lower() in y and module == 2:
            dca()
        if a.lower() in y and module == 3:
            eMath()
        #if a.lower() in y and module == 4:
            #iMath()
        if a.lower() in y and module == 5:
            iMath()
        if a.lower() in y and module == 6:
            taxCalculator()
        if a.lower() in y and module == 7:
            billCalculator()
        if a.lower() in y and module == 8:
            mlgCalc()
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
            modSwitch(1)
            pChange()
            continue
        if introSelection == "2":
            modSwitch(2)
            dca()
            continue
        if introSelection == "3":
            modSwitch(3)
            eMath()
            continue
#       if introSelection == "4":
#           modSwitch(4)
#           placeholder()
#           continue
        if introSelection == "5":
            modSwitch(5)
            iMath()
            continue
        if introSelection == "6":
            modSwitch(6)
            taxCalculator()
            continue
        if introSelection == "7":
            modSwitch(7)
            billCalculator()
            continue
        if introSelection == "8":
            modSwitch(8)
            mlgCalc()
            continue
        if introSelection.lower() == "x":
            logTools()
        if introSelection == "0":
            loady("exit", 10)
            exit()
        else:
            clear()
            invalidInput = input("Not a valid option. Want to try again? (Y/N)\n: ")
            if invalidInput.lower() in y:
                intro()
            else:
                loady("exit", 10)
                exit()
#referenced functions
def pChange():
    loady("moduleLoad", 10)
    global func
    func = "Percent Change Calculator"
    pcCurrent = float(input("Enter the current price\n: "))
    pcFinal = float(input("Enter the final price\n: "))
    pcChange = (pcCurrent - pcFinal) / pcCurrent
    pcFormat = "%.0f%%" % (-100 * pcChange)
    global result
    result = "\tCurrent Price: ${0}\n\tFinal Price: ${1}\n\tPercent Change: {2}\n".format(str(pcCurrent), str(pcFinal), str(pcFormat))
    clear()
    loady("math", 20)
    print(func + ":\n" + result)
    oSave("trade.log")
def dca():
    loady("moduleLoad", 10)
    global func
    func = "Dollar Cost Average"
    dcaSharePrices = [float(x) for x in input("Please enter dollar amounts with spaces inbetween.\n*correspond volume(x) with share price($).*\n$: ").split() if isFloat(x)]
    dcaVolumes = [float(x) for x in input("x: ").split() if isFloat(x)]
    if len(dcaSharePrices) == len(dcaVolumes):
        dcaTotalVolume = sum(dcaVolumes)
        dcaTotal = 0
        for v, p in zip(dcaSharePrices, dcaVolumes):
            dcaTotal += (v * p)
            for j in ["[", "]"]:
                dcaSharePrices = str(dcaSharePrices).replace(j, "")
                dcaVolumes = str(dcaVolumes).replace(j, "")
        dcaAvg = dcaTotal / dcaTotalVolume
        global result
        result = "\tValue(s): ${0}\n\tVolume(s): {1}x\n\tAverage: {2}\n".format(dcaSharePrices, dcaVolumes, str(dcaAvg))
        loady("math", 20)
        print(func + ":\n" + result)
        oSave("trade.log")
    else:
        a = input("Not in correspondence! Do you want to try again? (Y/N)\n: ")
        if a in y:
            dca()
        else:
            loady("reset", 15)
            intro()
def eMath():
    loady("moduleLoad", 10)
    global func
    func = "Entry Maths"
    emTicker = str(input("Please enter the ticker:\n: "))
    if emTicker.isalpha() and len(emTicker) == 3:
        emValues = [float(x) for x in input("Please enter the entry point.\n*add spaces for average / correspond volume(x) with share price($).*\n$: ").split() if isFloat(x)]
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
                global result
                result = "Ticker: {0}\n\n\tValue(s): ${1}\n\tVolume(s): {2}x\n\n\tAverage: ${3}\n\tTotal Volume: {4}x\n\tPosition: ${5}\n\tFuture Position: (+)${6} | (-)${7}\n\n\tTake: ${8}\n\tStop: ${9}\n\n\tProfit: ${10}\n\tLoss: ${11}\n".format(emTicker.upper(), emValues, emVolumes, emAvg, emTotalVolume, emPosition, emFutPlus, emFutMinus, emTake, emStop, emProfit, emLoss)
                loady("math", 20)
                print(func + ":\n" + result)
                oSave("trade.log")
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
    global func
    func = "Interest Calculator"
    imRate = float(input("Please enter the interest rate:\n%: "))
    imVolume = float(input("Please enter borrowed amount:\n$: "))
    loady("math", 7)
    imResult = (imRate / 100) * imVolume
    imTotal = (imVolume + imResult)
   # result = "Interest Rate: " + str(imRate) + "%\n" + "Borrowed Amount: $" + str(imVolume) + "\n" +"Interest Expense: $" + str(imResult) + "\n"
    global result
    result = "\tInterest Rate: {0}%\n\tBorrowed Amount: ${1}\n\tInterest Expense: ${2}\n\n\tTotal Due: ${3}\n".format(str(imRate), str(imVolume), str(imResult), str(imTotal))
    print(func + ":\n" + result)
    oSave("trade.log")
def taxCalculator():
    loady("moduleLoad",10)
    global func
    func = "Tax Calculator"
    tcRate = 0.0825
    tcVolume = int(input("How much did you spend?\n: $"))
    clear()
    print("""Which Taxes?
    1.) Sales
    2.) Sales + MJ
    """)
    tcParam = input("Please select an option.\n: ")
    if tcParam == "1":
        func = "Sales Tax Calculator"
        tcResult = tcVolume + (tcVolume * tcRate)
        tcTax = tcResult - tcVolume
        tcRate = tcRate * 100
        #result = "Result: " + str(tcResult)
        result = "\tTax Rate: {2}%\n\tGross Spend: ${3}\n\tTaxes Due: ${0}\n\n\tResult: ${1}\n".format(tcTax, tcResult, tcRate, tcVolume)
    elif tcParam == "2":
        func = "MJ Tax Calculator"
        tcRate = 0.1625
        tcResult = tcVolume + (tcVolume * tcRate)
        tcTax = tcResult - tcVolume
        tcRate = tcRate * 100
        #result = "Result: " + str(tcResult) +"\n"
        result = "\tTax Rate: {2}%\n\tGross Spend: ${3}\n\tTaxes Due: ${0}\n\n\tResult: ${1}\n".format(tcTax, tcResult, tcRate, tcVolume)
    loady("math",7)
    print(func + ":\n" + result)
    oSave("trade.log")
def billCalculator():
    loady("moduleLoad", 10)
    global func
    func = "Bills"
    bcList = []
    bcElectric = float(input("Electric Bill\n:$"))
    bcGas = float(input("Gas Bill\n:$"))
    bcUtility = float(input("Utility Bill\n:$"))
    bcInternet = float(input("Internet Bill\n:$"))
    bcList.append(bcElectric + bcGas + bcUtility + bcInternet)
    bcTotal = sum(bcList)
    bcSplit = int(input("How are you splitting the bills?\n: "))
    bcTSplit = bcTotal / bcSplit
    bcESplit = bcElectric / bcSplit
    bcGSplit = bcGas / bcSplit
    bcUSplit = bcUtility / bcSplit
    bcISplit = bcInternet / bcSplit
    #result = "Electric Bill: $" + str(bcElectric) + " ($" + str(bcESplit) + ")" + "\nGas Bill: $" + str(bcGas) + " ($" + str(bcGSplit) + ")" + "\nUtility Bill: $" + str(bcUtility) + " ($" + str(bcUSplit) + ")" + "\nInternet Bill: $" + str(bcInternet) + " ($" + str(bcISplit) + ")" + "\n\nTotal: $" + str(bcTotal) + " ($" + str(bcTSplit) + ")\n"
    global result
    result = "\tElectric Bill: ${0} (${1})\n\tGas Bill: ${2} (${3})\n\tUtility Bill: ${4} (${5})\n\tInternet Bill: ${6} (${7})\n\n\tTotal: ${8} (${9})\n".format(bcElectric, bcESplit, bcGas, bcGSplit, bcUtility, bcUSplit, bcInternet, bcISplit, bcTotal, bcTSplit)
    loady("math",7)
    print(func + ":\n" + result)
    oSave("bills.log")
def mlgCalc():
    clear()
    global func
    func = "Mileage Calculator"
    loady("moduleLoad", 10)
    mMileage = (float(input("Miles to Destination?\n: ")))
    mMPG = (float(input("Miles per Gallon?\nmpg: ")))
    mPPG = (float(input("Cost per Gallon?\n$: ")))
    mRTrip = input("Is this a round trip? (Y/N)\n: ")
    if mRTrip in y:
        mMileage = mMileage * 2
    mGallonsToDest = mMileage / mMPG
    mFinal = (mMileage / mMPG) * mPPG
    mWeekly = mFinal * 5
    mMonthly = mFinal * 20
    #result = "Miles to Destination: " + str(mMileage) + "\n" + "Miles per Gallon: " + str(mMPG) + "\n" + "Cost per Gallon: $" + str(mPPG) + "\n\n" + "Cost per Trip: $" + str(final) + "\n"
    global result
    result = "\tMiles to Destination: {0}/mi\n\tMiles per Gallon: {1}/gal\n\tCost per Gallon: ${2}\n\tGallons per Trip: {3}/gal\n\n\tCost per Trip: ${3}\n\tCost per Week: ${4}\n\tCost per Month: ${5}\n".format(mMileage, mMPG, mPPG, mGallonsToDest, mFinal, mWeekly, mMonthly)
    loady("math", 7)
    print(func + ":\n" + result)
    oSave("mileage.log")
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