#!/usr/bin/python3
############################
#                                                          #
#                                                          #
#         -maths hub 1.0 upgrade-       #
#            Slimmed down test              #
#           version of maths hub            #
#                                                          #
#                                                          #
############################





#pckg import
import sys
import os
import time
from sys import platform
from datetime import datetime
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich import print
#global variable declarations
y = ["Y", "y", "YES", "yes", "Yes", "1"]
n = ["N", "n", "NO", "no", "No", "0"]
console = Console()
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
    if str(msg) == "reset":
        console = Console(style = "light red")
        with console.status("[light red] Resetting...[/]", spinner = "dots"):
            for i in range(times):
                time.sleep(0.1)
    if str(msg) == "math":
        console = Console(style = "cyan")
        with console.status("[cyan]Doing Maths...[/]", spinner = "material"):
            for i in range(times):
                time.sleep(0.1)
    if str(msg) == "moduleLoad":
        console = Console(style = "purple")
        with console.status("[purple] Loading Module...[/]", spinner = "point"):
            for i in range(times):
                time.sleep(0.1)
    if str(msg) == "log":
        console = Console(style = "cyan")
        with console.status("[cyan] Logging...[/]", spinner = "growHorizontal"):
            for i in range(times):
                time.sleep(0.1)
    if str(msg) == "load":
        console = Console(style = "green")
        with console.status("[green]Loading...[/]", spinner = "aesthetic"):
            for i in range(times):
                time.sleep(0.1)
    if str(msg) == "exit":
        console = Console(style = "light red")
        with console.status("[red]Exiting...[/]", spinner = "growVertical"):
            for i in range(times):
                time.sleep(0.1)
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
            eMath()
#main function
def intro():
    loady("load", 15)
    while True:
        print("""        [bold green]Welcome to Quick Maths! [/]""")
        print("""
[green] 1.) Entry Maths.        2.) Filler.\n[/]
             [bold red]0.) To Exit.\n [/]
          [purple] 9.) Log Settings. [/]
        """)
        introSelection = Prompt.ask("[bold cyan]Please select an option\n: [/]", choices=["1", "9", "0"], show_choices=False)
        if introSelection == "1":
            modSwitch(1)
            eMath()
            continue
        if introSelection.lower() == "9":
            logTools()
        if introSelection == "0":
            loady("exit", 10)
            exit()
#referenced functions
def eMath():
    loady("moduleLoad", 10)
    global func
    func = "Entry Maths"
    emTicker = str(Prompt.ask("[bold green]Please enter the ticker:\n: "))
    if emTicker.isalpha() and len(emTicker) == 3:
        emValues = [float(x) for x in Prompt.ask("Please enter the entry point.\n*add spaces for average / correspond volume(x) with share price($).*\n$: ").split() if isFloat(x)]
        emVolumes = [float(x) for x in Prompt.ask("x: ").split() if isFloat(x)]
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