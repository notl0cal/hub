#!/usr/bin/env python3
import sys
import rich
from rich.console import Console
console = Console()
def main():
    with console.status("Working..."):
        do_work()


if __name__ == "__main__":
    main()