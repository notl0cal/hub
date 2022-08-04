#!/usr/bin/env python3
# import sys
# import os
# import time import sleep
# from rich.console import Console
# console = Console(style = "green")
# def main():
#     with console.status("Working...", spinner="aesthetic"):
#         for i in range(20):
#             time.sleep(2)
#             print(i)


# if __name__ == "__main__":
#     main()





# from time import sleep

# from rich.console import Console
# from rich.align import Align
# from rich.text import Text
# from rich.panel import Panel

# console = Console()

# with console.screen(style="bold white on red") as screen:
#     for count in range(5, 0, -1):
#         text = Align.center(
#             Text.from_markup(f"[blink]Don't Panic![/blink]\n{count}", justify="center"),
#             vertical="middle",
#         )
#         screen.update(Panel(text))
#         sleep(1)

import time

from rich.live import Live
from rich.table import Table

table = Table()
table.add_column("Row ID")
table.add_column("Description")
table.add_column("Level")

with Live(table, refresh_per_second=4) as live:  # update 4 times a second to feel fluid
    for row in range(12):
        live.console.print(f"Working on row #{row}")
        time.sleep(0.4)
        table.add_row(f"{row}", f"description {row}", "[red]ERROR")