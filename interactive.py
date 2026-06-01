from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.text import Text

console = Console()


def caesar_cipher(text, shift, direction):
    result = ""

    if direction == "L":
        shift = -shift
    elif direction == "R":
        pass
    else:
        return None

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def main():
    console.clear()
    console.print(
        Panel.fit(
            "[bold cyan]🔐 Caesar Cipher Tool 🔐[/bold cyan]",
            border_style="cyan",
        )
    )

    message = Prompt.ask("\n[bold yellow]Enter message[/bold yellow]")
    shift = IntPrompt.ask("[bold yellow]Enter shift key[/bold yellow]")
    direction = Prompt.ask(
        "[bold yellow]Choose direction[/bold yellow] (L = Left, R = Right)",
        choices=["L", "R"],
        default="R",
    ).upper()

    encrypted = caesar_cipher(message, shift, direction)

    if encrypted is None:
        console.print("\n[bold red]❌ Invalid direction! Use L or R.[/bold red]")
        return

    opposite = "L" if direction == "R" else "R"
    decrypted = caesar_cipher(encrypted, shift, opposite)
    output_text = Text()
    output_text.append("Encrypted Message:\n", style="bold green")
    output_text.append(f"{encrypted}\n\n", style="white")
    output_text.append("Decrypted Message:\n", style="bold magenta")
    output_text.append(f"{decrypted}", style="white")

    console.print(
        Panel(
            output_text,
            title="[bold blue]Result[/bold blue]",
            border_style="blue",
        )
    )


if __name__ == "__main__":
    main()
