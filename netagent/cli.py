"""Typer-based CLI entry point.

Usage:
    netagent run --topology T1 --scenario bgp_md5_mismatch_r1_r2
    netagent benchmark --llm claude-sonnet --runs 5
"""

from __future__ import annotations

import typer
from rich.console import Console

app = typer.Typer(
    name="netagent",
    help="Adaptive LLM agent for network fault remediation.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def run(
    topology: str = typer.Option(..., help="Topology ID (T1/T2/T3/T4)"),
    scenario: str = typer.Option(..., help="Scenario name (see testbed/fault_scenarios/)"),
    llm: str = typer.Option("claude-sonnet", help="LLM to use"),
) -> None:
    """Run the agent against a single fault scenario."""
    console.print(f"[bold cyan]NetAgent[/bold cyan] — topology={topology} scenario={scenario} llm={llm}")
    console.print("[yellow]Stub — implement in Week 3.[/yellow]")


@app.command()
def benchmark(
    llm: str = typer.Option("claude-sonnet", help="LLM to evaluate"),
    runs: int = typer.Option(5, help="Runs per scenario"),
) -> None:
    """Run the full 50-scenario benchmark."""
    console.print(f"[bold cyan]NetAgent benchmark[/bold cyan] — llm={llm} runs={runs}")
    console.print("[yellow]Stub — implement in Week 9.[/yellow]")


@app.command()
def version() -> None:
    """Print version."""
    from netagent import __version__
    console.print(f"netagent {__version__}")


if __name__ == "__main__":
    app()
