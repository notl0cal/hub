#!/usr/bin/env python3
import sys
import os
import math
import time
from sys import platform
from datetime import datetime
from rich import print
from rich.panel import Panel
from rich.layout import Layout
layout = Layout()
layout.split_column(
    Layout(name="left"),
    Layout(name="right")
)
layout["right"].split_row(
    Layout(name="upper"),
    Layout(name="lower")
)
print(layout)
mlg1 = 164
mlg2 = 14.980
mlg3 = 3.988281671
print((Panel.fit(f"""

Miles to Dest = {mlg1}\mlg
Cost per Trip = ${mlg2}
Cost per Gallon = ${mlg3}\gal


""", title="[red]Mileage Calculator")))