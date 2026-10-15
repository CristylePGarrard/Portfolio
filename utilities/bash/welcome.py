import os
import shutil
import time
import sys
import datetime
import subprocess

from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
import pyfiglet

console = Console()

def big_banner(name):
    width = shutil.get_terminal_size().columns
    fig = pyfiglet.Figlet(font='slant', width=width)
    return fig.renderText(name)

def gradient_text(text):
    colors = [
        "#ff00ff",
        "#ff66ff",
        "#cc66ff",
        "#9966ff",
        "#6699ff",
        "#33ccff",
        "#00ffff"
    ]
    rich_text = Text()
    for i, char in enumerate(text):
        rich_text.append(char, style=f"bold {colors[i % len(colors)]}")
    return rich_text

def get_battery():
    try:
        output = subprocess.check_output(
            ["pmset", "-g", "batt"],
            text=True
        )
        percent = output.split("\n")[1].split(";")[0].split()[-1]
        return percent
    except Exception:
        return "?"

def main():
    name = os.environ.get("MY_NAME", "Cristyle")
    handle = os.environ.get("MY_HANDLE", "")
    emoji = os.environ.get("MY_EMOJI", "🌸")

    banner = big_banner(name)
    banner_text = gradient_text(banner)

    small_text = Text("\n" + small, style="bold white")

    combined = Text()
    combined.append(banner_text)
    combined.append(small_text)

    content = Panel(
        Align.center(combined),
        border_style=color
    )

    battery = get_battery()
    now = datetime.datetime.now().strftime("%A %H:%M")

    small = f"{emoji}  {handle}  |  🔋 {battery}  |  {now}  {emoji}"

    colors = ["bright_magenta", "bright_blue", "bright_cyan", "bright_green"]

    with Live(refresh_per_second=12) as live:
        for i in range(20):
            color = colors[i % len(colors)]

            combined = Text()
            combined.append(gradient_text(banner))
            combined.append(Text("\n" + small, style="bold white"))

            content = Panel(
                Align.center(combined),
                border_style=color
            )

            live.update(content)
            time.sleep(0.05)

if __name__ == "__main__":
    main()