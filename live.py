#!/usr/bin/env python3
import sys
import os
import math
import time
from sys import platform
from datetime import datetime

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt
from rich.live import Live
def layoutMake() -> Layout:
    layout = Layout(name="root")
    layout.split_row(
        Layout(name="prompt"),
        Layout(name="io")
    )
    layout["io"].split_column(
        Layout(name="output"),
        Layout(name="input")
    )
    return layout
def intro() -> Panel:
    splashMsg = Table.grid(padding=2)
    splashMsg.add_column(style="green", justify="center")
    splashMsg.add_row("1. Mileage Calculator")
    splashMsg.add_row("2. Filler")
    splashMsg.add_row("9. Log Tools")
    splashMsg.add_row("0. Exit")
    qPrompt= Prompt.ask("How would you like to proceed?", choices=["1", "2", "9", "0"], show_choices=False)
    prompt = Table.grid(padding=1)
    prompt.add_column()
    prompt.add_column(no_wrap=True)
    prompt.add_row(qPrompt, splashMsg)

    splash_panel = Panel(
        Align.center(
            Group(splashMsg, "\n", Align.center(qPrompt)),
            horizontal="middle",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="Welcome to Quick Maths!",
        border_style="green"
    )
    return splash_panel
# while True:
#     print("""        [bold green]Welcome to Quick Maths! [/]""")
#     print("""
# [green] 1.) Entry Maths.        2.) Filler.\n[/]
#             [bold red]0.) To Exit.\n [/]
#         [purple] 9.) Log Settings. [/]
#     """)
#     introSelection = Prompt.ask("[bold cyan]Please select an option\n: [/]", choices=["1", "9", "0"], show_choices=False)
#     if introSelection == "1":
#         mlgCalc()
#         return False
# test figures
def mlgCalc():
    mDest = (float(input("Miles to Destination?\n: ")))
    mMPG = (float(input("Miles per Gallon?\nmpg: ")))
    mCPG = (float(input("Cost per Gallon?\n$: ")))
    mGallonsToDest = mDest / mMPG
    mFinal = (mDest/ mMPG) * mCPG
    result = f"\tMiles to Destination: {mDest}\mi\nMiles Per Gallon: {mMPG}\mpg\nCost Per Gallon: ${mCPG}\n\nResult: ${mFinal}"




layout = layoutMake()
layout["prompt"].update(intro())
with Live(layout, refresh_per_second=10, screen=True):
    while True:
        layout["prompt"].update(intro())













# def mlgCalc():
    # clear()
    # global func
    # func = "Mileage Calculator"
    # loady("moduleLoad", 10)
    # mMileage = (float(input("Miles to Destination?\n: ")))
    # mMPG = (float(input("Miles per Gallon?\nmpg: ")))
    # mPPG = (float(input("Cost per Gallon?\n$: ")))
    # mRTrip = input("Is this a round trip? (Y/N)\n: ")
    # if mRTrip in y:
    #     mMileage = mMileage * 2
    # mGallonsToDest = mMileage / mMPG
    # mFinal = (mMileage / mMPG) * mPPG
    # mWeekly = mFinal * 5
    # mMonthly = mFinal * 20
    # #result = "Miles to Destination: " + str(mMileage) + "\n" + "Miles per Gallon: " + str(mMPG) + "\n" + "Cost per Gallon: $" + str(mPPG) + "\n\n" + "Cost per Trip: $" + str(final) + "\n"
    # global result
    # result = "\tMiles to Destination: {0}/mi\n\tMiles per Gallon: {1}/gal\n\tCost per Gallon: ${2}\n\tGallons per Trip: {3}/gal\n\n\tCost per Trip: ${3}\n\tCost per Week: ${4}\n\tCost per Month: ${5}\n".format(mMileage, mMPG, mPPG, mGallonsToDest, mFinal, mWeekly, mMonthly)
    # loady("math", 7)
    # print(func + ":\n" + result)
    # oSave("mileage.log")