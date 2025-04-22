# ui_terminal.py

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

print("[DEBUG] ui_terminal.py loaded")

def display_result(prompt, response, evaluation):
    console.rule("[bold green]Scenario Prompt")
    console.print(Text(prompt, style="italic white"))

    console.rule("[bold cyan]Model Response")
    console.print(Panel.fit(response, border_style="cyan"))

    console.rule("[bold magenta]Ethical Evaluation")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Scenario ID")
    table.add_column("Moral Axis")
    table.add_column("Contradiction")
    table.add_column("Keywords")

    table.add_row(
        evaluation.get("scenario_id", "?"),
        evaluation.get("moral_axis", "?"),
        str(evaluation.get("contradiction", False)),
        ", ".join(evaluation.get("keywords", []))
    )

    console.print(table)
    console.rule("[bold red]End of Scenario", style="red")